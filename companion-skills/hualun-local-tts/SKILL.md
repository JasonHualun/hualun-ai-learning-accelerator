---
name: hualun-local-tts
description: 花伦本地语音（文字转语音）共享入口：任何 Agent 需要把文字读成 mp3、给视频配旁白、生成带时间轴的字幕时，统一调用本 Skill 的 scripts/speak.sh。复用 Hermes 已装好的 edge-tts，声音以 Hermes 配置为唯一真源（当前云夏 zh-CN-YunxiaNeural），免费、无需 API Key、需要联网。触发词：「配音」「读出来」「转语音」「TTS」「旁白」「生成语音」。不做语音识别（听写转文字走 video-to-text）。
version: 1.0.0
author: 花伦 (Hualun)
owner: hualun
metadata:
  watermark: hualun
  brand: 花伦
  provenance: original-user-work
---

# 花伦本地语音 1.0.0

## 这是什么

把文字变成语音文件。Hermes 早已装好 edge-tts（借用微软 Edge「朗读」的声音，免费、无 Key、需联网），本 Skill 只是让其他 Agent 也能用同一份，**不另装、不复制程序**。

## 唯一真源

| 东西 | 在哪 | 规则 |
|---|---|---|
| 语音程序 | PATH 上的 `edge-tts`，没有则用 `~/.hermes/hermes-agent/venv/bin/edge-tts` | 脚本自动找；都找不到时**停下问用户**，不要自行重装 |
| 默认声音 | `~/.hermes/config.yaml` → `tts.edge.voice` | 换声音只改这一处，所有 Agent 跟着变；`--voice` 只用于单次临时试听 |

## 用法

```bash
S=~/.hermes/skills/hualun-local-tts/scripts/speak.sh   # 各运行时的软链接都指向同一原件
bash $S "要读的文字" out.mp3
bash $S -f 旁白.txt out.mp3 --subs out.vtt            # 同时出带时间轴的字幕，做视频时用
bash $S "试听" demo.mp3 --voice zh-CN-XiaoxiaoNeural  # 临时换声音
bash $S --which                                       # 查看当前程序和声音
```

- `--rate +10%` / `-10%` 调语速。
- 字幕 `.vtt` 可用 `ffmpeg -i out.vtt out.srt` 转格式。
- 一段旁白建议 ≤ 300 字分段生成，失败（网络）重试一次，仍失败报告用户；不要静默改用 Mac 自带 `say`，如需降级先说明。

## 本人克隆声音（VoxCPM2，可选）

用花伦本人声音时改走 `scripts/clone_batch.py`：它加载 VoxCPM2 项目（`~/Documents/Codex/projects/视频剪辑/tools/voxcpm2`，模型约 5GB，本地 MPS 推理）的 `heard_voice()`，声音档案以该项目 `private/voice-profiles/user-primary/selected-profile.json` 为唯一真源。模型只加载一次，适合一次生成多句。

```bash
VOX=~/Documents/Codex/projects/视频剪辑/tools/voxcpm2
$VOX/.venv/bin/python scripts/clone_batch.py jobs.json   # [{"text": "...", "out": "/abs/a.mp3"}, ...]
```

- 声音档案和参考录音属于隐私资料，**不复制、不移动、不写进 Vault**。
- 只用于本人声音；不得用来模仿他人。

## 边界

- 只做文字 → 语音；不做语音识别、不做声音克隆。
- 生成的音频属于调用方项目的产物，放在调用方的项目/运行目录，不写进 Vault。
