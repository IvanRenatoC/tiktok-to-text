from __future__ import annotations
import argparse
from .pipeline import run

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="tiktok-to-text", description="TikTok URL -> transcript (Whisper)")
    p.add_argument("--url", required=True, help="URL del video TikTok")
    p.add_argument("--out", default="outputs", help="Directorio de salida (default: outputs)")
    p.add_argument("--model", default="small", help="Modelo Whisper (tiny/base/small/medium/large)")
    p.add_argument("--lang", default="es", help="Idioma (default: es)")
    p.add_argument("--keep-video", action="store_true", help="No borrar el video descargado")
    p.add_argument("--cookies-from-browser", default=None, help='Ej: "chrome"')
    p.add_argument("--cookies-file", default=None, help="Path a cookies.txt")
    return p

def main(argv=None) -> int:
    args = build_parser().parse_args(argv)

    out = run(
        url=args.url,
        out_dir=args.out,
        model=args.model,
        language=args.lang,
        keep_video=args.keep_video,
        cookies_from_browser=args.cookies_from_browser,
        cookies_file=args.cookies_file,
    )

    print(f"OK ✅\\n- transcript: {out.transcript_txt}\\n- json: {out.transcript_json}\\n- audio: {out.audio_path}")
    return 0
