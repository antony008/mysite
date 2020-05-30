from flask import Flask, session, render_template, request, redirect, g

app = Flask(__name__)

app.secret_key = b'should be a secret'

users_db = {
    'Antony': {
        'uid': 'Antony',
        'password': 'aaaaa',
        'name': 'Antony Hsieh',
        'email': 'antony@gmail.com'
    }
}


def get_user():
  user_id = session.get('user_id')
  if user_id:
    g.user = users_db.get(user_id)
  else:
    g.user = { 'uid': None, 'name': 'Guest' }


@app.route('/')
def index():
    get_user()
    return render_template('home.html', user=g.user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        uid = request.form.get('uid')
        password = request.form.get('password')
        if not uid or not password:
            return 'invalid input'
        user = users_db.get(uid)
        if not user:
            return 'user not exist'
        if user.get('password') != password:
            return 'password error'

        session['user_id'] = uid
        return redirect('/')
        
    return render_template('login.html')

@app.route('/logout')
def logout():
    session['user_id'] = None
    return redirect('/')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        uid = request.form.get('uid')
        password = request.form.get('password')
        email = request.form.get('email')
        name = request.form.get('name')
        if not uid or not password or not name or not email:
            return 'invalid input'
        user = users_db.get(uid) 
        if user:
            return 'user exeists'
        
        users_db[uid] = {'uid': uid, 'password': password, 'email': email, 'name': name}
        session['user_id'] = uid
        return redirect('/')
        
    return render_template('signup.html')

@app.route('/profile/<sid>')
def profile(sid):
    user = users_db[sid]
    return render_template('profile.html', user=user)