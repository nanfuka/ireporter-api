from flask import Flask, jsonify, make_response, request
from app.models.users import User, users
from app.validators import  *
from flask_jwt_extended import JWTManager
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_jwt_extended import create_access_token
app = Flask(__name__)
import datetime
jwt = JWTManager(app)

app.config['SECRET_KEY'] = 'customerkey'



# def customer_token(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         token = request.headers.get('Authorization')
#         if not token:
#             return {'message': 'Token is missing'}, 403
#         try:
#             jwt.decode(token[7:], app.config['SECRET_KEY'])
#         except:
#             return {'message': 'Token is invalid'}, 403
#         return f(*args, **kwargs)
#     return decorated

@app.route('/api/v1/signup', methods=['POST'])
def signup():
    """Method handling the user signup route"""
    print(request.get_json())
    try:
        user_data = request.get_json()

        if validate_not_keys(user_data,8):
            return make_response(jsonify({"message": "Some fields are missing!"}),400)
        else:
            firstname = user_data.get('firstname')
            lastname = user_data.get('lastname')
            othernames = user_data.get('othernames')
            email = user_data.get('email')
            phoneNumber = user_data.get('phoneNumber')
            username = user_data.get('username')
            isAdmin = user_data.get('isAdmin')
            # date = datetime.datetime.now()
            password = user_data.get('password')
        #   lastname, othernames, email, phoneNumber, password,username,  isAdmin):

        if is_not_valid_firstname(firstname.strip()):
            return make_response(jsonify({"message": "Please enter a valid firstname"}), 400)

        if is_not_valid_lastname(lastname.strip()):
            return make_response(jsonify({"message": "Please enter a valid lastname"}), 400)

        if is_not_valid_othernames(othernames.strip()):
            return make_response(jsonify({"message": "Please enter a valid othername"}), 400)

        if is_not_valid_email(email.strip()):
            return make_response(jsonify({"message": "Please enter a valid email"}), 400)

        if is_not_valid_phoneNumber(phoneNumber):
            return make_response(jsonify({"message": "Please enter a valid phoneNumber"}), 400)

        if is_not_valid_password(password.strip()):
            return make_response(jsonify({"message": "Please enter a valid password"}), 400)

        if is_not_valid_username(username.strip()):
            return make_response(jsonify({"message": "Please enter a valid username"}), 400)

        new_user =User(firstname, lastname, othernames, email, phoneNumber, password,username, isAdmin)

        existinguser = new_user.check_user(username)
        if existinguser:
            return make_response(jsonify({'message': 'Username already exists'}), 403)
        new_user.create_user()
        
        token = create_access_token(username)
        return jsonify({'user-data':new_user.get_dictionary(),
            'token': token,
            'message': f'{username} successfully registered.'
                }), 201   
    except Exception as error:
        raise error


@app.route('/api/v1/login', methods=['POST'])
def login():
    user_data = request.get_json()
    username = user_data.get('username')
    password = user_data.get('password')

    if validate_not_keys(user_data,2):
      return make_response(jsonify({"message": "Some fields are missing!", "user":username}),400)
 
    for one_user in users:
        if password == one_user['password'] and username == one_user["username"]:
            access_token = create_access_token(identity={"username": username})
            return make_response(jsonify({
                "message": "You have successfully logged in", "access token": access_token, "users":username}), 200)

    return make_response(jsonify({"message": "No such username and password"}), 200)
   
   
@app.route('/api/v1/users', methods=['GET'])
def get_users():
    """ 
        This method returns all users
        of the id given to it from the list of available orders
    """
    if users:
        return make_response(jsonify({"users": users}), 200)
    return make_response(jsonify({"message": "there are currently no users registered"}),
                        404)


