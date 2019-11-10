import hashlib
from database import User
from amqp import produce_message


def make_hash_password(password):
    return hashlib.md5(password.encode('utf-8')).hexdigest()


def save_user_on_db(user_data):
    senha = user_data.get('senha')
    hash_password = make_hash_password(senha)
    
    try:
        user_data['senha'] = hash_password
        user_created = User.create(
            **user_data
        )
        print('CREATED USER', user_created)
        return user_data
    except Exception as e:
        print(e)
        raise e


def send_message_email_notifications_service(user_data):
    produce_message('send_email', user_data)
