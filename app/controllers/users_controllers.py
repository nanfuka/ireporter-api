# from app.models.users import User
from app.models.ti import Ti, users
from flask import Flask, jsonify, request, json
import re


class User():

    def __init__(self):
        """This method initialises the list in which all user details will \
        be kept. Innitially, the list is empty
        """
        self.user_list = []

    def signup(self, *args):
        """This method innitialises all the attributes that will be used in \
        the create a redflag"""
        self.firstname = args[0]
        self.lastname = args[1]
        self.othernames = args[2]
        self.email = args[3]
        self.phoneNumber = args[4]
        self.username = args[5]
        self.isAdmin = args[6]
        self.password = args[7]

        ti = Ti(*args)
        newuser = ti.get_dictionary()

        users.append(ti.get_dictionary())
        return newuser
    
    def login(self, username, password):
        for user in users:
            if user['username'] ==username and user['password'] == password:
                return {"status":201, "message": "you have logged in successfully"}
            else:
                return {"error":"The username and password are incorrect"}

    # def validate_location(self, location):
    #     """Method where all validations are done"""
    #     geo_location = re.compile(
    #         "^[0-9]{2}(.)[0-9]{2}( )[0-9]{2}(.)[0-9]{2}$")

    #     if not location or location.isspace():
    #         return 'please enter the location of this redflag'

    #     elif not geo_location.match(location):
    #         string1 = 'invalid location, please enter the lat, long cordinates'
    #         string2 = 'in this formant, 25.22 56.22'
    #         return string1 + string2

    # def validate_input(self, *args):
    #     """Method where all validations are done"""
    #     createdby = args[0]
    #     incident_type = args[1]
    #     status = args[2]
    #     if not createdby:
    #         return 'please enter the id of the creator of this redflag'
    #     elif not isinstance(createdby, int):
    #         return 'createdby should be an id of the creator of the redflag'
    #     elif not incident_type or incident_type.isspace():
    #         return 'Enter a redflag.'
    #     elif incident_type != "redflag" and incident_type != "intervention":
    #         return 'Incident type should either be a redflag or intervention.'
    #     elif status != "draft":
    #         return 'status should either be draft,\
    #             underinvestigation, resolved or rejected'

    # def validate_coment(self, comment):
    #     if not comment or comment.isspace():
    #         return 'Enter the comment'
    #     if isinstance(comment, int):
    #         return 'Comment should be a string'

    # def get_allredflags(self):
    #     """Method to return all redflags"""
    #     if len(incidents) > 1:
    #         return jsonify({"status": 201, "data": incidents}), 201
    #     return jsonify({"status": 200, "message":
    #                     "there are no redflag records at the moment"}), 200

    # def get_a_redflag(self, redflag_id):
    #     """Method that returns a particular \
    #     redflag with a specific redflag_id"""
    #     record = [
    #         record for record in incidents if record[
    #             'redflag_id'] == redflag_id]

    #     if record:

    #         return jsonify({"status": 200, "data": record[0]})

    #     return jsonify({"status": 404, "error":
    #                     "the record_id is not available"})

    # def edits_record_location(self, redflag_id, item, newvalue):
    #     """Method for modifying a particular redflag's attribute """

    #     record = [record for record in incidents if record[
    #         'redflag_id'] == redflag_id]

    #     if record:
    #         record[0][item] = newvalue

    #         return jsonify({"status": 200, "message": "Updated redflag"}), 200

    # def delete_record(self, redflag_id):
    #     """method for deleting a particular redflag at a certain redflag_id"""
    #     record = [
    #         redflag for redflag in incidents if redflag[
    #             'redflag_id'] == redflag_id]
    #     if record:
    #         incidents.remove(record[0])
    #         return jsonify({
    #             "status":
    #             200, "message": "was successfully deleted.",
    #             "data": record[0]})
    #     return {"status": 404, "error":
    #             "the record_id is not available"}
