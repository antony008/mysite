import sqlite3  
conn = sqlite3.connect('my_website.db')

def select_message(conn):
      c = conn.cursor()
      sql = """
      SELECT id, name, title, desc, img 
            FROM messages
      """
      c.execute(sql)
      return c.fetchall()
      #ps = [f"{id:<5}{name:<10}{intro:<20}{avatar}"
         #   for id, name, intro, avatar in stus]
      #print('\n'.join(ps))
#print(select_message(conn))

def select_comment(conn, pid):
      c = conn.cursor()
      sql = """
      SELECT id, pid, name, com 
            FROM comments WHERE pid = ?
      """
      c.execute(sql, (pid,))
      return c.fetchall()
