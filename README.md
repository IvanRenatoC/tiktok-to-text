# 🎬➡️📝 tiktok-to-text

Pipeline en **Python + Google Colab** para convertir un **link de TikTok** a **texto** usando **Whisper**.

---

## ✅ ¿Qué hace este proyecto?

A partir de un link como:

- 🔗 `https://vt.tiktok.com/...`

El flujo hace:

1. 📥 **Descarga el video** (con `yt-dlp`)
2. 🎧 **Extrae el audio** a `.wav` mono 16kHz (con `ffmpeg`)
3. 🧠 **Transcribe a texto** (con `openai-whisper`)
4. 💾 **Guarda outputs**:
   - `transcripcion.txt`
   - `segments.json` (con timestamps por segmento)
   - (opcional) `captions.srt`

---

## 🧱 Estructura del repo

---

## ✅ Requirements / Instalación

### 1) Dependencias del sistema
Este proyecto requiere **ffmpeg**.

- En Google Colab:
  ```bash
  apt-get -y update
  apt-get -y install ffmpeg

### Bonus: revisa tu `requirements.txt`

Asegúrate que tenga esto (mínimo):

```txt
yt-dlp
openai-whisper
ffmpeg-python

