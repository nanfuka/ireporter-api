import datetime
"""
    Global variable users  holds  user data , initially its empty
"""
users = []


class Ti:
    def __init__(self, *args):

        self.firstname = args[0]
        self.lastname = args[1]
        self.othernames = args[2]
        self.email = args[3]
        self.phoneNumber = args[4]
        self.username = args[5]
        self.isAdmin = args[6]
        self.password = args[7]

    def get_dictionary(self):
        return{
            "user_id": len(users) + 1,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "othernames": self.othernames,
            "email": self.email,
            "phoneNumber": self.phoneNumber,
            "username": self.username,
            "date": datetime.datetime.now(),
            "isAdmin": self.isAdmin,
            "user_name": self.username,
            "password": self.password
        }
