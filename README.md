# 🎓 StudentSmart AI

StudentSmart AI is an AI-powered educational analytics assistant that converts natural language questions into SQL queries using Google Gemini AI and SQLite.

The application helps students, educators, and analysts explore student performance trends, study habits, and academic factors through an interactive Streamlit dashboard.

---

## 🚀 Features

* 🧠 Natural Language to SQL using Gemini AI
* 📊 Student performance analytics
* 🗄️ SQLite database integration
* 💬 Interactive Streamlit interface
* 📈 Educational data insights
* 🔍 Predefined + custom analytical questions
* ⚡ Real-time SQL query generation

---

## 📂 Project Structure

```bash
StudentSmart-AI/
│
├── app.py                  # Streamlit frontend
├── agent_ai.py             # Gemini AI + SQL generation logic
├── setup_database.py       # CSV → SQLite database setup
├── student_performance.db  # SQLite database
├── requirements.txt
└── README.md
```

---

## 📊 Dataset Information

The dataset includes multiple student-related academic and lifestyle factors such as:

* Study Hours
* Attendance
* Sleep Hours
* Previous Scores
* Motivation Level
* Tutoring Sessions
* Internet Access
* Teacher Quality
* Family Income
* Extracurricular Activities
* Final Exam Scores

---

## 💡 Example Questions

* What is the average exam score for each level of parental involvement?
* How does sleep duration affect exam performance?
* Do students with extracurricular activities score higher?
* Does tutoring improve final exam scores?
* How does previous academic performance impact final scores?
* How much should I study per week if my previous score was 88 and I want 95 in final exam?

---

## ⚙️ Tech Stack

* Python
* Streamlit
* SQLite
* Pandas
* Google Gemini AI
* Prompt Engineering

---

## 🧠 How It Works

1. User asks a question in natural language.
2. Gemini AI converts the question into a valid SQLite query.
3. SQLite executes the query on the student database.
4. Results are displayed interactively in Streamlit.

---

## 📸 Demo Preview

<p align="center">
  <img src="YOUR_SCREENSHOT_LINK_HERE" alt="StudentSmart AI Demo" width="100%">
</p>

---

## 🛠️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/StudentSmart-AI.git
cd StudentSmart-AI
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Configure Gemini API Key

Replace:

```python
genai.configure(api_key="YOUR_API_KEY")
```

with your own Gemini API key.

---

## ▶️ Run Database Setup

```bash
python setup_database.py
```

---

## ▶️ Launch Streamlit App

```bash
streamlit run app.py
```

---

## 📌 Future Improvements

* 📈 Advanced visualizations
* 🎯 Personalized study recommendations
* 🧮 Predictive performance analysis
* ☁️ Cloud deployment
* 🔐 Secure API key management

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

---

## 📜 Preview

<img width="838" height="794" alt="image" src="https://github.com/user-attachments/assets/cd5bfe78-ccb7-4542-8ad7-c5228bc03a7f" />

