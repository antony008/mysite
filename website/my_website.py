from flask import Flask, render_template
from flask import request, redirect
import sqlite3
from flask import g
import ex3, ex2

DATABASE = 'my_website.db'


app = Flask(__name__)



#comments = {
#  "1":[{'name': 'Tom', 'com':'這個方法不錯😃😃😃'}, {'name': 'Antony', 'com':'這個方法不錯'}],
#  "2":[{'name': 'Jimmy', 'com':'很棒很棒o(*^＠^*)o'}],
#}


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()



@app.route("/")
def my_website():
    title = '環保大家一起來'
    #print(message)
    conn = get_db()
    ms = ex3.select_message(conn)
    messages = {}
    for m in ms:
        id, name, title, desc, img = m
        messages.update({str(id):{'name': name, 'title': title, 'desc': desc, 'img': img}})
    print(messages)
        
    return render_template('homepage.html', title=title, messages=messages)


@app.route("/message/<sid>")  
def message(sid):
    conn = get_db()
    ms = ex3.select_message(conn)
    messages = {}
    for m in ms:
        id, name, title, desc, img = m
        messages.update({str(id):{'name': name, 'title': title, 'desc': desc, 'img': img}})
    mes = messages[sid]    
    
    
    return render_template('message.html', mes=mes)

   
@app.route("/comment/<sid>")
def comment(sid):
    conn = get_db()
    cmts = ex3.select_comment(conn, sid)
    comment = []
    for cm in cmts:
        id, pid, name, com = cm
        comment.append({ 'name': name, 'com': com })
    return render_template('comment.html', comment=comment, sid=sid)   
   
  
@app.route("/leave/message", methods = ['GET', 'POST'])
def leave_message():
    conn = get_db()
    #ms = ex3.select_message(conn)
    #messages = {}
    #for m in ms:
    #    id, name, title, desc, img = m
    #    messages.update({str(id):{'name': name, 'title': title, 'desc': desc, 'img': img}})
    errors = {}
    
    if request.method == 'POST':
        name = request.form['name']
        title = request.form['title']
        img = request.form['img']
        desc = request.form['desc']
        if not img:
            img = 'https://children.moc.gov.tw/resource/calture_article_image/146.png'
        if not name:
            errors['name'] = '匿名一定要填'
        if not title:
            errors['title'] = '標題一定要填'     

        if not desc:
            errors['desc'] = '內容一定要填'
        
        ex2.insert_message(conn, name, title, desc, img)
           
        
        #n = len(messages) + 1
        
        #if len(errors) == 0:
        #  messages[str(n)] = {'name': name, "title": title, "img": img, "desc": desc}

        return redirect('/')   
    return render_template("leave_message.html", errors=errors)



@app.route('/leave/comment/<sid>', methods = ['GET', 'POST'])
def leave_comment(sid):
    errors = {}
    conn = get_db()
    #comment_list = comments[sid]
    if request.method == 'POST':
        name = request.form['name']
        cmt = request.form['comment']
        if not name:
            errors['name'] = 'name should not be empty'
        if not comment:
            errors['comment'] = 'comment should not be empty'     
        #if len(errors) == 0:
        #    comment_list.append({'name': name, 'com' : cmt})
        
        ex2.insert_comment(conn, sid, name, cmt)
  
        return redirect('/comment/' + sid)

    return render_template('leave_comment.html', errors=errors, sid=sid)

