from flask import Flask, jsonify, request, json
from app.controllers.incident_cont import Redflag
from app.models.incident import Incident, incidents
from app.validators import validate_data, validate_intdata_type, validate_keys, input_jsonformat


app = Flask(__name__)
redflag = Redflag()

@app.route('/api/v1/')
def index():
    return jsonify({"status":201, "message":"hi welcome to ireporter"})
@app.route('/api/v1/redflag')
def get_redflags():
    
    """ Get all redflags """

    return jsonify({ "status":201, 'redflags': redflag.get_allredflags() }), 200


@app.route('/api/v1/redflag', methods=['POST'])
def add_parcels():
    data = request.get_json()

    createdby = data.get('createdby')
    location = data.get('location')
    comment = data.get('comment')
    redflags = data.get('redflags')
    intervention = data.get('intervention')
    status = data.get('status')
    images = data.get('images')
    videos = data.get('videos')
    redflag = Redflag()
    error_message = redflag.validate_input(createdby, location, redflags, intervention)
    if  error_message:
        return jsonify({"status":404, 'message': error_message}), 404
    new_incident = redflag.create_redflag(data['createdby'], data['location'], data['comment'],data['redflags'],data['intervention'], data['status'], data['images'], data['videos'])
    return jsonify({"status":201, "message":"Added a new incident","data":new_incident}),201

    # # return 

    # """ Create a parcel delivery order """

    # data = request.get_json() 

    # input_type = input_jsonformat(data)
    # # if input_type:
    #     return input_type  

    # valid_key = validate_keys('createdby', data.keys())
    # if valid_key:
    #     return valid_key

    # valid_key = validate_keys('location', data.keys())
    # if valid_key:
    #     return valid_key

    # valid_key = validate_keys('location', data.keys())
    # if valid_key:
    #     return valid_key
    # valid_key = validate_keys('comment', data.keys())
    # if valid_key:
    #     return valid_key

    # valid_key = validate_keys('redflag', data.keys())
    # if valid_key:
    #     return valid_key

    # valid_key = validate_keys('intervention', data.keys())
    # if valid_key:
    #     return valid_key

    # valid_key = validate_keys('status', data.keys())
    # if valid_key:
    #     return valid_key

    # valid_key = validate_keys('images', data.keys())
    # if valid_key:
    #     return valid_key

    # valid_key = validate_keys('videos', data.keys())
    # if valid_key:
    #     return valid_key
 
    # new_parcel = redflag.create_redflag(data['createdby'], data['location'], data['comment'],data['redflag'],data['intervention'], data['status'], data['images'], data['videos'])
    # valid_value = validate_data(data['createdby'])
    # if valid_value:
    #     return valid_value

    # valid_value = validate_data(data['location'])
    # if valid_value:
    #     return valid_value

    # valid_value = validate_data(data['comment'])
    # if valid_value:
    #     return valid_value

    # valid_value = validate_data(data['redflag'])
    # if valid_value:
    #     return valid_value

    # valid_value = validate_data(data['intervention'])
    # if valid_value:
    #     return valid_value

    # valid_value = validate_data(data['comment'])
    # if valid_value:
    #     return valid_value

    # if not data['status']=="draft" and not data['status']=="resolved" and not data['status']=="rejected" and not data['status']=="under_investigation":
    #     return jsonify({"status": 404, "message":"invalid status input. The status should either be draft, resolved, underinvestigation or rejected"})

    # return jsonify({"status": 201, "message":"Added a new incident", "Incident":new_parcel}), 201

@app.route('/api/v1/redflag/<int:redflag_id>', methods=['GET'])
def get_sepecific_record(redflag_id):
    return redflag.get_a_redflag(redflag_id), 200

@app.route('/api/v1/redflag/<int:redflag_id>', methods=['PUT'])
def edit_location(redflag_id):
    return jsonify({"status": 201, "data":redflag.edit_record(redflag_id)}) 

@app.route('/api/v1/redflag/<int:redflag_id>', methods=['DELETE'])
def remove_sepecific_record(redflag_id):
    return redflag.delete_record(redflag_id)

    