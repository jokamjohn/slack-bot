from slackclient import SlackClient
from config import get_env


class SlackHelper:

    def __init__(self):
        self.slack_token = get_env("SLACK_TOKEN")
        self.slack_client = SlackClient(self.slack_token)
        self.slack_channel = get_env("SLACK_CHANNEL")

    def post_message_to_channel(self, msg):
        """
        This method sends a text message to a slack channel whose Id
        has been specified.
        Change the username to match that of your app
        checkout this https://github.com/slackapi/python-slackclient
        :param msg:
        :return:
        """
        return self.slack_client.api_call(
            "chat.postMessage",
            channel=self.slack_channel,
            text=msg,
            username="lit",
            parse="full",
            as_user=False
        )
