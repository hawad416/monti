import time
from flask import Flask

app = Flask(__name__)


@app.route('/')
def welcome():
    return "welcome"
@app.route('/time')
def get_current_time():
    return {'time': time.time()}