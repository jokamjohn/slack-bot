from flask import Flask, request, jsonify
from app.utils.actions import Actions

app = Flask(__name__)


@app.route('/', methods=["GET"])
def home():
    Actions.headlines()
    return "Home success"


@app.route('/lit-bot', methods=['POST'])
def lit():
    command = request.form.get('text')
    slack_user_uid = request.form.get('user_id')
    response_body = ''

    if command not in Actions.allowed_commands():
        response_body = {"text": "Invalid command - try `/lit help` for available commands"}

    if command == 'help':
        response_body = Actions.help()

    if command == 'headlines':
        response_body = Actions.headlines()
        Actions.send_to_user(slack_user_uid)

    response = jsonify(response_body)
    response.status_code = 200
    return response
