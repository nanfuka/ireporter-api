import unittest
from app.views import app
import json

class TestUsers(unittest.TestCase):
    def setUp(self):
        self.test_client = app.test_client(self)

    def test_user_signup(self):
        report = {
            "redflag_id" : 1,
            "createdon" : 22/2/2012,
            "createdby" : 'Deb',
            "intervantion" : 'fire the thief',
            "location" : 'luweero',
            "status" : 'draft',
            "images" : 'thief',
            "videos": 'theft',
            "comment" : 'this is serious'  
        }

        response  = self.test_client.post(
            '/api/v1/redflag',
            content_type='application/json',
            data=json.dumps(user)
        )

        message = json.loads(response.data.decode())
        self.assertEqual(message['message'], 'deborah successfully registered')

    # def test_users(self):

    #     user1 = {
    #         'username': 'deborah',
    #         'email': 'deb@gmail.com',
    #         'password': 'kanatanata'
    #     }

    #     response1 = self.test_client.post(
    #         'api/v1/signup',
    #         content_type='application/json',
    #         data=json.dumps(user1)
    #     )

    #     token = json.loads(response1.data.decode())
    #     print(token)

        response = self.test_client.get(
            'api/v1/users',
            headers={'Authorization': 'Bearer ' + token['token']},
            content_type='application/json'
        )

        message = json.loads(response.data.decode())

        self.assertEqual(message['message'], 'welcome')

