from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
from .audio import extract_audio
from .download import download_tiktok
from .transcribe import transcribe


@dataclass
class RunOutputs:
    video_path: Path
    audio_path: Path
    transcript_txt: Path
    transcript_json: Path


def run(
    url: str,
    out_dir: str | Path = "outputs",
    model: str = "small",
    language: str = "es",
    keep_video: bool = False,
    cookies_from_browser: str | None = None,
    cookies_file: str | None = None,
) -> RunOutputs:
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    video_path = download_tiktok(
        url=url,
        out_dir=out_dir,
        filename_template="tiktok-%(id)s.%(ext)s",
        cookies_from_browser=cookies_from_browser,
        cookies_file=cookies_file,
    )

    audio_path = out_dir / "audio.wav"
    extract_audio(video_path, audio_path)

    transcript_txt = out_dir / "transcript.txt"
    transcript_json = out_dir / "transcript.json"
    transcribe(
        audio_path, transcript_txt, transcript_json, model_name=model, language=language
    )

    if not keep_video:
        try:
            video_path.unlink()
        except Exception:
            pass

    return RunOutputs(
        video_path=video_path,
        audio_path=audio_path,
        transcript_txt=transcript_txt,
        transcript_json=transcript_json,
    )
