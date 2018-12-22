# from app.controllers import *
from flask import Flask, jsonify, make_response, request
from app.models.incident import Incident, incidents
from app.validators import *






app = Flask(__name__)


validators = Validators()
# methods = Methods()
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

    # error = validators.validates_incident(createdby, incidenttype, location, status, image, video, comment)

    # if error:
    #     return jsonify({'Error': error}), 400 
    incident = Incident(createdby, incidenttype, location, status, video, image, comment)
    incident.create_redflags()
    # methods.create_incident(createdby, incidenttype, location, status, video, image, comment)
    return jsonify({"status": 201,  "message": "report successfully placed", "data": incident.create_redflags()}),201


@app.route('/api/v1/redflag', methods=['GET'])
def get_red_flags():

    return jsonify({"data":incidents})

@app.route('/api/v1/redflag/<int:redflag_id>', methods=['GET'])
def get_sepecific_record(redflag_id):
    incident = Incident('createdby', 'incidenttype', 'location', 'status', 'video', 'image', 'comment')
    return incident.get_a_redflag(redflag_id)

# @app.route('/api/v1/redflag/<int:redflag_id>', methods=['PATCH'])
# def ​redflag​​(redflag_id):
#     data = request.get_json(['location'])

#     record = [redflag for redflag in incidents if redflag['redflag_id'] == redflag_id]
#     record[0]['location'] == data

#     specific_order[0]['status'] = data

#     if data:

#         return jsonify({"data": record, "message":"location successfully modified"}), 200

#     return jsonify({"message": "The flag_id is invalid"}), 400
@app.route('/api/v1/redflag/<int:redflag_id>', methods=['DELETE'])
def remove_sepecific_record(redflag_id):
    record = [redflag for redflag in incidents if redflag['redflag_id'] == redflag_id]
    
    incidents.remove(record[0])
    return jsonify({"status": 200, "message": "was successfully deleted.","data":record[0]})


    # current_incident = request.get_json()
    # redflag_id :len(incidents)+1     
    # createdby =current_incident['createdby'] 
    # incidenttype =current_incident['incidenttype']
    # location =current_incident['location']
    # image =current_incident['image']
    # status =current_incident['status']
    # video =current_incident['video']
    # comment =current_incident['comment']
        # "intervantion" :  incidenttype,
        # "location" : location,
        # "status" :status,
        # "images" : image,
        # "videos": video,
        # "comment" : comment 
    # record = Incident(createdby, incidenttype, location, status, video, image, comment)

    # incidents.append(record.get_json)
    # return jsonify({"data": "you posted something"})



    # red_flag = request.get_json()
    # createdby = red_flag.get['created_by']
    # incidenttype = red_flag.get['incidenttype']
 
    # location =red_flag.current_incident['location']
    # images =red_flag.current_incident['images']
    # status =red_flag.current_incident['status']
    # videos =red_flag.current_incident['videos']
    # comment =red_flag.current_incident['comment']

    # incident = Incident(createdby, incidenttype, location, status, video, image, comment)



    # error = validators.validates_incident(createdby, incidenttype, location, status, image, video, comment)

    # if error != None:
    #     return jsonify({'Error': error}), 400 
    # return jsonify({"status": 201,  "message": "report successfully placed", "data": incident.get_json()}),201




# from app.controllers import *
# from flask import Flask, jsonify, make_response, request
# from app.models.incident import Incident, incidents
# from app.validators import *

# app = Flask(__name__)

# incidents = []
# validators = Validators()
# methods = Methods()
# """index route"""
# @app.route('/')
# def index():
#     return jsonify({"status": 200, "message": "Welcome to I-Reporter API"}),200

# @app.route('/api/v1/redflag', methods=['POST'])
# # def creates_red_flag():
# def create_incident(self, createdby, incidenttype, location, status, video, image, comment):
        
#     current_incident = request.get_json()
#     redflag_id :len(incidents)+1      
#     createdby =current_incident['createdby'] 
#     intervantion =current_incident['intervantion']
#     location =current_incident['location']
#     images =current_incident['images']
#     status =current_incident['status']
#     videos =current_incident['videos']
#     comment =current_incident['comment']
    
#     record = Incident(createdby, incidenttype, location, status, video, image, comment)

#     incidents.append(record)
#     return jsonify({current_incident}) 
        # incident = Incident(
        #     createdby=createdby,
        #     incidenttype=incidenttype,
        #     location=location,
        #     video=video,
        #     image=image,
        #     status='draft',
        #     comment=comment) 

        # newreport ={
        #     "redflag_id" :len(incidents)+1,
        
        #     "createdby" : createdby,
        #     "intervantion" :  incidenttype,
        #     "location" : location,
        #     "status" :status,
        #     "images" : image,
        #     "videos": video,
        #     "comment" : comment 
        #     }

        # current_incident = incident.get_json()
        # redflag_id :len(incidents)+1,      
        # createdby =current_incident['createdby'] 
        # intervantion =current_incident['intervantion']
        # location =current_incident['location']
        # images =current_incident['images']
        # status =current_incident['status']
        # videos =current_incident['videos']
        # comment =current_incident['comment']
            # "intervantion" :  incidenttype,
            # "location" : location,
            # "status" :status,
            # "images" : image,
            # "videos": video,
            # "comment" : comment 
        # record = Incident(createdby, incidenttype, location, status, video, image, comment)

        # incidents.append(record)
        # return current_incident      
        # incidents.append(newreport)
        # return newreport
    # red_flag = request.get_json()
    # createdby = red_flag.get('created_by')
    # incidenttype = red_flag.get('incidenttype')
    # location = red_flag.get('location')
    # status = red_flag.get('status')
    # image = red_flag.get('image')
    # video = red_flag.get('video')
    # comment = red_flag.get('comment')

    # # valid_incident = validators.validates_incident(createdby, incidenttype, location, status, video, image, comment)

    # incident = Incident(createdby, incidenttype, location, status, video, image, comment)
    # error = validators.validates_incident(createdby, incidenttype, location, status, image, video, comment)

    # if error:
    #     return jsonify({'Error': error}), 400 

    # methods.create_incident(createdby, incidenttype, location, status, video, image, comment)
    # return jsonify({"status": 201,  "message": "report successfully placed", "data": incident.get_json()}),201

    # def create_incident():
    #     request_data = request.get_json()
    #     created_by = request_data.get('created_by')
    #     incident_type = request_data.get('incident_type')
    #     location = request_data.get('location')
    #     file = request_data.get('file')
    #     comment = request_data.get('comment')
    #     valid_incident = incident_validator.validate_incident(created_by,
    #                                                         incident_type, location, file, comment)
    #     if valid_incident:
    #         return jsonify({"status": 400, "message": "some fields are empty"}), 400
    #     incident_obj = Incident(created_by,
    #                             incident_type, location, file, comment)

    #     add_incident = incident_controller.create_incident(
    #         created_by=incident_obj.created_by,
    #         incident_type=incident_obj.incident_type,
    #         location=incident_obj.location,
    #         file=incident_obj.file,
    #         comment=incident_obj.comment)
    #     if add_incident:
    #         return jsonify({"status": 201, "data": incidents, "message": "incident {} has been created".format(incident_type)}), 201



    # all_red_flags = methods.get_all_redflags()
    # if all_red_flags:
    #     return jsonify({"status":200, "data":incidents})
    # return jsonify({"status": 200, "message": "There are no incidents at the moment"}), 200


