import flask
from flask import request, jsonify
import requests
# careful not to mix flask's request with requests!

import threading

#
PORT = 8000

app = flask.Flask(__name__)

# there's a _data so the Python compiler won't confuse the function and the variables
hello_data = {'hello': 'there', 'response': 'ok'}
bye_data = ['good', 'bye']

@app.route('/', methods=['GET'])
def base_greeting():
    return jsonify('Greetings')

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify(hello_data)

@app.route('/hi', methods=['GET'])
def hi():
    if 'name' in request.args:
        return jsonify('hi ' + request.args['name'])
    else:
        return jsonify('hi John Doe')

@app.route('/bye', methods=['GET'])
def bye():
    return jsonify(bye_data)

if __name__ == "__main__":
    thread = threading.Thread(target=app.run, kwargs=dict(host='localhost', port=PORT))
    thread.start()
    url = f'http://localhost:{PORT}'
    request_hello = requests.get(url + '/hello')
    print(request_hello.json())
    request_hi = requests.get(url + '/hi?name=bob')
    print(request_hi.json())
