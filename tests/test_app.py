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

                       "location": "25.22 56.22",
                       "status": "draft",
                       "images": "hjhj",
                       "videos": "jjh",
                       "comment": "theft of funds",
                       "redflags": "kjkjhghgjh",
                       "intervention": "corruption should stop"
                       }

    def test_index(self):
        """Method for testing the index route"""
        response = self.test_client.get('/')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], "hi welcome to ireporter")
        self.assertEqual(data['status'], 201)

    def test_create_redflag(self):
        """This method tests whether a redflag can be created if all the
         attributes are provided"""
        response = self.test_client.post('/api/v1/red-flags', json=self.report)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['status'], 201)
        self.assertEqual(data['message'], "Added a new incident")
        self.assertEqual(data['data']['comment'], "theft of funds")
        self.assertEqual(data['data']['location'], '25.22 56.22')

    # def test_create_red_flag_with_wrong_createdby_field(self):
    #     """This method tests whether a redflag can return an error message if
    #      all the created by key and/ or value is invalid are provided"""
    #     report = {"createdb": "nkjnk",

    #               "location": "25.22 56.22",
    #               "status": "draft",
    #               "images": "hjhj",
    #               "videos": "jjh",
    #               "comment": "hjgjhkj",
    #               "redflags": "kjkjhghgjh",
    #               "intervention": "jhkjhk"
    #               }
    #     response = self.test_client.post('/api/v1/red-flags', json=report)
    #     data = json.loads(response.data)
    #     self.assertEqual(response.status_code, 404)
    #     self.assertEqual(data['status'], 404)
    #     self.assertEqual(data['error'],
    #                      "please enter the id of the creator of this redflag")

    def test_create_red_flag_with_invalid_createdby_value(self):
        """This method tests whether a redflag can return an error message if
         all the created by key and/ or value is invalid are provided"""
        report = {"createdby": "debs",

                  "location": "25.22 56.22",
                  "status": "draft",
                  "images": "hjhj",
                  "videos": "jjh",
                  "comment": "hjgjhkj",
                  "redflags": "kjkjhghgjh",
                  "intervention": "jhkjhk"
                  }
        response = self.test_client.post('/api/v1/red-flags', json=report)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['status'], 404)
        self.assertEqual(
            data['error'],
            "createdby should be an id of the creator of the redflag")

    def test_create_red_flag_with_wrong_locationfield(self):
        """This method tests whether a redflag can return an error message if
         all the location key and/ or value is invalid are provided"""
        report = {"createdby": 2,

                  "locatin": "25.22 56.22",
                  "status": "draft",
                  "images": "hjhj",
                  "videos": "jjh",
                  "comment": "hjgjhkj",
                  "redflags": "kjkjhghgjh",
                  "intervention": "jhkjhk"
                  }
        response = self.test_client.post('/api/v1/red-flags', json=report)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['status'], 404)
        self.assertEqual(
            data
            ['error'],
            'please enter the location of the creator of this redflag')

    def test_create_red_flag_with_wrong_redflagfield(self):
        """This method tests whether a redflag can return an error message if
         all the redflad key and/ or value is invalid are provided"""
        report = {"createdby": 2,

                  "location": "25.22 56.22",
                  "status": "draft",
                  "images": "hjhj",
                  "videos": "jjh",
                  "comment": "hjgjhkj",
                  "redfla": "kjkjhghgjh",
                  "intervention": "jhkjhk"
                  }
        response = self.test_client.post('/api/v1/red-flags', json=report)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['status'], 404)
        self.assertEqual(data['error'], "Enter a redflag.")

    def test_create_red_flag_with_wrong_interventionfield(self):
        """This method tests whether a redflag can return an error message if
         all the intervention key and/ or value is invalid are provided"""
        report = {"createdby": 2,

                  "location": "25.22 56.22",
                  "status": "draft",
                  "images": "hjhj",
                  "videos": "jjh",
                  "comment": "hjgjhkj",
                  "redflags": "kjkjhghgjh",
                  "intervent": "jhkjhk"
                  }
        response = self.test_client.post('/api/v1/red-flags', json=report)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['status'], 404)
        self.assertEqual(data['error'], "Enter intervantion.")

    def test_get_all_redflags(self):
        """This method tests whether after posting valid
        data, all redfalgs can be returned"""
        response = self.test_client.post('/api/v1/red-flags', json=self.report)
        response = self.test_client.get('/api/v1/red-flags')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['status'], 201)

        # self.assertEqual(data['data'], [{'comment': 'theft of funds'}])
        # self.assertEqual(data['data']['location'], ['masaka'])

    def test_get_one_redflag(self):
        """This method tests whether after posting valid
        data, a particular can be returned"""
        response = self.test_client.post('/api/v1/red-flags', json=self.report)

        response = self.test_client.get('/api/v1/red-flags/1')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'], 200)
        self.assertEqual(data['data']['comment'], "theft of funds")
        self.assertEqual(
            data['data']
                ['incident_type'][0], {'intervantion':
                                       'corruption should stop',
                                       'redflag': 'kjkjhghgjh'})

    def test_edit_location(self):
        """This method tests whether after posting valid
        data, a redfalg's location can be modified with a patch method"""
        response = self.test_client.post('/api/v1/red-flags', json=self.report)
        edited_location = {"location": "Mattuga"}
        response = self.test_client.patch('/api/v1/red-flags/1/location',
                                          json=edited_location)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 200)
        self.assertEqual(data['data'][0], {'message':
                                           'Updated redflag location',
                                           "redflag_id": 1})

    def test_edit_comment(self):
        """This method tests whether after posting valid
        data, a redfalg's comment can be modified with a patch method"""
        response = self.test_client.post('/api/v1/red-flags', json=self.report)
        edited_comment = {"location": "treat this very seriously"}
        response = self.test_client.patch('/api/v1/red-flags/1/comment',
                                          json=edited_comment)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 200)
        self.assertEqual(data['data'][0],
                         {'message': 'Updated redflag location',
                          'redflag_id': 1})
