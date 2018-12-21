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
    return jsonify({"message": "Welcome to I-Reporter API"})

@app.route('/api/v1/redflag', methods=['POST'])
def creates_red_flag():

    red_flag = request.get_json()
    created_by = red_flag.get('created_by')
    incidenttype = red_flag.get('incidenttype')
    location = red_flag.get('location')
    status = red_flag.get('status')
    image = red_flag.get('image')
    video = red_flag.get('video')
    comment = red_flag.get('comment')


    error = validators.validates_incident(created_by, incidenttype, location, status, image, video, comment)

    if error != None:
        return jsonify({'Error': error}), 400

    # incident_report= validators.validates_incident(created_by, incidenttype, location, status, videos, image, comment)
#     if incident_report:
#         return jsonify({"status": 400, "message": "some fields are missing"}), 400
#     incident_obj = Incident(created_by,
#                             incident_type, location, file, comment)

#     add_incident = incident_controller.create_incident(
#         created_by=incident_obj.created_by,
#         incident_type=incident_obj.incident_type,
#         location=incident_obj.location,
#         file=incident_obj.file,
#         comment=incident_obj.comment)
    # if not incident_report():
    
    # new_incident =Incident(createdby, incidenttype, location, status, video, image, comment)
    
    return jsonify({"status": 201, "data": validators.validates_incident(incidenttype, location, status, video, image, comment)})

    # return jsonify({"message": incident_report()})

# @app.route('/api/v1/redflag')
# def get_all_flag_record():
#     return jsonify({"status": 201, "Data": get_all_red_flag_record()})

# @app.route('/api/v1/specific_redflag/<int:report_id>')
# def get_a_specific _red_flag​​_record():
#     return jsonify({"status": 201, "Data":get_a_specific_red_flag_record(redflag_id)})

# ○ Edit a specific ​red-flag​​ record  ○ Delete a ​red-flag​​ record 
