from flask import Flask, request, make_response, jsonify
from app.utils.actions import Actions

app = Flask(__name__)


@app.route('/', methods=["GET"])
def home():
    Actions.headlines()
    return "Home success"


@app.route('/lit-bot', methods=['POST'])
def lit():
    command = request.data.get('text')
    slack_user_uid = request.data.get('user_id')
    slack_user_info = Actions.get_user_info(slack_user_uid)
    response_body = ''

    if command not in Actions.allowed_commands():
        response_body = {"text": "Invalid command - try `/lit help` for available commands"}

    if command == 'help':
        response_body = Actions.help()

    if command == 'headlines':
        response_body = Actions.headlines()

    return make_response(jsonify(response_body)), 200
