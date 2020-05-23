from flask import Flask, render_template
from flask import request, redirect

app = Flask(__name__)

students = {
    's01' : {
        'name': 'Antony',
        'intro': 'smart',
        'avatar': '/static/img/下載.png'
    },
    's02': {
        'name':'Jimmy',
        'intro':'smart smart',
        'avatar':'/static/img/23046491.jpg'
    },
    's03' : {
        'name':'James',
        'intro':'smart smart smart',
        'avatar':'/static/img/student-icon-male-person-profile-avatar-symbol-vector-21850878.jpg'
    },
    's04' : {
        'name':'Tom',
        'intro':'smart smart smart smart',
        'avatar':'/static/img/23046491.jpg'
    },
    's05' : {
        'name':'Sam',
        'intro':'smart smart smart smart smart',
        'avatar':'/static/img/student-icon-white-background-71302919.jpg'
    }

}

@app.route('/')
def school():
    return render_template('school.html', students=students)


@app.route('/student/<sid>')
def student(sid):
    student = students[sid]
    return render_template('student.html', student=student)