import re
from flask_restplus import Namespace, fields


def validate_payload(payload):
    pattern_int = re.compile(r"(0|-?[1-9][0-9]*)")
    telefone = payload.get('telefone')

    if not telefone.isdigit():
        return {
            "message": "The phone number is not a integer"
        }, 400   


class UserModel:
    users_schema = Namespace('users', description='Users', validate=True)
    model = users_schema.model('users', {
        "nome": fields.String(required=True, description=(u'Descricao')),
        "email": fields.String(required=True, description=(u'Email')),
        "telefone": fields.String(required=True, description=(u'Telefone')),
        "pais": fields.String(required=False, description=(u'Pais')),
        "cidade": fields.String(required=False, description=(u'Cidade')),
        "endereco": fields.String(required=False, description=(u'Endereco')),
        "senha": fields.String(required=True, description=(u'Senha')),
        "verificado": fields.Boolean(required=True, description=(u'Verificado')),
    })
