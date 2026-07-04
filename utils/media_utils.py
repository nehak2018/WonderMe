import base64
import tempfile
from pathlib import Path

from gtts import gTTS


def image_to_base64(path: Path) -> str:
    """
    Convert image file to base64 string.
    """
    return base64.b64encode(path.read_bytes()).decode()


def make_audio(text: str) -> str:
    """
    Generate speech and return temporary mp3 path.
    """
    tts = gTTS(text=text, lang="en")

    tmp = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".mp3"
    )

    tts.save(tmp.name)

    return tmp.name


def make_audio_base64(text: str) -> str:
    """
    Generate speech and return base64 encoded audio.
    """
    audio_path = make_audio(text)

    with open(audio_path, "rb") as f:
        audio_bytes = f.read()

    return base64.b64encode(audio_bytes).decode()