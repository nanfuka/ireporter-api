import datetime
"""
    Global variable users_data  holds  user data , initially its empty
"""
    thernames” ​:​ ​String​,  ​“email” ​:​ ​String​,  ”phoneNumber” ​:​ ​String,  ​“username” ​:​ ​String​,  ​“registered” ​:​ ​Date​,  ​“isAdmin” ​:​ ​Boolean
users = []

class User:
    def __init__(self, user_id, firstname, lastname, othernames,, email, phoneNumber,username,  date, isAdmin):
        """
            This method acts as a constructor
            for our class, its used to initialise class attributes
        """
        self.user_id = user_id
        self.firstname = firstname
        self.lastname = lastname
        self.othernames = othernames
        self.email = email
        self.phoneNumber = phoneNumber
        self.username = user_name
        self.date = date
        self.isAdmin = isAdmin
            pass


    def get_dictionary(self):
        return{
            "user_id" : len(users)+1,
            "firstname" : self.firstname,
            "lastname" : self.lastname ,
            "othernames" : self.othernames,
            "email" : self.email,
            "phoneNumber" : self.phoneNumber,
            "username" : self.user_name,
            "date": datetime.datetime.now()
            "isAdmin" : False
            "user_id" :len(use)+1,
            "user_name" : self.user_name,
            "email" : self.email,
            "password" : self.password
    }

    def create_user(self):
        """
            This method receives an object of the
            class, creates and returns a dictionary from the object
        """
        oneuser = {
            
            "user_id" : len(user)+1,
            "firstname" : self.firstname,
            "lastname" : self.lastname ,
            "othernames" : self.othernames,
            "email" : self.email,
            "phoneNumber" : self.phoneNumber,
            "username" : self.user_name,
            "date": datetime.datetime.now()
            "isAdmin" : False
            "user_id" :len(use)+1,
            "user_name" : self.user_name,
            "email" : self.email,
            "password" : self.password
        }

        users.append(oneuser)

        return user
    @staticmethod
    def get_user_id(username):
        for oneuser in users:
            if username == oneuser['username']:
                return oneuser['user_id']
        return {"message": "user doesn't exist"}

    def getalluser(self):
        return {"users":users}
    


