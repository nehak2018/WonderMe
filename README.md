# StoryBuddy ⭐

StoryBuddy is a multi-agent AI storytelling application built using Google's Agent Development Kit (ADK). Designed for children, StoryBuddy generates engaging, age-appropriate stories and interactive character conversations while ensuring content safety through a dedicated safety review agent.

The application demonstrates a complete multi-agent architecture where specialized agents collaborate to create magical storytelling experiences for kids.

## Features

* 📚 Generate personalized children's stories based on age, character, and theme.
* 🛡️ Multi-agent safety pipeline to ensure child-friendly content.
* 🗣️ Text-to-Speech narration for immersive storytelling.
* 🤖 Built with Google Agent Development Kit (ADK).
* 🎭 Extensible architecture for future conversational character mode.
* 🎨 Simple Streamlit-based user interface.

## Capstone Project Concepts Demonstrated
This project demonstrates the following concepts from the **Google & Kaggle 5-Day AI Agents Intensive Course**:

* ✅ **Multi-Agent System (ADK)**
  * Implements a sequential multi-agent architecture using Google Agent Development Kit (ADK).Specialized agents collaborate to generate and review stories.
* ✅ **Agent Skills**
  * Reusable skills are implemented for story generation and child safety review.
  * Skills are encapsulated within individual agent modules.
* ✅ **Security Features**
  * A dedicated Safety Agent reviews all generated content to ensure stories remain age-appropriate, safe, and child-friendly.
* ✅ **Deployability**
  * The application is deployed as a Streamlit application and can be easily run locally or deployed to cloud environments.
* ⚙️ **Antigravity-Assisted Development**
  * Antigravity was used during development for rapid prototyping, code generation, and documentation assistance.


## Multi-Agent Architecture

StoryBuddy uses a sequential multi-agent pipeline:

**User → Story Agent → Safety Agent → Final Story**

* **Story Agent**: Generates creative, age-appropriate stories.
* **Safety Agent**: Reviews and sanitizes content for child safety.
* **Root Agent**: Orchestrates agent interactions using ADK.

## Agent Skills

* Story generation skills
* Child safety review skills
* Age-adaptive storytelling prompts

## Tech Stack

* Google Agent Development Kit (ADK)
* Gemini Models
* Streamlit
* Python
* gTTS (Google Text-to-Speech)

## Project Motivation

StoryBuddy was developed as a capstone project for the **Google & Kaggle 5-Day AI Agents Intensive Course**, demonstrating key agentic AI concepts including multi-agent orchestration, agent skills, safety mechanisms, and deployable AI applications.

## Disclaimer

StoryBuddy is intended for educational and demonstration purposes.
