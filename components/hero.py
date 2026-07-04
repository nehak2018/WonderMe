import streamlit as st


def render_hero() -> None:
    st.markdown(
        """
        <div class="main-card">
            <div class="hero-card">
                <div class="speech">
                    <b>🔊 Hi there!</b><br><br>
                    I'm your storytelling friend.<br>
                    Let's create something magical together!
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )