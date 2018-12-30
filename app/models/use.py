import datetime
"""
    Global variable users_data  holds  user data , initially its empty
"""
users = []

class User:
    def __init__(self, *args):
        """
            This method acts as a constructor
            for our class, its used to initialise class attributes
        """

        self.firstname = args
        self.lastname = args
        self.othernames = args
        self.email = args
        self.phoneNumber = args
        self.username = args
        self.isAdmin = args
        self.password = args
            


    def get_dictionary(self):
        print({
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
    })
user = User('firstname', 'lastname', 'othernames', 'email', 'phoneNumber', 'password','username',  'isAdmin')
user.get_dictionary()
