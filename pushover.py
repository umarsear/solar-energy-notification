__author__ = 'Umar Sear'

from pushover import init, Client


def send_push_notification(application_token, user_key, message, title):
    init(application_token)
    Client(user_key).send_message(message, title=title)
