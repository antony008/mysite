import sqlite3  
conn = sqlite3.connect('student.db')

c = conn.cursor()
sql = """
  CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    intro TEXT,
    avatar text 
  )
"""
c.execute(sql)

conn.commit()
conn.close()