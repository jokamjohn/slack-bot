from flask import Flask

app = Flask(__name__)


@app.route('/', methods=["GET"])
def home():
    """
    Add code to send a message to a channel within a slack workspace
    1. Create a slack app and get the token
    2. Create a slack channel and get the slack Id which you then add to
    the .env file
    3. Run the app to send the message to the channel
    :return:
    """
    return "Hello Andela Uganda DevCon"
