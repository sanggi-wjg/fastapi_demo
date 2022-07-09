import os

from gtts import gTTS

from app.core.config import get_config_settings

settings = get_config_settings()


def get_tts_save_path(text: str) -> str:
    return os.path.join(settings.media_dir, f"{text}.mp3")


def create_tts_file(text: str) -> bool:
    save_path = get_tts_save_path(text)
    tts = gTTS(text)
    tts.save(save_path)
    return True
