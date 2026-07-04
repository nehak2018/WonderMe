import streamlit as st


def render_settings():
    with st.container(border=True):
        st.markdown(
            '<div class="card-title">⚙️ Choose Your Settings</div>',
            unsafe_allow_html=True,
        )

        age = st.selectbox(
            "Kid's Age",
            ["3 - 5 years", "6 - 8 years", "9 - 12 years"],
            index=1,
        )

        # character = st.selectbox(
        #     "Choose a Character",
        #     ["🐉 Luna the Dragon", "🤖 Milo the Robot", "🐰 Bella the Bunny", "Hippo Elephant", "Unico Unicorn", "Tini Ant", "Octo Octopus", "Duckling"],
        #     index=0,
        # )

        character = st.selectbox(
           "Choose a Character",
            [
                "🐉 Luna the Dragon",
                "🤖 Milo the Robot",
                "🐰 Bella the Bunny",
                "🐘 Ellie the Elephant",
                "🦄 Unico the Unicorn",
                "🐜 Tini the Ant",
                "🐙 Ollie the Octopus",
                "🦆 Ducky the Duck"
            ],
            index=0,
        )


        theme = st.text_input("Story Theme", "Kindness and helping others")

        generate = st.button(
            "✨ Generate Story",
            type="primary",
            use_container_width=True,
        )

        clear = st.button("🗑️ Clear", use_container_width=True)
        about = st.button("ⓘ About", use_container_width=True)

    return age, character, theme, generate, clear, about