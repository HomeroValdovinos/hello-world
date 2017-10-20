from flask import Flask, request, render_template
import time
import json
import datetime

app = Flask(__name__)


@app.route('/')
def home():
    return "<h1>Hola mundo!!!!!<h1/>"


@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/timestamp', methods=['POST'])
def get_timestamp():
    current_time = time.time()
    time_millis = int(round(current_time * 1000))
    print " Time in millis is: ", time_millis
    return str(time_millis)


@app.route('/messages', methods=['POST'])
def api_message():
    if request.headers['Content-type'] == 'text/plan':
        return "Text Message: " + request.data
    elif request.headers['Content-type'] == 'application/json':
        return "JSON Message: " + json.dumps(request.json)
    else:
        return "415 unsupported File"


@app.route("/datetime", methods=["POST"])
def get_datetime():
    request_body = json.loads(request.data)
    milis_time = int(request_body["millis"])
    date_time_gen = datetime.datetime.fromtimestamp(milis_time/1000)
    print("the date time is: ", date_time_gen)
    return str(date_time_gen)


@app.route('/name/')
@app.route('/name/<name>')
def name(name=None):
    return render_template('hello.html', name=name)


@app.route('/suma', methods=['GET'])
def suma():
    a = int(request.args.get('numero1'))
    b = int(request.args.get('numero2'))
    suma = a + b
    return str(suma)


if __name__ == '__main__':
    app.run()

