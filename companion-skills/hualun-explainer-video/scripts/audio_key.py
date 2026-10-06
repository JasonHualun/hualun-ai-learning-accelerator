"""旁白音频的缓存命名（无第三方依赖，渲染端和预生成端共用，保证同一句话对得上同一个文件）。"""
import hashlib
import os

ENGINE = os.environ.get("EXPLAINER_TTS", "edge")      # edge = Hermes 云夏；clone = 本人克隆声音（VoxCPM2）
RATE = os.environ.get("EXPLAINER_RATE", "+0%")       # 语速，edge 直接用；clone 换算成 atempo


def key(text: str) -> str:
    return hashlib.md5(f"{ENGINE}|{RATE}|{text}".encode()).hexdigest()[:12] + ".mp3"


def atempo() -> float:
    return 1 + float(RATE.rstrip("%")) / 100
