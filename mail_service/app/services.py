import sys
import logging
import smtplib
import email.message


logging.basicConfig(filename="teste.log", level=logging.INFO)


def make_link_to_ativate_user(payload):
    return "http://link_to_ativate_user"


def make_email(payload):
    nome = payload.get('nome')
    user_email = payload.get('email')
    link = make_link_to_ativate_user(payload)
    server = smtplib.SMTP('smtp.gmail.com:587')
 
    email_content = """
    <html>
    
    <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        
    <title>Confirmação de Cadastro</title>
    <style type="text/css">
    </style>
    </head>
    
    <body>
    Bem vindo {0}!!!
    Clique no link para confirmar o seu cadastro: {1}
    
    </body>
    </html>
    """.format(nome, link)
 
    msg = email.message.Message()
    msg['Subject'] = 'Confirmação de Usuario'
    
    msg['From'] = 'fake_email@gmail.com'
    msg['To'] = user_email
    password = "testepasswd"
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(email_content)
    
    smtp_server = smtplib.SMTP('smtp.gmail.com: 587')
    smtp_server.starttls()
    
    # Login Credentials for sending the mail
    smtp_server.login(msg['From'], password)
    smtp_server.sendmail(msg['From'], [msg['To']], msg.as_string())


def send_message_to_confirmation_user(payload):
    print('SEND EMAIL')
    
    try:
        link = make_link_to_ativate_user(payload)
        make_email(payload)
    except Exception as e:
        print(e)
    
    nome = payload.get('nome')
    email = payload.get('email')
    log_message = "Email enviado para | Nome: {0} | Email: {1}".format(nome, email)
    print(log_message)
    sys.stdout.write(log_message)
    logging.info(log_message)
    