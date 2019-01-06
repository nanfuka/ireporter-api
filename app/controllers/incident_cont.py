from app.models.incident import Incident, incidents
from flask import Flask, jsonify, request, json


class Redflag():

    def __init__(self):
        self.redflag_list = []

    def create_redflag(self, *args):

        self.createdby = args[0]
        self.redflag = args[1]
        self.intervention = args[2]
        # self.incident_type =[self.redflag, self.intervention]
        self.location = args[3]
        self.status = args[4]
        self.images = args[5]
        self.videos = args[6]
        self.comment = args[7]

        incident = Incident(*args)

        newinput = incident.get_json()
        incidents.append(incident.get_json())
        return newinput


    # def validate_input(self, createdby, location,redflag, intervention):
    def validate_input(self, createdby, location, redflag, intervention,
                       status):

        # if createdby not in lst:
        #     return "Createdby field must be present", 404

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

    # def validate_keys(self, createdby, location, lst):
    #     if createdby not in lst:
    #         return "All fields must be present", 404
    #     elif not location or location.isspace():
    #         return 'Email field can not be left empty.'

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
            # return {"status": 404, "error":
            #         "the record_id is not available"}

    # def edit_record_comments(self, redflag_id, newcomment):

    #     record = [
    #         record for record in incidents if record[
    #             'redflag_id'] == redflag_id]

    #     if record:
    #         record['comment'] = newcomment

    #         return jsonify({"status": 200, "data": record})

        # return jsonify({"status": 404, "error":
        #                 "the record_id is not available"})

        # for redflag in incidents:
        #     if redflag['redflag_id'] == redflag_id:
        #         # redflag['comment'] = data
        #         return redflag
        # data = request.get_json(['comment'])
        # for redflag in incidents:
        #     if redflag['redflag_id'] == redflag_id:
        #         redflag['comment'] = data
        #     return redflag
            #     if redflag:
            #         return jsonify({"status": 201, "data": redflag})
            #     return jsonify({"status": 404, "error":
            #                    "the record_id is not available"})
            # return {"status": 404, "error":
            #                 "the record_id is not available"}                               

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



    # def update_incident(self, incident_id, request_data, keyword, username):

    #     location = request_data.get("location")

    #     if self.validator.check_empty_string(location):
    #         return self.response_unaccepted("empty")

    #     if self.validator.check_str_datatype(location):
    #         return self.response_unaccepted("datatype")

    #     update_incident_instance = incident_data.update_incident(
    #         incident_id, request_data, keyword, username)
    #     if update_incident_instance is None:
    #         return self.response_unaccepted("none")
    #     elif update_incident_instance == "non_author":
    #         return Response(json.dumps({
    #             "status":401,
    #             "message": "You are not authorised to edit this incident."
    #         }), content_type="application/json", status=401)
    #     else:
    #         return self.response_sumission_success(update_incident_instance,
    #                                                "update")

    def edit_redflag(self, redflag_id):
        """ 
        edit a particular redflags
        """
        record = [record for record in incidents if record['redflag_id'] == redflag_id]
        if record:
            return record
        return jsonify({"status": 404, "error": "no incident with such an id"}), 404

    # def update_location(self, incident_id):
    #     """ 
    #     updates single  redflags
    #     """
    #     red_flag = [
    #         incident for incident in incidents if incident['incident_id'] == incident_id]
    #     return red_flag