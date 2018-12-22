from app.controllers import *
from flask import Flask, jsonify, make_response, request
from app.models.incident import Incident, incidents
from app.validators import *






app = Flask(__name__)


validators = Validators()
methods = Methods()
"""index route"""
@app.route('/')
def index():
    return jsonify({"status": 200, "message": "Welcome to I-Reporter API"}),200

@app.route('/api/v1/redflag', methods=['POST'])
def creates_red_flag():

    red_flag = request.get_json()
    createdby = red_flag.get('created_by')
    incidenttype = red_flag.get('incidenttype')
    location = red_flag.get('location')
    status = red_flag.get('status')
    image = red_flag.get('image')
    video = red_flag.get('video')
    comment = red_flag.get('comment')

    incident = Incident(createdby, incidenttype, location, status, video, image, comment)



    error = validators.validates_incident(createdby, incidenttype, location, status, image, video, comment)

    if error != None:
        return jsonify({'Error': error}), 400 
    return jsonify({"status": 201,  "message": "report successfully placed", "data": incident.get_json()}),201


