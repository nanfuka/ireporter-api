# from app.models.users import User
from app.models.ti import Ti, users
from flask import Flask, jsonify, request, json
import re


class User():

    def __init__(self):
        """This method initialises the list in which all user details will \
        be kept. Innitially, the list is empty
        """
        self.user_list = []

    def signup(self, *args):
        """This method innitialises all the attributes that will be used in \
        the creation of a user"""
        self.firstname = args[0]
        self.lastname = args[1]
        self.othernames = args[2]
        self.email = args[3]
        self.phoneNumber = args[4]
        self.username = args[5]
        self.isAdmin = args[6]
        self.password = args[7]

        ti = Ti(*args)
        newuser = ti.get_dictionary()

        users.append(ti.get_dictionary())
        return newuser

    def login(self, username, password):
        for user in users:
            if user['username'] == username and user['password'] == password:
                return {"status": 201,
                        "message": "you have logged in successfully"}
            else:
                return {"status": 404, "error": "The username and password are incorrect"}

    def check_repitition(self, username, email, password):
        for user in users:
            if user['username'] == username:
                return "Username already exists, choose another one"
            elif user['email'] == email:
                return "Email already exists, choose another one"
            elif user['password'] == password:
                return "password already exists, choose another one"
            elif len(password) < 4:
                return "password strength is too weak"
            
