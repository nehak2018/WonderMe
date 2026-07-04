from gtts import gTTS
import tempfile


def text_to_speech(text: str) -> str:
    """Convert text to an mp3 file and return the file path."""
    tts = gTTS(text=text, lang="en")
    audio_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(audio_file.name)
    return audio_file.name
