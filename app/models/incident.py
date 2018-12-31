import datetime
incidents = []

class Incident:
    # def __init__(self, createdby, location,comment, redflag, intervention, status, images, videos):
    # def __init__(self, *args):
    #     self.createdby = createdby
    #     self.location = location
    #     self.comment = comment
    #     self.redflag = redflag
    #     self.intervention = intervention
    #     self.status = status
    #     self.images = images
    #     self.videos = videos

    def __init__(self, *args):
        self.createdby = args[0]
        self.location = args[1]
        self.comment = args[2]
        self.redflag = args[3]
        self.intervention = args[4]
        self.status = args[5]
        self.images = args[6]
        self.videos = args[7]

    def get_json(self):
        
        return{
            "redflag_id" :len(incidents)+1,
            "createdon" : datetime.datetime.now(),
            "createdby" : self.createdby,
            "incident_type" :  [{"redflag":self.redflag, "intervantion":self.intervention}],
            "location" : self.location,
            "status" : [{"status":self.status}],
            "images" : [{"images":self.images}],
            "videos": [{"videos":self.videos}],
            "comment" : self.comment         

    }


    # def get_a_redflag(self, redflag_id):
    #     record = [record for record in incidents if record['redflag_id'] == redflag_id]

    #     if record:

    #         return jsonify({"status":200, "data":record[0]})

    #     return jsonify({"message": "the record_id is not available"})

    # def get_redflag(self, ​​redflag_id):
    #     for 
   
    #     record = [redflag for redflag in incidents if record['redflag_id'] == redflag_id]

    #     record[0]['lcation'] = data

    #     if data:f

    #         return jsonify({"success": specific_order}), 200

    #     return jsonify({"message": "The order_id is invalid"}), 400
    # def editredflag(self, redflag_id):
    #     record = [redflag for redflag in incidents if redflag['redflag_id'] == redflag_id]
    #     record[0]['location'] == data

    #     if data:f

    #         return jsonify({"success": specific_order}), 200

    #     return jsonify({"message": "The order_id is invalid"}), 400



