from app.models.incident import Incident, incidents
from flask import Flask, jsonify, request, json


class Redflag():

    def __init__(self):
        self.redflag_list = []

    def create_redflag(self, *args):

        self.createdby = args[0]
        self.redflag = args[1]
        self.intervention = args[2]
        self.location = args[3]
        self.status = args[4]
        self.images = args[5]
        self.videos = args[6]
        self.comment = args[7]

        incident = Incident(*args)

        newinput = incident.get_json()
        incidents.append(incident.get_json())
        return newinput


    def validate_input(self, *args):
        createdby = args[0]
        location = args[1]

        redflag = args[2]
        intervention = args[3]
        status = args[4]


        if not createdby or createdby.isspace():
            return 'please enter the id of the creator of this redflag'
        elif not location or location.isspace():
            return 'Enter location.'
        elif not redflag or redflag.isspace():
            return 'Enter a redflag.'
        elif not intervention or intervention.isspace():
            return 'Enter intervantion.'
        elif status != "draft":
            return 'status should either be draft, underinvestigation, resolved or rejected'


    def get_allredflags(self):
        if len(incidents) > 1:
            return jsonify({"status": 201, "data": incidents}), 201
        return jasonify({"status": 200, "message":
                        "there are no redflag records at the moment"}), 200

    def get_a_redflag(self, redflag_id):
        record = [
            record for record in incidents if record[
                'redflag_id'] == redflag_id]

        if record:

            return jsonify({"status": 200, "data": record[0]})

        return jsonify({"status": 404, "error":
                        "the record_id is not available"})

    def edit_record_location(self, redflag_id, data):
        # data = request.get_json(['location'])
        for redflag in incidents:
            if redflag['redflag_id'] == redflag_id:
                redflag['location'] = data
                return redflag



    def edits_record_location(self, redflag_id, item):
        record = [record for record in incidents if record['redflag_id'] == redflag_id]
        if record:
            record[0][item] = request.json.get(item, record[0][item])
            return jsonify({"status": 200, "data": [{"redflag_id": redflag_id, "message": "Updated redflag location"}]}), 200
                               

    def delete_record(self, redflag_id):
        record = [
            redflag for redflag in incidents if redflag[
                'redflag_id'] == redflag_id]
        if record:
            incidents.remove(record[0])
            return jsonify({
                "status":
                200, "message": "was successfully deleted.", "data": record[0]})
        return {"status": 404, "error":
                "the record_id is not available"}

    def edit_redflag(self, redflag_id):
        """ 
        edit a particular redflags
        """
        record = [record for record in incidents if record['redflag_id'] == redflag_id]
        if record:
            return record
        return jsonify({"status": 404, "error": "no incident with such an id"}), 404

