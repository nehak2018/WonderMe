import base64
import streamlit as st

from utils.media_utils import make_audio


def render_audio_on_image(story: str) -> None:

    audio_output = make_audio(story)

    if isinstance(audio_output, str):
        with open(audio_output, "rb") as f:
            audio_bytes = f.read()

    elif hasattr(audio_output, "read"):
        audio_bytes = audio_output.read()

    else:
        audio_bytes = audio_output

    audio_b64 = base64.b64encode(audio_bytes).decode("utf-8")

    st.markdown(
        f"""
        <div style="
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            background: rgba(255, 255, 255, 0.92);
            backdrop-filter: blur(6px);
            padding: 10px 16px;
            border-radius: 0 0 16px 16px;
            ">
            <p style="margin: 0 0 6px 0;">
                🔊 <strong>Listen</strong>
            </p>

            <audio controls style="width:100%;">
                <source src="data:audio/mpeg;base64,{audio_b64}"
                        type="audio/mpeg">
            </audio>
        </div>
        """,
        unsafe_allow_html=True,
    )