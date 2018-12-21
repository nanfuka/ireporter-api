import datetime

incidents = []
class Incident:
    def __init__(self, createdby, incidenttype, location, status, video, image, comment):
        self.report_id = len(incidents)+1
        self.createdon = datetime.datetime.now()
        self.createdby = createdby
        self.incidenttype = incidenttype
        self.location = location
        self.status = 'draft'
        self.image = image
        self.video = video
       
        self.comment = comment
    
    def get_json(self):

        return{
            "redflag_id" :self.report_id,
            "createdon" : self.createdon,
            "createdby" : self.createdby,
            "intervantion" :  self.incidenttype,
            "location" : self.location,
            "status" : self.status,
            "images" : self.image,
            "videos": self.video,
            "comment" : self.comment         

    }
