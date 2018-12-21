from app.models.incident import Incident, incidents

class Validators:
    #     """
    #     method that adds validation to Incident 
    #     """

    def validates_incident(self,  created_by, incidenttype, location, status, video, image, comment):
        """validate no input and spaces in the input box"""
        if not created_by:
            return "Enter the name of the creator of thin incident"


        if not incidenttype or incidenttype.isspace():
            return "Enter the incidenttype"

        if not location or location.isspace():
            return "Enter the location of the incident"

        if not comment or comment.isspace():
            return "Enter the comment"

        



        """validate data-types"""
        if isinstance(created_by, int) or status == " ":
            return "created_by should be a string"
        if isinstance(location, int):
            return "location should be a string"

        if isinstance(status, int):
            return "status should be a string"

        if isinstance(comment, int):
            return "video should be a string"

        if isinstance(incidenttype, int):
            return "incidenttype should be a string"
        






    # from flask import Flask, jsonify, make_response, request
    # # """This files handles validation of input data"""
    # # import re
    # # #include negative

    # def is_not_valid_user_id(key):
    #     """This method validates numbers"""
    #     if isinstance(key, int): 
    #         return True
        
    #     return jsonify({"status": "404", "message":"phonenumber should be an integer" })
        

    # def is_not_valid_phoneNumber(key):
    #     """This method validates the users phone number"""
    #     if not isinstance(key, int):
    #         return jsonify({"status": "404", "message":"phonenumber should be an integer" })
    #     return jsonify({"status": "404", "message":"phonenumber should be an integer" })


    # # def is_not_valid_username(key):
    # #     """This method validates the users username"""
    # #     if not key or key.isspace() or not re.compile('^[a-zA-Z]+$').match(key) \
    # #             or not len(str(key)) > 4 or not isinstance(key, str) or len(key) > 25:
    # #         return True

    # # def is_not_valid_isAdmin(key):
    # #     """This method validates the users username"""
    # #     if key is not True:
    # #         key == False
    # #     return True

    # # def is_not_valid_email(key):
    # #     if '@' and '.' not in key:
    # #         return True
    # # def is_not_valid_firstname(key):
    # #     """This method validates the users username"""
    # #     if not key or key.isspace() or not re.compile('^[a-zA-Z]+$').match(key) \
    # #             or not len(str(key)) > 4 or not isinstance(key, str) or len(key) > 25:
    # #         return True

    # # def is_not_valid_lastname(key):
    # #     """This method validates the users username"""
    # #     if not key or key.isspace() or not re.compile('^[a-zA-Z]+$').match(key) \
    # #             or not len(str(key)) > 4 or not isinstance(key, str) or len(key) > 25:
    # #         return True

    # # def is_not_valid_othernames(key):
    # #     """This method validates the users username"""
    # #     if not key or key.isspace() or not re.compile('^[a-zA-Z]+$').match(key) \
    # #             or not len(str(key)) > 4 or not isinstance(key, str) or len(key) > 25:
    # #         return True



    # # def is_not_valid_password(key):
    # #     """This method checks to see a password has been entered"""
    # #     if not key or key.isspace() or len(str(key)) < 4:
    # #         return True


    # # def validate_not_username_string(key):
    # #     if not isinstance(key, str):
    # #         return True



    # # def validate_not_username_characters(key):
    # #     if not re.compile('^[a-zA-Z]+$').match(key):
    # #         return True



    # # def validate_not_email(key):
    # #     if '@' and '.' not in key:
    # #         return True


    # # def validate_not_email_structure(key):
    # #     """This method validates the email entered by user"""
    # #     if '@' not in key or '.' not in key or key[0] == '@' or key[0] == '.' or key.index("@") >= key.index('.') \
    # #             or key.count("@") > 1 \
    # #             or key.count(".") > 1 or key.index(".") == key.index("@") + 1:
    # #         return True

    # # def validate_not_keys(parser, number_items):
    # #     if len(parser.keys()) != number_items:
    # #         return True

    # # def validate_signup
    # # 	if validate_not_keys(user_data,8):
    # # 		return make_response(jsonify({"message": "Some fields are missing!"}),400)
    # # 	else:
    # # 		firstname = user_data.get('firstname')
    # # 		lastname = user_data.get('lastname')
    # # 		othernames = user_data.get('othernames')
    # # 		email = user_data.get('email')
    # # 		phoneNumber = user_data.get('phoneNumber')
    # # 		username = user_data.get('username')
    # # 		isAdmin = user_data.get('isAdmin')
    # # 		# date = datetime.datetime.now()
    # # 		password = user_data.get('password')
    # # 	#   lastname, othernames, email, phoneNumber, password,username,  isAdmin):
    # # #write a class for validations
    # # 	if is_not_valid_firstname(firstname.strip()):
    # # 		return make_response(jsonify({"message": "Please enter a valid firstname"}), 400)

    # # 	if is_not_valid_lastname(lastname.strip()):
    # # 		return make_response(jsonify({"message": "Please enter a valid lastname"}), 400)

    # # 	if is_not_valid_othernames(othernames.strip()):
    # # 		return make_response(jsonify({"message": "Please enter a valid othername"}), 400)

    # # 	if is_not_valid_email(email.strip()):
    # # 		return make_response(jsonify({"message": "Please enter a valid email"}), 400)

    # # 	if is_not_valid_phoneNumber(phoneNumber):
    # # 		return make_response(jsonify({"message": "Please enter a valid phoneNumber"}), 400)

    # # 	if is_not_valid_password(password.strip()):
    # # 		return make_response(jsonify({"message": "Please enter a valid password"}), 400)

    # # 	if is_not_valid_username(username.strip()):
    # # 		return make_response(jsonify({"message": "Please enter a valid username"}), 400)

    # # 	new_user =User(firstname, lastname, othernames, email, phoneNumber, password,username, isAdmin)

    # # 	existinguser = new_user.check_user(username)
    # # 	if existinguser:
    # # 		return make_response(jsonify({'message': 'Username already exists'}), 403)
    # # 	new_user.create_user()