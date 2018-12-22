from app.models.incident import Incident, incidents
from flask import Flask, jsonify, make_response, request

class Validators:
    #     """
    #     method that adds validation to Incident 
    #     """

    def validates_incident(self,  createdby, incidenttype, location, status, video, image, comment):
        """validate no input and spaces in the input box"""
        if not createdby:
            return jsonify({"status": 404, "message":"Enter the name of the creator of this incident"}) 


        if not incidenttype or incidenttype.isspace():
            return "Enter the incidenttype"

        if not location or location.isspace():
            return "Enter the location of the incident"

        # if not comment or comment.isspace():
        #     return "Enter the comment"

        



        """validate data-types"""
        if isinstance(createdby, int) or status == " ":
            return "created_by should be a string"
        if isinstance(location, int):
            return "location should be a string"

        if isinstance(status, int):
            return "status should be a string"

        if isinstance(comment, int):
            return "video should be a string"

        if isinstance(incidenttype, int):
            return "incidenttype should be a string"
