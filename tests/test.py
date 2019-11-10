
import json
import time
import unittest
import requests


class TestPhoenixServer(unittest.TestCase):

    def setUp(self):
        print('SETUP')

   
    def test_can_send_post_request_and_receive_status_201(self):
        url = 'http://phoenix_api:{port}/users/'.format(port=5000)
        data = {
            "nome": "Jonas",
            "email":	"ferreirajonasss@gmail.com",
            "telefone":	"89529899",
            "pais":	"Brasil",
            "cidade":	"SP",
            "endereco":	"Sao Paulo",
            "senha":	"465465121",
            "verificado":	False
        }
        _headers = { 'content-type': 'application/json' }
        response = requests.post(url, json.dumps(data), headers=_headers)
        self.assertEqual(response.status_code, 201)


    def test_can_send_invalid_post_request_and_receive_status_400(self):
        url = 'http://phoenix_api:{port}/users/'.format(port=5000)
        data = {
            "nome": "Jonas",
            "email":	"ferreirajonasss@gmail.com",
            "telefone":	"teste",
            "pais":	"Brasil",
            "cidade":	"SP",
            "endereco":	"Sao Paulo",
            "senha":	"465465121",
            "verificado":	False
        }
        _headers = { 'content-type': 'application/json' }
        response = requests.post(url, json.dumps(data), headers=_headers)
        self.assertEqual(response.status_code, 400)


if __name__=='__main__':
    
    time.sleep(30)
    unittest.main()