import unittest
from app.views import app
import json
import datetime

class TestUsers(unittest.TestCase):
    def setUp(self):
        self.test_client = app.test_client(self)

    def test_index(self):
        response = self.test_client.get('/')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], "Welcome to I-Reporter API")


    def test_create_redflag(self):

        report = { 
            "createdby":"jkoijbbj",
            "incidenttype" : 'fire the thief',
            "location" : 'luweero',
            "status" : 'draft',
            "images" : 'thief',
            "videos": 'theft',
            "comment" : 'this is serious'  
        }

        response  = self.test_client.post('/api/v1/redflag', json = report)
        self.assertEqual(response.status_code, 201)
    #     report = {
    #         "redflag_id" : 1,
    #         "createdon" : datetime.datetime.now(),
    #         "createdby" : 'Deb',
    #         "intervantion" : 'fire the thief',
    #         "location" : 'luweero',
    #         "status" : 'draft',
    #         "images" : 'thief',
    #         "videos": 'theft',
    #         "comment" : 'this is serious'  
    #     }

    #     response  = self.test_client.post(
    #         '/api/v1/redflag',
    #         content_type='application/json',
    #         data=json.dumps(report)
    #     )

    #     message = json.loads(response.data.decode())
    #     self.assertEqual(message['message'], 'report successfully placed')
    #     self.assertEqual(response.status_code, 201)

    # def test_user_signup_without_create_user(self):
    #     report = { 
    #         "intervantion" : 'fire the thief',
    #         "location" : 'luweero',
    #         "status" : 'draft',
    #         "images" : 'thief',
    #         "videos": 'theft',
    #         "comment" : 'this is serious'  
    #     }

    #     response  = self.test_client.post('/api/v1/redflag', json = report)
    #     self.assertEqual(response.status_code, 201)

        # message = json.loads(response.data.decode())
        # self.assertEqual(message['message'], 'report successfully placed')
        # self.assertEqual(response.status_code, 201)



    # def test_report_without_createuser(self):

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

        # response = self.test_client.get(
        #     'api/v1/users',
        #     headers={'Authorization': 'Bearer ' + token['token']},
        #     content_type='application/json'
        # )

        # message = json.loads(response.data.decode())

        # self.assertEqual(message['message'], 'welcome')

