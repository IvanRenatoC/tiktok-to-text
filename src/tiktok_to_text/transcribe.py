from __future__ import annotations
import json
from pathlib import Path
import whisper


def transcribe(
    audio_path: str | Path,
    out_txt: str | Path,
    out_json: str | Path,
    model_name: str = "small",
    language: str = "es",
) -> str:
    audio_path = Path(audio_path)
    out_txt = Path(out_txt)
    out_json = Path(out_json)
    out_txt.parent.mkdir(parents=True, exist_ok=True)
    out_json.parent.mkdir(parents=True, exist_ok=True)

    model = whisper.load_model(model_name)
    result = model.transcribe(str(audio_path), language=language, fp16=False)
    text = (result.get("text") or "").strip()

    out_txt.write_text(text + "\n", encoding="utf-8")
    out_json.write_text(
        json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    return text
