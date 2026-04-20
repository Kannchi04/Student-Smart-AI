# app.py

import streamlit as st
from ai_agent import get_schema, get_sql_query, run_query
import os

DB_PATH = "student_performance.db"

st.set_page_config(page_title="StudentSmart AI", layout="centered")

# 💡 App Title
st.markdown("<h1 style='text-align: center; color:#2E86C1;'>🎓 StudentSmart AI</h1>", unsafe_allow_html=True)

# 🛡️ Check if database exists
if not os.path.exists(DB_PATH):
    st.error("❌ Database file not found. Please ensure 'student_performance.db' is in the app folder.")
    st.stop()

# 📋 Get schema once
schema = get_schema(DB_PATH)

# 🎯 Predefined questions
predefined_questions = [
    "What is the average exam score for each level of parental involvement?",
    "How does number of sleep hours affect final exam score?",
    "Do students with extracurricular activities score higher?",
    "How does previous score relate to final exam score?",
    "Does gender affect average exam performance?",
    "What is the impact of tutoring sessions on exam score?",
    "How much should I study per week if my previous score was 88 and I want 95 in final exam?"
]

st.subheader("💬 Ask a question about student performance")

# 🌟 Dropdown or custom question
question_type = st.selectbox("Choose from examples or write your own:", ["Choose from dropdown", "Write your own"])

if question_type == "Choose from dropdown":
    selected_question = st.selectbox("📌 Example Questions", predefined_questions)
    user_question = selected_question
else:
    user_question = st.text_input("📝 Your Custom Question")

# 🔍 Generate & Run
if user_question:
    if st.button("🔍 Analyze"):
        with st.spinner("Thinking... Generating query..."):
            sql = get_sql_query(user_question, schema)
            result = run_query(DB_PATH, sql)

        # 🧾 Display SQL query
        st.subheader("🧾 SQL Query")
        st.code(sql, language="sql")

        # 📊 Display Results
        st.subheader("📊 Result")
        if result:
            if isinstance(result[0], str) and result[0].startswith("❌"):
                st.error(result[0])
            else:
                st.dataframe(result)
        else:
            st.warning("No results found for this query.")
