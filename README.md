# 🚀 AI Study Buddy Pro

**Your Intelligent Academic Assistant powered by Google Gemini 1.5 Flash.**

![Status](https://img.shields.io/badge/Status-Live-green) [![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/ksgaik/AI-Study-Budy) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1iKTo6CFA7YTiOneWoZABI6bUaaFgHizM?usp=sharing)

## 📖 Overview

**AI Study Buddy Pro** is an advanced web application designed to revolutionize how students revise and interact with their study materials. By leveraging the power of **Large Language Models (LLMs)**, specifically **Google Gemini 1.5 Flash**, this tool transforms static documents into interactive learning experiences.

Instead of passively reading through hundreds of pages of PDF notes, you can simply upload your files and ask the AI to **summarize them, explain complex concepts, generate quizzes, or create flashcards** instantly.

## ✨ Key Features

* **📄 Multi-Format Support:** Upload multiple **PDFs**, **Word Documents (.docx)**, and **Text files (.txt)** simultaneously. The system intelligently stitches them together for analysis.
* **🧠 Four Intelligent Modes:**
    * **Summarize Notes:** Condenses lengthy content into crisp, bulleted summaries.
    * **Explain Concepts:** Breaks down jargon and complex topics into simple, easy-to-understand language.
    * **Generate Quiz:** Automatically creates 5-question multiple-choice quizzes with answers for self-assessment.
    * **Create Flashcards:** Generates Q&A pairs perfect for active recall and memorization.
* **⚡ Real-Time Streaming:** Experience zero latency with streaming responses that type out the answer as the AI "thinks."
* **🎨 Pro UI Design:** A polished "Glassmorphism" interface with a **High-Contrast Onyx & Indigo Theme**, designed for maximum readability and focus.
* **📋 One-Click Copy:** Dedicated copy button to instantly grab the generated text for your notes (Notion, Obsidian, etc.).
* **🗑️ Session Management:** Easily clear inputs and outputs with a single click to start a fresh study session.

## 🛠️ Tech Stack

* **Frontend:** [Gradio](https://www.gradio.app/) (Python-based web UI framework)
* **AI Model:** [Google Gemini 1.5 Flash](https://ai.google.dev/) (via `google-generativeai`)
* **Document Processing:**
    * `pypdf`: For extracting text from PDF files.
    * `python-docx`: For parsing Microsoft Word documents.
* **Deployment:** Hugging Face Spaces (Cloud Hosting)

## 🚀 How to Run Locally

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/YOUR_GITHUB_USERNAME/AI-Study-Buddy-Pro.git](https://github.com/YOUR_GITHUB_USERNAME/AI-Study-Buddy-Pro.git)
    cd AI-Study-Buddy-Pro
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set Up API Key**
    You need a Google Gemini API Key. Get one here: [Google AI Studio](https://aistudio.google.com/).
    
    * **Option A (Environment Variable):**
        Create a `.env` file or export it in your terminal:
        ```bash
        export GEMINI_API_KEY="your_actual_api_key_here"
        ```
    * **Option B (Direct Input):**
        (Not recommended for sharing) You can temporarily hardcode it in `app.py` for testing.

4.  **Run the App**
    ```bash
    python app.py
    ```
    The app will launch at `http://127.0.0.1:7860`.

## ☁️ Deployment on Hugging Face

1.  Create a new **Space** on Hugging Face.
2.  Select **Gradio** as the SDK.
3.  Upload `app.py` and `requirements.txt`.
4.  Go to **Settings** > **Variables and Secrets**.
5.  Add a new Secret:
    * **Name:** `GEMINI_API_KEY`
    * **Value:** `Your_Google_API_Key`
6.  The app will build and go live automatically!

## 📸 Screenshots

| **UI Interface** |
| :---: |
| ![image alt](https://github.com/KMG1610/AI-StudyBuddy/blob/main/UI-SS.png?raw=true) |

| **Notes Explanation** |
| :---: |
| ![image alt](https://github.com/KMG1610/AI-StudyBuddy/blob/main/EXPLANATION-SS.png?raw=true) |

| **Notes Summarization** |
| :---: |
| ![image alt](image_url) |

| **Quiz Generation** |
| :---: |
| ![image alt](image_url) |

| **Flashcard Generation** |
| :---: |
| ![image alt](image_url) |

## 🔮 Future Roadmap

* [ ] **RAG Integration:** Support for querying massive textbooks (500+ pages) without token limits.
* [ ] **Audio Mode:** Text-to-Speech for listening to summaries on the go.
* [ ] **Visual Aids:** Auto-generate diagrams and flowcharts for concepts.
* [ ] **User Accounts:** Save your quizzes and study history.

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request if you have ideas for new features.

## 📜 License

This project is open-source and available under the **MIT License**.

---

<p align="center">
  Made with ❤️ by [Your Name]
</p>
