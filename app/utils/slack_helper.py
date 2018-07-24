from slackclient import SlackClient
from config import get_env
import json


class SlackHelper:

    def __init__(self):
        self.slack_token = get_env("SLACK_TOKEN")
        self.slack_client = SlackClient(self.slack_token)
        self.slack_channel = get_env("SLACK_CHANNEL")

    def post_message(self, msg, recipient):
        return self.slack_client.api_call(
            "chat.postMessage",
            channel=recipient,
            text=msg,
            as_user=True
        )

    def post_message_to_channel(self, msg):
        return self.slack_client.api_call(
            "chat.postMessage",
            channel=self.slack_channel,
            text=msg,
            username="lit",
            parse="full",
            as_user=False
        )

    def post_message_with_attachment(self, message):
        return self.slack_client.api_call(
            "chat.postMessage",
            channel=self.slack_channel,
            username="lit",
            parse="full",
            attachments=json.dumps(message),
            as_user=False
        )

    def post_message_to_user_with_attachments(self, message, recipient):
        return self.slack_client.api_call(
            "chat.postMessage",
            channel=recipient,
            attachments=json.dumps(message),
            as_user=True
        )

    def file_upload(self, file_content, file_name, file_type, title=None, ):
        return self.slack_client.api_call(
            "files.upload",
            channels=self.slack_channel,
            content=file_content,
            filename=file_name,
            filetype=file_type,
            initial_comment='{} Log File'.format(file_name),
            title=title
        )

    def get_user_info(self, uid):
        return self.slack_client.api_call(
            "users.info",
            user=uid,
            token=self.slack_token
        )
