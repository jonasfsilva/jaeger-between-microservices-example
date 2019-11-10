import json
from services import save_user_on_db
from services import send_message_email_notifications_service
from jaeger_client import Config


def init_jaeger_tracer(service_name='user_microservice'):
    config = Config(config={}, service_name=service_name, validate=True)
    return config.initialize_tracer()


def default_callback(ch, method, properties, body):
    # TODO define router rules
    print('RECEIVE MESSAGE USER MICROSERVICE')
    payload = json.loads(body)
    print(" [x] Received %r" % payload)
    
    tracer = init_jaeger_tracer()
    with tracer.start_span('user_microservice') as span:
        span.log_kv({'add_user.receive_request_data': payload})

    try:
        user_data = save_user_on_db(payload)
        send_message_email_notifications_service(user_data)
    except Exception as e:
        raise e