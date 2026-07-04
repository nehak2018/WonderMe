import streamlit as st


def apply_css(character_img) -> None:
    st.markdown(
        f"""
        <style>
        .block-container {{
            padding-top: 6.9rem !important;
            max-width: 1450px;
        }}

        .stApp {{
            background: #f7f5ff;
        }}

        .logo {{
            font-size: 38px;
            font-weight: 900;
            color: #6c4cff;
            line-height: 1;
        }}

        .subtitle {{
            font-size: 16px;
            color: #444;
            margin-top: 4px;
        }}

        .mode-pill {{
            background: white;
            border-radius: 28px;
            padding: 12px;
            display: flex;
            gap: 4px;
            justify-content: center;
            box-shadow: 0 5px 16px rgba(0,0,0,0.08);
        }}

        .mode-active {{
            background: green;
            color: white;
            padding: 12px 28px;
            border-radius: 20px;
            font-weight: 800;
        }}

        .mode-inactive {{
            color: gray;
            padding: 12px 24px;
            font-weight: 600;
        }}

        .main-card {{
            background: white;
            border-radius: 28px;
            padding: 18px;
            box-shadow: 0 8px 24px rgba(0,0,0,0.08);
        }}

        .hero-card {{
            background-image: url("data:image/png;base64,{character_img}");
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center center;
            background-color: #cbb7ff;
            border-radius: 24px;
            min-height: 500px;
            padding: 28px;
            position: relative;
        }}

        .speech {{
            background: white;
            color: #111;
            padding: 10px 24px;
            border-radius: 22px;
            width: 240px;
            font-size: 18px;
            line-height: 1.2;
            box-shadow: 0 8px 24px rgba(0,0,0,0.12);
        }}

        .story-title {{
            color: #6c4cff;
            font-size: 24px;
            font-weight: 800;
            margin-bottom: 12px;
        }}

        .transcript-card {{
            margin-top: -12px !important;
            background: white;
            color: #111;
            border-radius: 22px;
            padding: 24px 28px;
            box-shadow: 0 6px 20px rgba(0,0,0,0.08);
        }}

        .stButton > button {{
            border-radius: 14px;
            height: 50px;
            font-weight: 800;
        }}

        div[data-testid="stButton"] button[kind="primary"] {{
            background: #6c4cff;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


# background-image: url("data:image/png;base64,{luna_img}");
