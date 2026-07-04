import streamlit as st


def render_header() -> None:
    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown('<div class="logo">WonderMe ⭐</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="subtitle">Create wonderful stories with your AI storytelling friend.</div>',
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="mode-pill">
                <div class="mode-active">Full Story Mode</div>
                <div class="mode-inactive">Talk With Character Mode</div>
            </div>
            """,
            unsafe_allow_html=True,
        )