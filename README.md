# 🌟 WonderMe: AI Storytelling Companion for Children

> **WonderMe** is an AI-powered storytelling application built using **Google's Agent Development Kit (ADK)** and a **multi-agent architecture** to generate personalized, age-appropriate stories for children. The application combines multiple AI agents to create engaging stories, AI-generated narration, and story transcripts, providing a fun, interactive, and educational storytelling experience.

> 🚀 Developed as part of the **Google AI Agents Intensive – Vibe Coding Capstone**.

---

## ✨ Features

- 📖 Personalized story generation
- 🤖 Multi-agent AI workflow using Google ADK
- 🎭 Multiple fun story characters
- 👧 Age-appropriate storytelling
- 🔊 AI-generated audio narration
- 📝 Story transcripts
- 🎨 Interactive Streamlit interface
- 📚 Educational storytelling experience

---

## 🤖 Multi-Agent Workflow

WonderMe uses specialized AI agents that collaborate to create a complete storytelling experience.

| Agent | Responsibility |
|--------|----------------|
| Story Coordinator | Manages the overall storytelling workflow |
| Story Generator | Generates personalized stories |
| Safety Agent | Ensures stories are child-friendly and age appropriate |


---

## 🛠️ Technology Stack

- Python
- Streamlit
- Google Agent Development Kit (ADK)
- Google Gemini
- Google AI Studio
- Text-to-Speech
- CSS

---

## 📁 Project Structure

```text
WonderMe/
│
├── agents/
├── assets/
├── utils/
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/nehak2018/WonderMe.git

cd WonderMe
```

### Create a virtual environment

Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure API Key

Create a `.env` file.

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

> **Important:** Never commit your `.env` file or API keys to GitHub.

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will launch automatically in your default web browser.

---

## 🎮 How to Use

1. Select your favorite story character.
2. Choose the child's age.
3. Enter a story theme or prompt.
4. Generate a personalized story.
5. Listen to the AI narration.
6. Read the transcript.

---

## 📸 Screenshots

Add screenshots of:

- Home page
- Character selection
- Story generation
- Audio player
- Transcript

---

## 🎥 Demo Video

Watch the WonderMe demo on YouTube:

**https://youtu.be/MUX7SzQSz3w?si=1Q8jbO3SFoB5Y1u9**

---

## 🌱 Future Enhancements

- Additional story characters
- Multiple language support
- Interactive story choices
- Voice customization
- Story illustrations
- Parent dashboard
- Reading progress
- Educational quizzes

---

## 🔒 Security

WonderMe follows security best practices:

- API keys stored using environment variables
- `.env` excluded from Git version control
- No secrets committed to the repository

---

## 🤝 Contributing

Contributions, suggestions, and feature requests are welcome.

Feel free to fork the repository and submit a pull request.

---

## 🙏 Acknowledgements

- Google AI
- Google Agent Development Kit (ADK)
- Google Gemini
- Streamlit
- Kaggle
- Google AI Agents Intensive – Vibe Coding Capstone

---

## ⭐ Support

If you enjoyed this project, please consider giving it a ⭐ on GitHub!

Your support helps others discover WonderMe and encourages future development.