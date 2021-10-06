from flask import Flask, request, jsonify


app = Flask(__name__)
messages = []


@app.route('/health/', methods=['GET'])
def test():
    return "Healthy"


@app.route('/replicate_message/', methods=['POST'])
def replicate_message():
    message = request.json.get('message')
    messages.append(message)
    return jsonify(message)


@app.route('/list_messages/', methods=['GET'])
def list_messages():
    return jsonify(messages)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8009)
