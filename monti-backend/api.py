import time
from flask import Flask

app = Flask(__name__)


@app.route('/')
def welcome():
    return "welcome"
@app.route('/time')
def get_current_time():
    return {'time': time.time()}

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/story', methods=['GET'])
def get_story():
    story = [
        {'text': 'Once upon a time...', 'image': 'image_url_1'},
        {'text': 'The adventure begins...', 'image': 'image_url_2'},
        # Add more story pages
    ]
    return jsonify(story)

@app.route('/api/comprehension', methods=['POST'])
def comprehension_check():
    data = request.get_json()
    response = data['response']
    # Analyze response and provide feedback
    feedback = analyze_response(response)
    return jsonify(feedback)

def analyze_response(response):
    # Dummy feedback logic
    if len(response) > 10:
        return {'feedback': 'Great job!'}
    else:
        return {'feedback': 'Please provide a more detailed answer.'}


