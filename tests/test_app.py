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

    def test_delete_redfalg(self):
        report = [{"createdby": 3,

                  "location": "22.98 33.26",
                  "status": "draft",
                  "images": "imagelocation",
                  "videos": "videolocation",
                  "comment": "this is over recurring",
                  "incident_type": "redflag"
                  },
                  {"createdby": 3,

                  "location": "22.98 33.26",
                  "status": "draft",
                  "images": "imagelocation",
                  "videos": "videolocation",
                  "comment": "this is over recurring",
                  "incident_type": "redflag"
                  }]
        response = self.test_client.post('/api/v1/red-flags', json=report)
        response = self.test_client.delete('/api/v1/red-flags/2/redflag')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)

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
        self.assertEqual(
            data['message'], "Successfully signedup with ireporter")
        self.assertEqual(data['data']['firstname'], "debrah")
        self.assertEqual(data['data']['othernames'], "Nsubuga")
        self.assertEqual(data['data']['username'], "nanfuka")
        self.assertEqual(data['data']['phoneNumber'], 777777)

    def test_login(self):
        """method for testing the login"""
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
        self.assertEqual(
            data[0], {'message': 'you have logged in successfully',
                      'status': 201})

        logins = {"username": "nanfuks",
                  "password": "secres"}
        response = self.test_client.post('/api/v1/login', json=logins)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(
            data, {"error": "user with such credentials does not exist",
                   'status': 404})

    def test_create_redflag(self):
        """This method tests whether a redflag can be created if all the
         attributes are provided"""
        response = self.test_client.post('/api/v1/red-flags', json=self.report)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['status'], 201)
        self.assertEqual(
            data['data'], [{'id': 1, 'message': 'Added a new incident'}])

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
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['status'], 400)
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
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['status'], 400)
        self.assertEqual(
            data,
            {"error":
             "Incident type should either be a redflag or intervention.",
             "status": 400})

    def test_edit_location(self):
        """This method tests whether after posting valid
        data, a redfalg's location can be modified with a patch method"""
        report = {"createdby": 3,

                  "location": "22.98 33.26",
                  "status": "draft",
                  "images": "imagelocation",
                  "videos": "videolocation",
                  "comment": "this is over recurring",
                  "incident_type": "redflag"
                  }
        edited_location = {"location": "22.33 44.56"}
        response = self.test_client.patch('/api/v1/red-flags/1/location',
                                          json=edited_location)
        self.assertEqual(response.status_code, 200)

    def test_edit_comment(self):
        """This method tests whether after posting valid
        data, a redfalg's comment can be modified with a patch method"""
        response = self.test_client.post('/api/v1/red-flags', json=self.report)
        edited_comment = {"comment": "treat this very seriously"}
        response = self.test_client.patch('/api/v1/red-flags/1/comment',
                                          json=edited_comment)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)

    def test_get_one_redflag(self):
        """This method tests whether after posting valid
        data, a particular can be returned"""
        report = {"createdby": 2,

                  "location": "22.98 33.26",
                  "status": "draft",
                  "images": "imagelocation",
                  "videos": "videolocation",
                  "comment": "this is over recurring",
                  "incident_type": "redflag"
                  }
        response = self.test_client.post('/api/v1/red-flags', json=report)

        response = self.test_client.get('/api/v1/red-flags/1')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'], 200)
        self.assertEqual(data['data']['comment'], 'treat this very seriously')
        self.assertEqual(data['data']['createdby'], 2)
        self.assertEqual(data['data']['images'], "imagelocation")
        self.assertEqual(data['data']['incident_type'], "redflag")
        self.assertEqual(data['data']['location'], "22.33 44.56")
        self.assertEqual(data['data']['redflag_id'], 1)
        self.assertEqual(data['data']['status'], "draft")
        self.assertEqual(data['data']['videos'], "videolocation")



