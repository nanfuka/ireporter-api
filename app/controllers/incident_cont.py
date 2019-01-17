from app.models.incident import Incident, incidents
from flask import Flask, jsonify, request, json


class Redflag:

    def create_redflag(self, *args):
        """This method innitialises all the attributes that will be used in \
        the creation of a redflag"""

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

    def get_allredflags(self):
        """Method to return all redflags"""
        if len(incidents) > 1:
            return jsonify({"status": 201, "data": incidents}), 201
        return jsonify({"status": 204, "message":
                        "there are no redflag records at the moment"}), 204

    def get_a_redflag(self, redflag_id):
        """Method that returns a particular \
        redflag with a specific redflag_id"""
        record = [
            record for record in incidents if record[
                'redflag_id'] == redflag_id]

        if record:

            return jsonify({"status": 200, "data": record[0]})

        return jsonify({"status": 204, "message":
                        "the record_id is not available"}), 204

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
                "data": record[0]}), 200
