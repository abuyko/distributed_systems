import requests
from flask import Flask, request, jsonify

app = Flask(__name__)
messages = []

client_ports = ['8009', '8010']


@app.route('/health/', methods=['GET'])
def test():
    return "Hello World!"


@app.route('/add_message/', methods=['POST'])
def add_message():
    message = request.json.get('message')
    messages.append(message)

    headers = {'Content-type': 'application/json'}
    for port in client_ports:
        url = f'http://localhost:{port}/replicate_message'
        r = requests.post(
            url,
            json={'message': message},
            headers=headers,
        )

        if r.ok:
            continue

    return jsonify(message)


@app.route('/list_messages/', methods=['GET'])
def list_messages():
    return jsonify(messages)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8008)
