import cta
import api_key

from flask import Flask
app = Flask(__name__)
routes = ['red', 'blue', 'brn', 'g', 'org', 'p', 'pink', 'y']


@app.route('/')
def hello_world():
    data = cta.get_coords(routes)
    print(data)
    return data
