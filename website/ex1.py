import sqlite3  
conn = sqlite3.connect('my_website.db')

def create_messages_table(conn):
  c = conn.cursor()
  sql = """
    CREATE TABLE messages (
      id INTEGER PRIMARY KEY,
      name TEXT NOT NULL,
      title TEXT NOT NULL,
      desc TEXT NOT NULL,
      img TEXT 
    )
  """
  c.execute(sql)

def create_comments_table(conn):
  c = conn.cursor()
  sql = """
    CREATE TABLE comments (
      id INTEGER PRIMARY KEY,
      pid INTEGER NOT NULL,
      name TEXT NOT NULL,
      com TEXT NOT NULL

    )
  """
  c.execute(sql)

  conn.commit()
  conn.close()


#create_messages_table(conn)
create_comments_table(conn)