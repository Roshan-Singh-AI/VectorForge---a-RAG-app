# VectorForge 🧩

A **Streamlit-based conversational AI app** powered by `llama-3.3-70b-versatile`.  
This project demonstrates a simple chat interface where user inputs are processed by an LLM, and responses are streamed back in real time.

---

## 🌐 Live Demo

You can try the deployed app here:  
👉 [VectorForge on Streamlit](https://vectorforge.streamlit.app/)

---
## 🚀 Features

- **Streamlit UI** – Clean and interactive chat interface.
- **Chat Memory** – Maintains conversation history across user and assistant turns.
- **Streaming Responses** – AI responses are streamed in real time for a smoother experience.
- **Custom Model Integration** – Uses `llama-3.3-70b-versatile` (configurable from `src/config`).

---

## 📂 Project Structure

```
.
├── app.py               # Main Streamlit app (entry point)
├── src/
│   └── config.py        # LLM model configuration (groq_llm_model)
└── README.md            # Project documentation
```

---

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Roshan-Singh-AI/VectorForge---a-RAG-app/
   cd vectorforge
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On macOS/Linux
   venv\Scripts\activate      # On Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure your LLM**  
   Create an .env file with the following values - 
   ```
   groq_api_key = "<groq_api_key>"
   groq_llama_model = "llama-3.3-70b-versatile"
   ```

---

## ▶️ Running the App

Start the Streamlit server:

```bash
streamlit run app.py
```

The app will be available at:  
👉 [http://localhost:8501](http://localhost:8501)

---

## 🧑‍💻 Usage

- Type your prompt into the chat input field.
- The assistant will generate a **streamed response** in real time.
- Conversation history is maintained across turns.

---

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/) – Web app framework
- [Python](https://www.python.org/) – Core language
- `groq_llm_model` – Custom LLM integration (replaceable with any API/model)

---

## 🤝 Contributing

Pull requests are welcome!  
For major changes, please open an issue first to discuss what you would like to change.

---

## 📜 License

This project is licensed under the MIT License. See `LICENSE` for details.
