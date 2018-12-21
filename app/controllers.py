
from .models.incident import Incident, incidents


class Methods:

    def create_incident(self, createdby, incidenttype, location, status, video, image, comment):
        incident = Incident(
            createdby=createdby,
            incidenttype=incidenttype,
            location=location,
            video=video,
            image=image,
            status='draft',
            comment=comment)
            

        incidents.append(incident)
        return incident

#     def get_all_redflags(self):
#         if len(incidents) > 0:
#             return incidents

#     def create_incident
#     # incident = Incident()
#     # report = incident.get_json(incident.get_json)

#     # incidents.append(report)
#     # return report

# # def get_all_red_flag_record():
# #     return incidents
# # def get_a_specific_red_flag_record(redflag_id):
# #     redflag = [redflag for redflag in incidents if redflag['redflag_id'] == redflag_id]

# #     if redflag:

# #         return {"redflag": redflag[0]}

# #     return {'message': "the redflag_id is not available"}

# def edit_a_specific_red-flag​​_record():

#     specific_redflag = [redflag for redflag in incidents if redflag['redflag_id'] == redflag_id]

#     specific_redflag[0]['status'] = data

#     if data:

#         return jsonify({"success": specific_order}), 200

#     return jsonify({"message": "The order_id is invalid"}), 400

# def Delete_a _red_flag​​_record():


    

        
