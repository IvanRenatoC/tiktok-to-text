import os
import subprocess

def download_tiktok(url: str, out_dir: str) -> str:
    os.makedirs(out_dir, exist_ok=True)
    out_tpl = os.path.join(out_dir, "tiktok.%(ext)s")
    cmd = ["yt-dlp", "-o", out_tpl, url]
    subprocess.run(cmd, check=True)
    # devuelve el path "más probable"
    for ext in ("mp4", "webm", "mkv"):
        p = os.path.join(out_dir, f"tiktok.{ext}")
        if os.path.exists(p):
            return p
    raise FileNotFoundError("No se encontró video descargado en el directorio.")
