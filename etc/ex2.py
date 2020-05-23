import sqlite3  
conn = sqlite3.connect('student.db')

c = conn.cursor()
sql = """
  INSERT INTO students (name, intro, avatar)
  VALUES (?, ?, ?)
"""
c.execute(sql, ('Jimmy', 'I am Bob', '/static/img/avatars/a1.png'))
c.execute(sql, ('Anthony', 'Hi, I am Anthony', '/static/img/avatars/a2.jpeg'))
c.execute(sql, ('Joshua', 'Hello', '/static/img/avatars/a3.jpeg'))

conn.commit()
conn.close()