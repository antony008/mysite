from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    title = 'A title that you like'
    subtitle = 'A subtitle that you like'
    return render_template('hello.html', title=title, subtitle=subtitle)