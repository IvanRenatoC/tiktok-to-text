import subprocess

def extract_audio(video_path: str, audio_path: str) -> str:
    cmd = ["ffmpeg", "-y", "-i", video_path, "-ac", "1", "-ar", "16000", audio_path]
    subprocess.run(cmd, check=True)
    return audio_path
