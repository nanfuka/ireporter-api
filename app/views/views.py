from flask import Flask, jsonify, request, json
from app.controllers.incident_cont import Redflag
from app.models.incident import Incident
from app.validators import validate_data, validate_keys, input_jsonformat


app = Flask(__name__)
redflag = Redflag()
@app.route('/api/v1/redflag')
def get_redflags():
    
    """ Get all redflags """

    return jsonify({ 'redflags': redflag.get_allredflags() }), 200


@app.route('/api/v1/redflag', methods=['POST'])
def add_parcels():

    """ Create a parcel delivery order """

    data = request.get_json() 

    input_type = input_jsonformat(data)
    if input_type:
        return input_type  

    # valid_key = validate_keys('createdby', data.keys())
    # if valid_key:
    #     return valid_key
    # valid_value = validate_data('createdby')
    # if valid_value:
    #     return valid_value

    # valid_key = validate_keys('location', data.keys())
    # if valid_key:
    #     return valid_key
    # valid_value = validate_data('location')
    # if valid_value:
    #     return valid_value



    # if 'userId' not in list(data.keys()):
    #     return jsonify({
    #         "message":'User Id missing in data',
    #         "required format":{"userid": "int", "weight": "float",
    #             "status":"string","destination":"string","pickup":"string"}
    #         }), 400

    
    # if 'weight' not in list(data.keys()):
    #     return jsonify({
    #         "message":'Weight missing in data',
    #         "required format":{"userid": "int", "weight": "float",
    #             "status":"string","destination":"string","pickup":"string"}
    #         }), 400
            
    # if 'status' not in list(data.keys()):
    #     return jsonify({
    #         "message":'Status missing in data',
    #         "required format":{"userid": "int", "weight": "float",
    #             "status":"string","destination":"string","pickup":"string"}
    #         }), 400

    # if 'destination' not in list(data.keys()):
    #     return jsonify({
    #         "message":'Destination missing in data',
    #         "required format":{"userid": "int", "weight": "float",
    #             "status":"string","destination":"string","pickup":"string"}
    #         }), 400

    # if 'pickup' not in list(data.keys()):
    #     return jsonify({
    #         "message":'Pickup missing in data',
    #         "required format":{"userid": "int", "weight": "float",
    #             "status":"string","destination":"string","pickup":"string"}
    #         }), 400

    # redflag_id = 1+redflag.get_highest_parcel_id(), , , , comment
    # incident_type = []
    # new_parcel = redflag.create_redflag(data['createdby'], data['incident_type'], data['location'], data['status'], data['image'], data['video'], data['comment'])
    new_parcel = redflag.create_redflag(data['createdby'], data['location'], data['comment'],data['redflag'],data['intervention'], data['status'], data['images'], data['videos'])

    return jsonify({"Added Parcel":new_parcel}), 201

