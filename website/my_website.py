from flask import Flask, render_template
from flask import request, redirect

app = Flask(__name__)

messages = {
  "1": { "name": "Antony", 'title': '省水', 'desc':' 每天用洗米水澆花就能省很多水喔',  'img':'https://i0.wp.com/07imgmini.eastday.com/mobile/20190115/20190115084944_49940c658d2afa799cec0a94ff980782_1.jpeg?zoom=2.625&w&ssl=1'},
  "2": { "name": "Antony", 'title': '省電', 'desc': '隨手關燈，但如果你只要出房間3分鐘就不用了', 'img': 'https://cc.tvbs.com.tw/img/upload/2020/01/06/20200106154643-b7bc92bf.jpg'}
}

comments = {
  "1":[{'name': 'Tom', 'com':'這個方法不錯😃😃😃'}, {'name': 'Antony', 'com':'這個方法不錯'}],
  "2":[{'name': 'Jimmy', 'com':'很棒很棒o(*^＠^*)o'}],
}



@app.route("/")
def my_website():
    title = '環保大家一起來'
    #print(message)
    return render_template('homepage.html', title=title, messages=messages)


@app.route("/message/<sid>")
def message(sid):
    print(sid)
    message=messages[sid]
    return render_template('message.html', message=message)

   
@app.route("/comment/<sid>")
def comment(sid):
    comment = comments[sid]  
    return render_template('comment.html', comment=comment, sid=sid)   
   
  
@app.route("/leave/message", methods = ['GET', 'POST'])
def leave_message():
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
        n = len(messages) + 1
        
        if len(errors) == 0:
          messages[str(n)] = {'name': name, "title": title, "img": img, "desc": desc}

        return redirect('/')   
    return render_template("leave_message.html", errors=errors, messages=messages)



@app.route('/leave/comment/<sid>', methods = ['GET', 'POST'])
def leave_comment(sid):
    errors = {}
    comment_list = comments[sid]
    if request.method == 'POST':
        name = request.form['name']
        cmt = request.form['comment']
        if not name:
            errors['name'] = 'name should not be empty'
        if not comment:
            errors['comment'] = 'comment should not be empty'     
        if len(errors) == 0:
            comment_list.append({'name': name, 'com' : cmt})
            return redirect('/comment/' + sid)

    return render_template('leave_comment.html', errors=errors, sid=sid)

