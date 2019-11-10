# Flask RabbitMQ, Jaeger Tracer, Microservices 

Flask RabbitMQ, Jaeger Tracer, Microservices 


# Como Testar a Aplicação

    - docker-compose -f docker-compose.test.yaml up --build
    - docker-compose -f docker-compose.test.yaml down

# Como Executar o Projeto

    - docker-compose up --build
    - Acessar o swagger em http://localhost:5000/
    
    - Requisição Valida:
        curl localhost:5000/users/ -d '{  "nome": "string",  "email": "string",  "telefone": "989529891",  "pais": "string",  "cidade": "string",  "endereco": "string",  "senha": "string",  "verificado": true}' -H 'Content-Type: application/json'

    - Requisição Invalida:
        curl localhost:5000/users/ -d '{"foo": "bar"}' -H 'Content-Type: application/json'

    - É possivel enviar requisições diretamente pelo swagger


# Tecnologias Utilizadas

    - Python
    - Flask, FlaskRestplus
    - Jaeger
    - RabbitMQ
    - Docker
    - Docker-compose

# Fluxo da Aplicação
![alt text](./fluxo.jpg)
