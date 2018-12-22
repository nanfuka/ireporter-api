import datetime
"""
    Global variable users_data  holds  user data , initially its empty
"""
users = []

class User:
    def __init__(self, firstname, lastname, othernames, email, phoneNumber, password,username,  isAdmin):
        """
            This method acts as a constructor
            for our class, its used to initialise class attributes
        """

        self.firstname = firstname
        self.lastname = lastname
        self.othernames = othernames
        self.email = email
        self.phoneNumber = phoneNumber
        self.username = username
        self.isAdmin = isAdmin
        self.password = password
            


    def get_dictionary(self):
        return{
            "user_id" : len(users)+1,
            "firstname" : self.firstname,
            "lastname" : self.lastname ,
            "othernames" : self.othernames,
            "email" : self.email,
            "phoneNumber" : self.phoneNumber,
            "username" : self.username,
            "date": datetime.datetime.now(),
            "isAdmin" : False,         
            "user_name" : self.username,
            "password" : self.password
    }




    from app.controllers import *
from flask import Flask, jsonify, make_response, request
from app.models.incident import Incident, incidents
from app.validators import *




validators = Validators()

app = Flask(__name__)

"""index route"""
@app.route('/')
def index():
    return jsonify({"message": "Welcome to I-Reporter API"})

@app.route('/api/v1/redflag', methods=['POST'])
def creates_red_flag():

    red_flag = request.get_json()
    created_by = red_flag.get('created_by')
    incidenttype = red_flag.get('incidenttype')
    location = red_flag.get('location')
    status = red_flag.get('status')
    image = red_flag.get('image')
    videos = red_flag.get('video')
    comment = red_flag.get('comment')

    incident_report= validators.validates_incident(created_by, incidenttype, location, status, video, image, comment)
    if incident_report:
        return jsonify({"status": 400, "message": "some fields are missing"}), 400
    incident_obj = Incident(created_by,
                            incident_type, location, file, comment)

    add_incident = incident_controller.create_incident(
        created_by=incident_obj.created_by,
        incident_type=incident_obj.incident_type,
        location=incident_obj.location,
        file=incident_obj.file,
        comment=incident_obj.comment)
    if add_incident:
        return jsonify({"status": 201, "data": incidents, "message": "incident {} has been created".format(incident_type)}), 201