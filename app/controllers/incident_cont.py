from app.models.incident import Incident, incidents


class Redflag():

    def __init__(self):
        self.redflag_list = []

    # def create_redflag(self, createdby, incident_type,location, status, image, video, comment):
    def create_redflag(self, createdby, location, comment,  redflag, intervention, status, images, videos):
        self.createdby = createdby
        self.redflag = redflag
        self.intervention = intervention
        # self.incident_type =[self.redflag, self.intervention] 
        self.location = location
        self.status = status
        self.images = images
        self.videos = videos
        self.comment = comment


    # valid_key = validate_keys('createdby', red_flag.keys())
    # if valid_key:
    #     return valid_key

        # # self.redflag_id =len(self.redflag_list)+1

        # # if not type(redflag_id) == int:
        # #     return 'parcel_id must be an Integer!!'

        # if not type(createdby) == str:
        #     return 'userId must be an str!!'

        # if not type(incidenttype) == str:
        #     return 'pickup must be a string!!'

        # if not type(location) == str:
        #     return 'destination must be a string!!'

        # if not type(status) == str:
        #     return 'status must be an String!!'


        # incident = Incident(createdby, incident_type, location, status, image, video, comment)
        incident = Incident( createdby, location, comment, redflag, intervention, status, images, videos)

        newinput = incident.get_json()
        incidents.append(incident.get_json())
        return newinput

    # def update_status(self, parcel_id):
    #     for parcel in self.parcel_list:
    #         if parcel['parcel_id']==parcel_id: 
    #             parcel['status']='Cancelled'
    #             return parcel

    def get_allredflags(self):
        return incidents

    # def get_parcel(self, parcel_id):
    #     for parcel in self.parcel_list:
    #         if parcel['parcel_id']==parcel_id:
    #             return parcel

    # def get_parcel_user(self, userId):
    #     ttt = []
    #     for parcel in self.parcel_list:
    #         if parcel['userId']==userId:
    #             ttt.append(parcel)
    #     return ttt

    # def get_highest_parcel_id(self):
    #     id_list=[]
    #     if self.redflag_list:
    #         for rediflag in self.redflag_list :
    #             id_list.append(rediflag['redflag_id'])
    #         return(max(id_list))
    #     return 0