from collections import deque

from flask import Flask, request, jsonify


app = Flask(__name__)
messages = deque()


@app.route('/health/', methods=['GET'])
def test():
    return 'Healthy'


@app.route('/message/', methods=['POST'])
def replicate_message():
    message = request.json.get('message')
    messages.append(message)
    return 'replicated'


@app.route('/messages/', methods=['GET'])
def list_messages():
    return jsonify(list(messages))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8009)
