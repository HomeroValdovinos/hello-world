from flask import Flask, request, render_template
import json
import requests

app = Flask(__name__)


@app.route('/')
def home():
    consulta = 'red hot chili peppers, pulp fiction'
    parametros = {'k': '286940-DevFSens-0KCM0XSU', 'q': consulta}
    url = 'http://tastedive.com/api/similar?'
    respuesta = requests.get(url, params=parametros)
    json_object_response = respuesta.json()


@app.route('/index')
def index():
    return render_template("rendering.html")


if __name__ == '__main__':
    app.run()

