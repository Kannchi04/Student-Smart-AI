import os
import sqlite3
import google.generativeai as genai

# ✅ Configure Gemini API
genai.configure(api_key="AIzaSyBkVqMJSQeJJaJnkSYQWfMdfFGSGQDT5SI")  # 🔁 Replace with your Gemini API key

def get_schema(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    schema = []
    for (table_name,) in cursor.execute("SELECT name FROM sqlite_master WHERE type='table';"):
        schema.append(f"Table: {table_name}")
        for column in cursor.execute(f"PRAGMA table_info({table_name});"):
            schema.append(f"  {column[1]} ({column[2]})")
        schema.append("")
    conn.close()
    return "\n".join(schema)

def get_sql_query(question, schema):
    prompt = f"""
You are an expert data analyst.

You are working with a SQLite database containing a table named `student_performance` with the following columns:

- Hours_Studied_per_week (number of study hours per week)
- Hours_Studied_per_day (number of study hours per day)
- Attendance (percentage of attendance)
- Parental_Involvement (Low,how much should i study per week if my previous score was 88 and want 95 in final exam Medium, High)
- Access_to_Resources (Low, Medium, High)
- Extracurricular_Activities (Yes, No)
- Sleep_Hours (average hours of sleep per night)
- Previous_Scores (score in past exams)
- Motivation_Level (Low, Medium, High)
- Internet_Access (Yes, No)
- Tutoring_Sessions (number per month)
- Family_Income (Low, Medium, High)
- Teacher_Quality (Low, Medium, High)
- School_Type (Public, Private)
- Peer_Influence (Positive, Neutral, Negative)
- Physical_Activity (hours per week)
- Learning_Disabilities (Yes, No)
- Parental_Education_Level (High School, College, Postgraduate)
- Distance_from_Home (Near, Moderate, Far)
- Gender (Male, Female)
- Exam_Score (final exam score)

Your job is to generate ONLY a valid SQLite query (no explanation) that answers the question below.

⚠️ Constraints:
- Use only SQLite-supported functions (AVG, COUNT, SUM, CASE, etc.)
- ❌ Do not use unsupported functions (like CORR, STDDEV)
- ❌ No explanations, markdown, or phrases like 'Sure', 'Okay', or 'ite'
- ✅ If analyzing numeric impact, use basic math or CASE/aggregate logic
- ✅ For categorical comparison, use GROUP BY with AVG(Exam_Score)

Question:
{question}
"""

    model = genai.GenerativeModel("models/gemini-2.0-flash")
    response = model.generate_content(prompt)
    sql_query = response.text.strip()

    # Clean output
    if "```" in sql_query:
        sql_query = sql_query.split("```")[-2].strip()
    if sql_query.lower().startswith("sql"):
        sql_query = sql_query[3:].strip()
    if sql_query.lower().startswith(("ite", "okay", "sure")):
        sql_query = "\n".join([line for line in sql_query.splitlines() if not line.lower().startswith(("ite", "okay", "sure"))])

    return sql_query

def run_query(db_path, sql):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        rows = cursor.fetchall()
        return rows
    except Exception as e:
        return [f"❌ Error: {str(e)}"]
    finally:
        conn.close()

def main():
    db_path = "student_performance.db"
    if not os.path.exists(db_path):
        print("❌ Database file not found.")
        return

    print("✅ AI Agent is ready to analyze student performance!")
    print("💡 Type 'exit' to quit.\n")

    schema = get_schema(db_path)

    while True:
        question = input("❓ Your question: ").strip()
        if question.lower() == "exit":
            break

        sql = get_sql_query(question, schema)
        print("\n📜 SQL Generated:\n", sql)

        result = run_query(db_path, sql)
        print("\n📊 Result:")
        if result:
            for row in result:
                print(" ", row)
        else:
            print(" No data returned.")
        print("-" * 50)

if __name__ == "__main__":
    main()
