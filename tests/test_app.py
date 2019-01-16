import unittest
from app.views.views import app
import json
import datetime


class TestUsers(unittest.TestCase):

    def setUp(self):
        """Method for innitialising app for testing"""
        self.app = app

        self.test_client = app.test_client()

        self.report = {"createdby": 2,

                       "location": "22.98 33.25",
                       "status": "draft",
                       "images": "imagelocation",
                       "videos": "videolocation",
                       "comment": "this is over recurring",
                       "incident_type": "redflag"
                       }

        self.user = {"firstname": "debrah",
                     "lastname": "kalungi",
                     "othernames": "Nsubuga",
                     "email": "kalungi2k6@yahoo.com",
                     "PhoneNumber": 777777,
                     "username": "nanfuka",
                     "isAdmin": "true",
                     "password": "secrets"
                     }
        self.login = {"username": "nanfuka",
                      "password": "secrets"}
   
    def test_index(self):
        """Method for testing the index route"""
        response = self.test_client.get('/')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], "hi welcome to ireporter")
        self.assertEqual(data['status'], 201)

    def test_signup(self):
        response = self.test_client.post('/api/v1/signup', json=self.user)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['message'], "Successfully signedup with ireporter")
        self.assertEqual(data['data']['firstname'], "debrah")
        self.assertEqual(data['data']['othernames'], "Nsubuga")
        self.assertEqual(data['data']['username'], "nanfuka")
        self.assertEqual(data['data']['phoneNumber'], 777777)

    def test_login(self):
        user = {"firstname": "debrah",
                "lastname": "kalungi",
                "othernames": "Nsubuga",
                "email": "kalungid2k6@yahoo.com",
                "PhoneNumber": 777777,
                "username": "nanfukas",
                "isAdmin": "true",
                "password": "secretss"
                }
        response = self.test_client.post('/api/v1/signup', json=user)
        login = {"username": "nanfukas",
                 "password": "secretss"}
        response = self.test_client.post('/api/v1/login', json=login)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data[0], {'message': 'you have logged in successfully', 'status': 201})
        
        logins = {"username": "nanfuks",
                  "password": "secres"}
        response = self.test_client.post('/api/v1/login', json=logins)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data, {"error": "user with such credentials does not exist", 'status': 404})


    def test_create_redflag(self):
        """This method tests whether a redflag can be created if all the
         attributes are provided"""
        response = self.test_client.post('/api/v1/red-flags', json=self.report)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['status'], 201)
        self.assertEqual(data['message'], "Added a new incident")
        self.assertEqual(data['data']['comment'], "this is over recurring")
        self.assertEqual(data['data']['location'], '22.98 33.25')

    def test_create_red_flag_with_invalid_createdby_value(self):
        """This method tests whether a redflag can return an error message if
         all the created by key and/ or value is invalid are provided"""
        report = {"createdby": "dfeefet",

                       "location": "22.98 33.25",
                       "status": "draft",
                       "images": "imagelocation",
                       "videos": "videolocation",
                       "comment": "this is over recurring",
                       "incident_type": "redflag"
                       }
        response = self.test_client.post('/api/v1/red-flags', json=report)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['status'], 404)
        self.assertEqual(
            data['error'],
            "createdby should be an id of the creator of the redflag")

    def test_create_red_flag_with_wrong_incidenttype_value(self):
        """This method tests whether a redflag can return an error message if
         all the location key and/ or value is invalid are provided"""
        report = {"createdby": 2,

                       "location": "22.98 33.25",
                       "status": "draft",
                       "images": "imagelocation",
                       "videos": "videolocation",
                       "comment": "this is over recurring",
                       "incident_type": "theft"
                       }
        response = self.test_client.post('/api/v1/red-flags', json=report)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['status'], 404)
        self.assertEqual(data, {"error": "Incident type should either be a redflag or intervention.", "status": 404})


    def test_get_all_redflags(self):


        user = {"firstname": "debrah",
                "lastname": "kalungi",
                "othernames": "Nsubuga",
                "email": "kalungidg2k6@yahoo.com",
                "PhoneNumber": 777777,
                "username": "nanfukass",
                "isAdmin": "true",
                "password": "secretsss"
                }

        response = self.test_client.post('/api/v1/signup', json=user)
        data = json.loads(response.data)
        token = json.loads(response.data.decode())

        # response = self.test_client.post('/api/v1/signup', json=user)
        # login = {"username": "nanfukass",
        #          "password": "secretsss"}
        # response = self.test_client.post('/api/v1/login', json=login)
        # data = json.loads(response.data)
        # token = json.loads(response.data.decode())

        response2 = self.test_client.get('/api/v1/red-flags')
        headers={'Authorisation':'Bearer'+ token['access_token']},
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 201)


        # response = self.test_client.post('/api/v1/red-flags', json=self.report)
        # response = self.test_client.get('/api/v1/red-flags', json=self.report)
        # headers = {'Authorisation':'Bearer'+ token['access_token']},
        # data = json.loads(response.data)
        # self.assertEqual(response.status_code, 201)
        # self.assertEqual(data["status"], 201)
        # self.assertEqual(data['user']['email'], "kassd@yahoo.com")



        # response2 = self.test_client.get('/api/v1/oneuser/1')
        # headers={'Authorisation':'Bearer'+ token['access_token']},
        # data = json.loads(response.data)
        # self.assertEqual(response.status_code, 201)
        # self.assertEqual(data["status"], 201)
        # self.assertEqual(data['user']['email'], "kassd@yahoo.com")
        # """This method tests whether after posting valid
        # data, all redfalgs can be returned"""
        # response = self.test_client.post('/api/v1/red-flags', json=self.report)
        # response = self.test_client.get('/api/v1/red-flags')
        # data = json.loads(response.data)
        # self.assertEqual(response.status_code, 201)
        # self.assertEqual(data['status'], 201)

        # self.assertEqual(data['data'], [{'comment': 'theft of funds'}])
        # self.assertEqual(data['data']['location'], ["22.98 33.25"])

    # def test_get_one_redflag(self):
    #     """This method tests whether after posting valid
    #     data, a particular can be returned"""
    #     response = self.test_client.post('/api/v1/red-flags', json=self.report)

    #     response = self.test_client.get('/api/v1/red-flags/1')
    #     data = json.loads(response.data)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(data['status'], 200)
    #     self.assertEqual(data['data']['comment'], "theft of funds")
    #     self.assertEqual(
    #         data['data']
    #             ['incident_type'][0], {'intervantion':
    #                                    'corruption should stop',
    #                                    'redflag': 'kjkjhghgjh'})

    # def test_edit_location(self):
    #     """This method tests whether after posting valid
    #     data, a redfalg's location can be modified with a patch method"""
    #     response = self.test_client.post('/api/v1/red-flags', json=self.report)
    #     edited_location = {"location": "22.33 44.56"}
    #     response = self.test_client.patch('/api/v1/red-flags/1/location',
    #                                       json=edited_location)
    #     self.assertEqual(response.status_code, 200)
    #     data = json.loads(response.data)
    #     self.assertEqual(data['status'], 200)
    #     self.assertEqual(data['message'], 'Updated redflag')
        # self.assertEqual(data['message'][0], {"redflag_id": 1})
        # self.assertEqual(data['data'][0], {'message':
        #                                    'Updated redflag location',
        #                                    "redflag_id": 1})

    # def test_edit_comment(self):
    #     """This method tests whether after posting valid
    #     data, a redfalg's comment can be modified with a patch method"""
    #     response = self.test_client.post('/api/v1/red-flags', json=self.report)
    #     edited_comment = {"comment": "treat this very seriously"}
    #     response = self.test_client.patch('/api/v1/red-flags/1/comment',
    #                                       json=edited_comment)
    #     data = json.loads(response.data)
    #     self.assertEqual(response.status_code, 200)

# self.assertEqual(data['status'], 200)
# self.assertEqual(data['data'][0],
#                  {'message': 'Updated redflag comment',
#                   'redflag_id': 1})

# def test_edit_comment_withwrong_redflagid(self):
#     """this method tests is a redflag can be edited if upon requesting for
#      a redflag, an unavailable redflagid was given
#     """
#     response = self.test_client.post('/api/v1/red-flags', json=self.report)
#     edited_comment = {"location": "treat this very seriously"}
#     response = self.test_client.patch('/api/v1/red-flags/16/comment',
#                                       json=edited_comment)
#     data = json.loads(response.data)
#     self.assertEqual(data['status'], 404)
#     # self.assertEqual(data['data'][0],
#     #                  {'message': 'Updated redflag location',
#     #                   'redflag_id': 1})
#     self.assertEqual(data['error'], 'data with such id not available')
