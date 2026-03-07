# 🤖 Conversational Chatbot

A conversational AI chatbot built with Django and powered by Meta's **LLaMA 3.3 70B** model via the Groq API. Supports real-time, context-aware conversations through a clean web interface.

---

## 🚀 Features

- 💬 Real-time conversational AI using LLaMA 3.3-70B-Versatile
- ⚡ Ultra-fast inference powered by Groq
- 🧠 Context-aware chat using LangChain
- 🗄️ Persistent chat history stored in MySQL
- 🌐 Simple and responsive web interface (HTML/CSS)

---

## 🛠️ Tech Stack

| Layer         | Technology                        |
|---------------|-----------------------------------|
| Backend       | Python, Django                    |
| Frontend      | HTML, CSS                         |
| Database      | MySQL                             |
| AI Model      | LLaMA 3.3-70B-Versatile (via Groq)|
| LLM Framework | LangChain                         |

---

## 📋 Prerequisites

Make sure you have the following installed:

- Python 3.9+
- MySQL Server
- A [Groq API Key](https://console.groq.com/)

---

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Abhisek8895/Convorsational_Chatbot
   cd Conversational_Chatbot
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate        # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**

   Create a `.env` file in the root directory:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   DB_NAME=your_database_name
   USER=your_mysql_username
   PASSWORD=your_mysql_password
   ```

5. **Set up the MySQL database**
   ```sql
   CREATE DATABASE chatbot_db;
   ```

6. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. **Start the development server**
   ```bash
   python manage.py runserver
   ```

8. **Open your browser** and navigate to `http://127.0.0.1:8000`

---

## 📁 Project Structure

```
conversational-chatbot/
├── accounts/               # User authentication & management
├── chat/                   # Core chat app (views, models, logic)
├── conversational_chatbot/ # Django project settings & main URLs
├── templates/              # HTML templates (frontend)
├── .env                    # Environment variables (not committed)
├── .gitignore
├── manage.py
└── requirements.txt
```

---

## 🔑 Environment Variables

| Variable       | Description                        |
|----------------|------------------------------------|
| `GROQ_API_KEY` | Your Groq API key                  |
| `DB_NAME`      | MySQL database name                |
| `USER`         | MySQL username                     |
| `PASSWORD`     | MySQL password                     |

---

## 📦 Dependencies

Key packages used (see `requirements.txt` for full list):

```
django
langchain-groq
mysqlclient
python-dotenv
```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Acknowledgements

- [Groq](https://groq.com/) for blazing-fast LLM inference
- [Meta AI](https://ai.meta.com/) for the LLaMA model
- [LangChain](https://www.langchain.com/) for the LLM framework
