from collections import deque

import requests
from flask import Flask, request, jsonify

app = Flask(__name__)
messages = deque()

client_ports = ['8009']


@app.route('/health/', methods=['GET'])
def test():
    return 'Healthy'


@app.route('/message/', methods=['POST'])
def add_message():
    message = request.json.get('message')
    messages.append(message)

    for port in client_ports:
        url = f'http://client:{port}/message'
        r = requests.post(
            url,
            json={'message': message},
        )

        if not r.text == 'replicated':
            return f'{r.status_code}: {r.reason}'

    return jsonify(message)


@app.route('/messages/', methods=['GET'])
def list_messages():
    return jsonify(list(messages))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8008)
