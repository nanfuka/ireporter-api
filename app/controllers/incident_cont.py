from app.models.incident import Incident, incidents
from flask import Flask, jsonify, request, json
import re


class Redflag():

    def __init__(self):
        """This method initialises the list in which all redflags will \
        be kept. Innitially, the list is empty
        """
        self.redflag_list = []

    def create_redflag(self, *args):
        """This method innitialises all the attributes that will be used in \
        the create a redflag"""

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
        self.createdby = args[0]
        self.location = args[1]
        self.comment = args[2]
        self.redflag = args[3]
        self.intervention = args[4]
        self.status = args[5]
        self.images = args[6]
        self.videos = args[7]
    
    def validate_location(self, location):
        """Method where all validations are done"""
        geo_location = re.compile(
            "^[0-9]{2}(.)[0-9]{2}( )[0-9]{2}(.)[0-9]{2}$")
        
        if not location or location.isspace():
            return 'please enter the location of this redflag'

        elif not geo_location.match(location):
            string1 = 'invalid location, please enter the lat, long cordinates'
            string2 = 'in this formant, 25.22 56.22'
            return string1 + string2


    def validate_input(self, *args):
            """Method where all validations are done"""
            createdby = args[0]
            redflag = args[1]
            intervention = args[2]
            status = args[3]
            if not createdby:
                return 'please enter the id of the creator of this redflag'
            elif not isinstance(createdby, int):
                return 'createdby should be an id of the creator of the redflag'
            elif not redflag or redflag.isspace():
                return 'Enter a redflag.'
            elif not intervention or intervention.isspace() or\
                    isinstance(intervention, int):
                return 'Enter intervantion.'
            elif status != "draft":
                return 'status should either be draft,\
                underinvestigation, resolved or rejected'


    def get_allredflags(self):
        """Method to return all redflags"""
        if len(incidents) > 1:
            return jsonify({"status": 201, "data": incidents}), 201
        return jasonify({"status": 200, "message":
                         "there are no redflag records at the moment"}), 200

    def get_a_redflag(self, redflag_id):
        """Method that returns a particular \
        redflag with a specific redflag_id"""
        record = [
            record for record in incidents if record[
                'redflag_id'] == redflag_id]

        if record:

            return jsonify({"status": 200, "data": record[0]})

        return jsonify({"status": 404, "error":
                        "the record_id is not available"})

    def edits_record_location(self, redflag_id, item):
        """Method for modifying a particular redflag's attribute """
        record = [record for record in incidents if record[
            'redflag_id'] == redflag_id]
        if record:
            record[0][item] = request.json.get(item, record[0][item])
            return jsonify({"status": 200, "data": [
                {"redflag_id": redflag_id,
                 "message": "Updated redflag location"}]}), 200

    def delete_record(self, redflag_id):
        """method for deleting a particular redflag at a certain redflag_id"""
        record = [
            redflag for redflag in incidents if redflag[
                'redflag_id'] == redflag_id]
        if record:
            incidents.remove(record[0])
            return jsonify({
                "status":
                200, "message": "was successfully deleted.",
                "data": record[0]})
        return {"status": 404, "error":
                "the record_id is not available"}
