import datetime
"""
    Global variable users_data  holds  user data , initially its empty
"""
users = []

class User:
    def __init__(self, firstname, lastname, othernames, email, phoneNumber, password,username,  isAdmin):
        """
            This method acts as a constructor
            for our class, its used to initialise class attributes
        """
        # date = len(users)+1
        # isAdmin = False
        # self.user_id = user_id
        self.firstname = firstname
        self.lastname = lastname
        self.othernames = othernames
        self.email = email
        self.phoneNumber = phoneNumber
        self.username = username
        # self.date = date
        self.isAdmin = isAdmin
        self.password = password
            


    def get_dictionary(self):
        return{
            "user_id" : len(users)+1,
            "firstname" : self.firstname,
            "lastname" : self.lastname ,
            "othernames" : self.othernames,
            "email" : self.email,
            "phoneNumber" : self.phoneNumber,
            "username" : self.username,
            "date": datetime.datetime.now(),
            "isAdmin" : False,         
            "user_name" : self.username,
            "password" : self.password
    }

    def create_user(self):
        """
            This method receives an object of the
            class, creates and returns a dictionary from the object
        """
        oneuser = {
            
            "user_id" : len(users)+1,
            "firstname" : self.firstname,
            "lastname" : self.lastname ,
            "othernames" : self.othernames,
            "email" : self.email,
            "phoneNumber" : self.phoneNumber,
            "username" : self.username,
            "date": datetime.datetime.now(),
            "isAdmin" : False,
      
            "user_name" : self.username,
            "email" : self.email,
            "password" : self.password
        }

        users.append(oneuser)

        return oneuser
    @staticmethod
    def get_user_id(username):
        for oneuser in users:
            if username == oneuser['username']:
                return oneuser['user_id']
        return {"message": "user doesn't exist"}

    def getalluser(self):
        return {"users":users}

    def check_user(self, username):
        """Method to check if a give user already exists in the database"""
        for one_user in users:
            if username == one_user['username']:
                return True
            return False
    


