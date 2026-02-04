import json
import whisper

def transcribe(audio_path: str, out_txt: str, out_json: str, model_name="small", language="es"):
    model = whisper.load_model(model_name)
    result = model.transcribe(audio_path, language=language)
    text = result["text"].strip()

    with open(out_txt, "w", encoding="utf-8") as f:
        f.write(text + "\n")

    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(result.get("segments", []), f, ensure_ascii=False, indent=2)

    return text
