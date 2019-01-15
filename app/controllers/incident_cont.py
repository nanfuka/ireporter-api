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
        self.incident_type = args[1]
        self.location = args[2]
        self.status = args[3]
        self.images = args[4]
        self.videos = args[5]
        self.comment = args[6]

        incident = Incident(*args)

        newinput = incident.get_json()
        incidents.append(incident.get_json())
        return newinput

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
        incident_type = args[1]
        status = args[2]
        if not createdby:
            return 'please enter the id of the creator of this redflag'
        elif not isinstance(createdby, int):
            return 'createdby should be an id of the creator of the redflag'
        elif not incident_type or incident_type.isspace():
            return 'Enter a redflag.'
        elif incident_type != "redflag" and incident_type != "intervention":
            return 'Incident type should either be a redflag or intervention.'
        elif status != "draft":
            return 'status should either be draft,\
                underinvestigation, resolved or rejected'

    def validate_coment(self, comment):
        if not comment or comment.isspace():
            return 'Enter the comment'
        if isinstance(comment, int):
            return 'Comment should be a string'

    def validate_user_details(self, *args):
        firstname = args[0]
        lastname = args[1]
        # othernames = args[2]
        email = args[2]
        # phoneNumber = args[4]
        username = args[3]
        # isAdmin = args[6]
        password = args[4]


        if not firstname or not lastname or not email or not username or not password:

        # if not firstname or not lastname or not othernames or not email or not phoneNumber or not username or not password:
            return "Enter all items"
        elif isinstance(firstname, int) or isinstance(lastname, int) or isinstance(username, int):
            return "the input should be a string"
        

    def get_allredflags(self):
        """Method to return all redflags"""
        if len(incidents) > 1:
            return jsonify({"status": 201, "data": incidents}), 201
        return jsonify({"status": 200, "message":
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

    def edits_record_location(self, redflag_id, item, newvalue):
        """Method for modifying a particular redflag's attribute """

        record = [record for record in incidents if record[
            'redflag_id'] == redflag_id]

        if record:
            record[0][item] = newvalue

            return jsonify({"status": 200, "message": "Updated redflag"}), 200

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
