from flask import Flask, request, render_template
# import sqlalchemy
# import time
# import json
# import datetime

try_login = Flask(__name__)


def get_resource_as_string(name, charset='utf-8'):
    with try_login.open_resource(name) as f:
        return f.read().decode(charset)


try_login.jinja_env.globals['get_resource_as_string'] = get_resource_as_string


@try_login.route('/', methods=['GET'])
def home():
    return render_template("index.html")


@try_login.route('/register.html')
def register():
    return render_template("register.html")


@try_login.route('/index.html')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    try_login.run()


