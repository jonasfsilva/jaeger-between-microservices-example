import json
import opentracing
from flask import Flask 
from flask_opentracing import FlaskTracing
from flask_restplus import Api, Resource
from flask import request
from models import UserModel
from amqp import open_conn
from amqp import produce_message
from models import validate_payload
from jaeger_client import Config


app = Flask(__name__)
api = Api(app=app)


api_usuarios = UserModel.users_schema
api.add_namespace(api_usuarios)


def init_jaeger_tracer(service_name='phoenix_api'):
    config = Config(
        config={ # usually read from some yaml config
            'sampler': {
                'type': 'const',
                'param': 1,
            },
            'local_agent': {
                'reporting_host': 'jaeger',
                # 'reporting_port': 'your-reporting-port',
            },
            'logging': True,
        },
        service_name=service_name, 
        validate=True
    )
    return config.initialize_tracer()


tracer = FlaskTracing(init_jaeger_tracer, True, app)


@api_usuarios.route("/")
class UserList(Resource):
    
    @api_usuarios.expect(UserModel.model, validate=True)
    def post(self): 
        payload = json.loads(request.data)
        
        with opentracing.tracer.start_span('Adicionando o Usuario') as span:
            span.set_tag("add_user.request_data", payload)

            custom_erros = validate_payload(payload)
            if custom_erros:
                with opentracing.tracer.start_span('Dados de Telefone Invalido', child_of=span) as child_span:
                    child_span.set_tag("add_user.invalid_data", payload)
                    return custom_erros

            with opentracing.tracer.start_span('Enviando dados p/ user_microservice', child_of=span) as child_span:
                child_span.set_tag("add_user.send_user_microservice_data", payload)
                child_span.set_tag("add_user.trace_id", span.trace_id)
                produce_message("create", payload)

        
        return {
            "message" : "Successfully Created User"
        }, 201


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')