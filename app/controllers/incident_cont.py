from app.models.incident import Incident, incidents
from flask import Flask, jsonify, request, json


class Redflag():

    def __init__(self):
        self.redflag_list = []

   
    def create_redflag(self, createdby, location, comment,  redflag, intervention, status, images, videos):
        self.createdby = createdby
        self.redflag = redflag
        self.intervention = intervention
        # self.incident_type =[self.redflag, self.intervention] 
        self.location = location
        self.status = status
        self.images = images
        self.videos = videos
        self.comment = comment

        incident = Incident( createdby, location, comment, redflag, intervention, status, images, videos)

        newinput = incident.get_json()
        incidents.append(incident.get_json())
        return newinput

    def get_allredflags(self):
        return incidents

   
    def get_a_redflag(self, redflag_id):
        record = [record for record in incidents if record['redflag_id'] == redflag_id]

        if record:

            return jsonify({"status":200, "data":record[0]})

        return jsonify({"message": "the record_id is not available"})

    def edit_record(self, redflag_id):
        data = request.get_json(['location'])
        for redflag in incidents:
            if redflag['redflag_id'] == redflag_id:
                redflag['location']= data
                return redflag

    def delete_record(self, redflag_id):
        record = [redflag for redflag in incidents if redflag['redflag_id'] == redflag_id]
    
        incidents.remove(record[0])
        return jsonify({"status": 200, "message": "was successfully deleted.","data":record[0]})
