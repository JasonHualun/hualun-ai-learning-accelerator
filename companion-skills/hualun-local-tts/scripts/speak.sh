#!/bin/bash
# 花伦本地语音：把文字转成 mp3（可选同时输出字幕）。
# 不另装语音程序：优先用 PATH 上的 edge-tts，找不到就用 Hermes 自带的那份。
# 声音唯一真源：~/.hermes/config.yaml 的 tts.edge.voice；可用 --voice 临时覆盖。
#
# 用法：
#   speak.sh "要读的文字" 输出.mp3 [--subs 字幕.vtt] [--voice zh-CN-XiaoxiaoNeural] [--rate +10%]
#   speak.sh -f 文本文件.txt 输出.mp3 [...]
#   speak.sh --which    # 只打印当前用的程序和声音
set -euo pipefail

find_bin() {
  if command -v edge-tts >/dev/null 2>&1; then command -v edge-tts; return; fi
  for p in "$HOME/.hermes/hermes-agent/venv/bin/edge-tts" "$HOME/.hermes/hermes-agent/.venv/bin/edge-tts"; do
    [ -x "$p" ] && { echo "$p"; return; }
  done
  echo "找不到 edge-tts：Hermes 自带的那份不在了。请先问用户再决定是否安装，不要自行重装。" >&2
  exit 2
}

hermes_voice() {
  local cfg="$HOME/.hermes/config.yaml"
  [ -f "$cfg" ] && awk '/^tts:/{t=1;next} t&&/^[^ ]/{t=0} t&&/voice:/{print $2; exit}' "$cfg"
}

BIN=$(find_bin)
VOICE=$(hermes_voice); VOICE=${VOICE:-zh-CN-YunxiaNeural}

if [ "${1:-}" = "--which" ]; then echo "程序: $BIN"; echo "声音: $VOICE"; exit 0; fi

if [ "${1:-}" = "-f" ]; then SRC=(--file "$2"); shift 2; else SRC=(--text "$1"); shift; fi
OUT="$1"; shift
EXTRA=()
while [ $# -gt 0 ]; do
  case "$1" in
    --subs)  EXTRA+=(--write-subtitles "$2"); shift 2 ;;
    --voice) VOICE="$2"; shift 2 ;;
    --rate)  EXTRA+=("--rate=$2"); shift 2 ;;
    *) echo "未知参数: $1" >&2; exit 1 ;;
  esac
done

# ${EXTRA[@]+...}：兼容 macOS 自带 bash 3.2（空数组配 set -u 会报 unbound variable）
"$BIN" --voice "$VOICE" "${SRC[@]}" --write-media "$OUT" ${EXTRA[@]+"${EXTRA[@]}"}
