from __future__ import annotations
import shutil
import subprocess
from pathlib import Path

class DependencyError(RuntimeError):
    pass

def _require(cmd: str) -> None:
    if shutil.which(cmd) is None:
        raise DependencyError(f"No encuentro '{cmd}' en PATH. Instálalo y prueba de nuevo.")

def download_tiktok(
    url: str,
    out_dir: str | Path,
    filename_template: str = "%(id)s.%(ext)s",
    cookies_from_browser: str | None = None,
    cookies_file: str | None = None,
) -> Path:
    _require("yt-dlp")

    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    out_tpl = str(out_dir / filename_template)

    cmd = ["yt-dlp", "--no-playlist", "-o", out_tpl, "--print", "after_move:filepath"]
    if cookies_from_browser:
        cmd += ["--cookies-from-browser", cookies_from_browser]
    if cookies_file:
        cmd += ["--cookies", cookies_file]
    cmd += [url]

    try:
        res = subprocess.run(cmd, check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Falló yt-dlp.\nSTDOUT:\n{e.stdout}\n\nSTDERR:\n{e.stderr}") from e

    #lines = [l.strip() for l in res.stdout.splitlines() if l.strip()]
    lines = [line.strip() for line in res.stdout.splitlines() if line.strip()]

    if not lines:
        raise RuntimeError("yt-dlp no devolvió filepath. Posible bloqueo/cookies.")

    p = Path(lines[-1])
    if not p.is_absolute():
        p = (out_dir / p).resolve()

    if not p.exists():
        candidates = sorted(out_dir.glob("*"), key=lambda x: x.stat().st_mtime, reverse=True)
        if candidates:
            return candidates[0]
        raise FileNotFoundError("No encontré el archivo descargado en el directorio de salida.")

    return p
