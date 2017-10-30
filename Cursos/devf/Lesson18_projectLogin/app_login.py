from flask import Flask, request, render_template
from Utils.models import db
# from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from Utils.models import Login

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def server():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        Login.user_name = Login(user_name='username')
        Login.user_password = Login(user_password='password')
        db.session.add(Login.user_name)
        db.session.add(Login.user_password)
        db.session.commit()
        # return 'The credentials for %s and %s and id $s' % (username, password)
    else:
        return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "<h1>ENTRASTE AL POST!!!!!<h1/>"
    else:
        return "<h1>GEEEEEEEEEEEEET!!!!!<h1/>"


@app.route('/register')
def register():
    return render_template('register.html')


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=4000)

