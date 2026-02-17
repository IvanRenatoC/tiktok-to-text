from __future__ import annotations
import shutil
import subprocess
from pathlib import Path


class DependencyError(RuntimeError):
    pass


def _require(cmd: str) -> None:
    if shutil.which(cmd) is None:
        raise DependencyError(
            f"No encuentro '{cmd}' en PATH. Instálalo y prueba de nuevo."
        )


def extract_audio(
    video_path: str | Path, audio_path: str | Path, sample_rate: int = 16000
) -> Path:
    _require("ffmpeg")
    video_path = Path(video_path)
    audio_path = Path(audio_path)
    audio_path.parent.mkdir(parents=True, exist_ok=True)

    cmd = [
        "ffmpeg",
        "-y",
        "-hide_banner",
        "-loglevel",
        "error",
        "-i",
        str(video_path),
        "-vn",
        "-ac",
        "1",
        "-ar",
        str(sample_rate),
        str(audio_path),
    ]
    subprocess.run(cmd, check=True)
    return audio_path
