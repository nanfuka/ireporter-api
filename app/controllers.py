
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