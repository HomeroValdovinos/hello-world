from flask import Flask, request, render_template
import json
import requests
from tastedive import TasteDive

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    # query = 'Game of Thrones'
    # parameters = {'k': '287946-Test-90NR5BYV', 'q': query}
    # url = 'http://tastedive.com/api/similar?'
    # response = requests.get(url, params=parameters)
    # data = response.text
    taste = TasteDive()
    return render_template("rendering.html", data=taste.Results)


if __name__ == '__main__':
    app.run()

