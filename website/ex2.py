import sqlite3  
conn = sqlite3.connect('my_website.db')

def insert_message(conn, name, title, desc, img):
  c = conn.cursor()
  sql = """
    INSERT INTO messages (name, title, desc, img)
    VALUES (?, ?, ?, ?)
  """
  c.execute(sql, (name, title, desc, img))
  #c.execute(sql, ('Jimmy', 'I am Bob', '/static/img/avatars/a1.png'))
  #c.execute(sql, ('Anthony', 'Hi, I am Anthony', '/static/img/avatars/a2.jpeg'))
  #c.execute(sql, ('Joshua', 'Hello', '/static/img/avatars/a3.jpeg'))

  conn.commit()
  #conn.close()

#insert_message(conn, "Antony",'省水',' 每天用洗米水澆花就能省很多水喔','https://i0.wp.com/07imgmini.eastday.com/mobile/20190115/20190115084944_49940c658d2afa799cec0a94ff980782_1.jpeg?zoom=2.625&w&ssl=1')
#insert_message(conn, "Antony", '省電', '隨手關燈，但如果你只要出房間3分鐘就不用了', 'https://cc.tvbs.com.tw/img/upload/2020/01/06/20200106154643-b7bc92bf.jpg')
#insert_message(conn, 'Antony', '環保袋', '每天省一個塑膠袋就可以拯救很多魚', 'https://www.jinbadge.com/images/2018/06/11/non-woven-bag-%20(10).jpg')
#insert_message(conn, 'Antony', '回收紙', '回收5000張紙就能拯救0.3棵樹', 'https://cimg.cnyes.cool/prod/news/4194784/l/dda4eb1212491fd2f9729b54abacf4f6.jpg')



def insert_comment(conn, pid, name, com):
  c = conn.cursor()
  sql = """
    INSERT INTO comments (pid, name, com)
    VALUES (?,?,?)
  """
  c.execute(sql, (pid, name, com))
  conn.commit()

#insert_comment(conn, {'Tom', '這個方法不錯😃😃😃'}, {'Antony', '這個方法不錯'})  
#insert_comment(conn, {'Jimmy', '很棒很棒o(*^＠^*)o'})
