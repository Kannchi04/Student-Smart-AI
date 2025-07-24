import pandas as pd
import sqlite3

# Load CSV
csv_path = "C:\\study-smart\\StudentPerformanceFactors.csv"  # 🔁 Update path if needed
df = pd.read_csv(csv_path)

# Connect to SQLite and create DB
db_path = "student_performance.db"
conn = sqlite3.connect(db_path)

# Save to SQLite table
df.to_sql("student_performance", conn, if_exists="replace", index=False)

print(f"✅ Database created successfully at: {db_path}")
conn.close()
