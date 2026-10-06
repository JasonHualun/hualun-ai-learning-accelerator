"""用花伦本人声音（VoxCPM2 极致克隆）批量生成旁白。

不复制模型、不复制声音档案：直接加载 VoxCPM2 项目的 app.py，调用它的 heard_voice()，
声音档案以该项目 private/voice-profiles/user-primary/selected-profile.json 为唯一真源。
模型只加载一次，适合一次生成多句（如解释视频的全部旁白）。

用法（必须用 VoxCPM2 项目自己的 Python）：
  $VOXCPM/.venv/bin/python clone_batch.py jobs.json
jobs.json = [{"text": "第一句", "out": "/abs/a.mp3"}, ...]   # out 可为 .mp3 或 .wav
"""
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

VOXCPM = Path(os.environ.get(
    "VOXCPM_DIR", Path.home() / "Documents/Codex/projects/视频剪辑/tools/voxcpm2"))

if __name__ == "__main__":
    jobs = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    sys.path.insert(0, str(VOXCPM))
    os.chdir(VOXCPM)
    import app  # 加载模型（约 5GB，只加载一次）

    for i, job in enumerate(jobs, 1):
        out = Path(job["out"])
        out.parent.mkdir(parents=True, exist_ok=True)
        wav = Path(app.heard_voice(job["text"]))
        if out.suffix.lower() == ".wav":
            shutil.move(wav, out)
        else:
            subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", str(wav), str(out)], check=True)
            wav.unlink()
        print(f"[{i}/{len(jobs)}] {out.name}", flush=True)
