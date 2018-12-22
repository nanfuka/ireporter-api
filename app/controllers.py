from flask import Flask, jsonify, make_response, request
from .models.incident import Incident, incidents



class Methods:
    def create_incident(self, createdby, incidenttype, location, status, video, image, comment):

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

        current_incident = incident.get_json()
        redflag_id :len(incidents)+1,      
        createdby =current_incident['createdby'] 
        intervantion =current_incident['intervantion']
        location =current_incident['location']
        images =current_incident['images']
        status =current_incident['status']
        videos =current_incident['videos']
        comment =current_incident['comment']
            # "intervantion" :  incidenttype,
            # "location" : location,
            # "status" :status,
            # "images" : image,
            # "videos": video,
            # "comment" : comment 
        record = Incident(createdby, incidenttype, location, status, video, image, comment)

        incidents.append(record)
        return current_incident      
        # incidents.append(newreport)
        # return newreport

    def get_all_redflags(self):
        if len(incidents) > 0:
            return incidents

    def get_one_redflag(self, report_id):
        for incident in incidents:
            if incident['report_id'] == report_id:
                return incident
        
    