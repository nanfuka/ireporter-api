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
        self.args = args
        # self.name = params.get('name')
        # self.lastname = params.get('lastname')
        # self.othernames = params.get('othernames')
        # self.email = args
        # self.phoneNumber = args
        # self.username = args
        # self.isAdmin = args
        # self.password = args
            


    def get_dictionary(self):
        print({

            "firstname" : self.args[0],
            "lastname" : self.args[1],
            "othernames" : self.args[2]
    })
user = User('ngfhgf','hjfhgf','ghfgdg')
user.get_dictionary()
# fname['name']=='star'
# fname['lastname']=='trouble'
# fname['othernames']=='nabbs'
# 'grace'== fname.get('name')
# 'naggs'== fname.get('lastname')
# 'erina' == fname.get('othernames')



