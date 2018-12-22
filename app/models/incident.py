import datetime
from flask import Flask, jsonify, make_response, request
incidents = []
class Incident:
    def __init__(self, createdby, incidenttype, location, status, video, image, comment):
        self.redflag_id = len(incidents)+1
        self.createdon = datetime.datetime.now()
        self.createdby = createdby
        self.incidenttype = incidenttype
        self.location = location
        self.status = 'draft'
        self.image = image
        self.video = video
        self.comment = comment
    
    def get_json(self):

        return{
            "redflag_id" :len(incidents)+1,
            "createdon" : self.createdon,
            "createdby" : self.createdby,
            "intervantion" :  self.incidenttype,
            "location" : self.location,
            "status" : self.status,
            "images" : self.image,
            "videos": self.video,
            "comment" : self.comment         

    }
    def create_redflags(self):
        record = {
            "redflag_id" :len(incidents)+1,
            "createdon" : self.createdon,
            "createdby" : self.createdby,
            "intervantion" :  self.incidenttype,
            "location" : self.location,
            "status" : self.status,
            "images" : self.image,
            "videos": self.video,
            "comment" : self.comment
        }
        incidents.append(record)
        return record

    def get_a_redflag(self, redflag_id):
        record = [record for record in incidents if record['redflag_id'] == redflag_id]

        if record:

            return jsonify({"status":200, "data":record[0]})

        return jsonify({"message": "the record_id is not available"})

    # def get_redflag(self, ​​redflag_id):
    #     for 
   
    #     record = [redflag for redflag in incidents if record['redflag_id'] == redflag_id]

    #     record[0]['lcation'] = data

    #     if data:f

    #         return jsonify({"success": specific_order}), 200

    #     return jsonify({"message": "The order_id is invalid"}), 400
    # def editredflag(self, redflag_id):
    #     record = [redflag for redflag in incidents if redflag['redflag_id'] == redflag_id]
    #     record[0]['location'] == data

    #     if data:f

    #         return jsonify({"success": specific_order}), 200

    #     return jsonify({"message": "The order_id is invalid"}), 400




