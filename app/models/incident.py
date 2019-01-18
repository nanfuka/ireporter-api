import datetime
incidents = []


class Incident:

    def __init__(self, *args):
        """This method acts as a constructor
            for the incident class, it initialises all class attributes
        """
        self.createdby = args[0]
        self.incident_type = args[1]
        self.location = args[2]
        self.status = args[3]
        self.images = args[4]
        self.videos = args[5]
        self.comment = args[6]

    def get_json(self):
        """this method converts the class attributes into json objects
        """
        return{
            "redflag_id": len(incidents) + 1,
            "createdon": datetime.datetime.now(),
            "createdby": self.createdby,
            "incident_type": self.incident_type,
            "location": self.location,
            "status": self.status,
            "images": self.images,
            "videos": self.videos,
            "comment": self.comment

        }
