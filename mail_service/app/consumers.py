import json 
from services import send_message_to_confirmation_user


def default_callback(ch, method, properties, body):
    # TODO define routers and rules here!
    print('RECEIVE MESSAGE MAIL MICROSERVICE')
    payload = json.loads(body)
    print(" [x] Received %r" % payload)
    send_message_to_confirmation_user(payload)

