# tiktok-to-text

Pipeline para:
1) descargar TikTok (si se puede),
2) extraer audio,
3) transcribir con Whisper,
4) guardar TXT/JSON/SRT.

## Estructura
- notebooks/: pruebas en Colab/Jupyter
- src/: scripts (download/audio/transcribe)
- outputs/: resultados (NO subir mp4/wav)

## Setup
- Instalar ffmpeg
- `pip install -r requirements.txt`
