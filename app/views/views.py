from flask import Flask, jsonify, request, json
# from flasgger import Swagger, swag_from
from app.validators import Validators
from app.controllers.incident_cont import Redflag
from app.controllers.users_controllers import User
from app.models.incident import Incident, incidents
from flask_jwt_extended import create_access_token, JWTManager, jwt_required,\
    get_jwt_identity


app = Flask(__name__)
jwt = JWTManager(app)
app.config['JWT_SECRET_KEY'] = 'thisismysecret'
redflag = Redflag()
validators = Validators()


@app.route('/')
def index():
    """index url"""
    return jsonify({"status": 201, "message": "hi welcome to ireporter"})


@app.route('/api/v1/signup', methods=['POST'])
def signup():
    """A user can signup by entering all the required data"""
    data = request.get_json()
    firstname = data.get('firstname')
    lastname = data.get('lastname')
    othernames = data.get('othernames')
    email = data.get('email')
    phoneNumber = data.get('phoneNumber')
    username = data.get('username')
    isAdmin = data.get('isAdmin')
    password = data.get('password')
    user = User()

    invalid_detail = user.check_repitition(username, email, password)
    error_message = validators.validate_user_details(firstname, lastname,
                                                     email, username, password,
                                                     phoneNumber, isAdmin,
                                                     othernames)
    if error_message:
        return jsonify({"status": 400, 'error': error_message}), 400
    elif invalid_detail:
        return jsonify({"status": 400, 'error': invalid_detail}), 400
    else:
        newuserinput = user.signup(
            data['firstname'],
            data['lastname'],
            data['othernames'],
            data['email'],
            data['PhoneNumber'],
            data['username'],
            data['isAdmin'],
            data['password'])
    token = create_access_token(username)

    return jsonify({
        "status": 201,
        "message": "Successfully signedup with ireporter",
        "data": newuserinput, "access_token": token}), 201


@app.route('/api/v1/login', methods=['POST'])
def login():
    """route for logging in into the application"""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    user = User()
    loggedin_user = user.login(username, password)

    if loggedin_user:
        token = create_access_token(username)
        return jsonify(loggedin_user, {"access_token": token})
    else:
        return jsonify(
            {"status": 404,
             "error": "user with such credentials does not exist"}), 404


@app.route('/api/v1/red-flags')
# @jwt_required
def get_redflags():
    """ A user can retrieve all redflag records\
    only after including the bearer token in the header
    """
    if redflag.get_allredflags():
        return jsonify({"status": 200, "data": redflag.get_allredflags()})
    return jsonify({"status": 200, "message": "there are currently no redflag records"})


@app.route('/api/v1/red-flags/<int:redflag_id>', methods=['GET'])
# @jwt_required
def get_sepecific_record(redflag_id):
    """route to rertieve a redflag at a specific route"""
    return redflag.get_a_redflag(redflag_id)


@app.route('/api/v1/red-flags', methods=['POST'])
def create_redflags():
    """A user can create a redflag by entering all the required data"""
    data = request.get_json()
    createdby = data.get('createdby')
    location = data.get('location')
    comment = data.get('comment')
    incident_type = data.get('incident_type')
    status = data.get('status')
    images = data.get('images')
    videos = data.get('videos')
    redflag = Redflag()
    error_message = validators.validate_input(
        createdby, incident_type, status)
    wrong_location = validators.validate_location(location)
    if wrong_location:
        return jsonify({"status": 400, 'error': wrong_location}), 400
    elif error_message:
        return jsonify({"status": 400, 'error': error_message}), 400
    new_incident = redflag.create_redflag(
        data['createdby'],
        data['incident_type'],
        data['location'],
        data['status'],
        data['images'],
        data['videos'],
        data['comment'])

    return jsonify({"status": 201, "data": [{"id": new_incident['redflag_id'],"message": "Added a new incident"}]}), 201


@app.route('/api/v1/red-flags/<int:redflag_id>/location', methods=['PATCH'])
# @jwt_required
def edit_location(redflag_id):
    """
    using this route a user can modify the location of a single redflag
    """
    data = request.get_json()
    location = data.get('location')
    wrong_location = validators.validate_location(location)
    if wrong_location:
        return jsonify({"status": 400, 'error': wrong_location}), 400
    elif redflag.edits_record_location(redflag_id, 'location', location):
        return jsonify({"status": 201, "data": redflag.edits_record_location(redflag_id, 'location', location)})
    return jsonify({"status": 200, "message": "the redflag with redflag_id is not available"})


@app.route('/api/v1/red-flags/<int:redflag_id>/comment', methods=['PATCH'])
# @jwt_required
def edit_comment(redflag_id):

    # """
    # Route where a user can edit the comment of a particular redfalg
    # """
    data = request.get_json()
    comment = data.get('comment')

    error_message = validators.validate_coment(comment)

    if error_message:
        return jsonify({"status": 400, 'error': error_message}), 400
    elif redflag.edits_record_location(redflag_id, 'comment', comment):
        return jsonify({"status": 201, "data": redflag.edits_record_location(redflag_id, 'comment', comment)})
    return jsonify({"status": 200, "message": "the redflag with redflag_id is not available"})


@app.route('/api/v1/red-flags/<int:redflag_id>/redflag', methods=['DELETE'])
# @jwt_required
def delete_redflag(redflag_id):
    # if redflag.delete_record(redflag_id):
    #     return jsonify ({"status":200, "data":[{"id":redflag_id, "message":"redflag has been successfully deleted"}]})
    #     # return jsonify({"status": 200, "data": redflag.delete_record(redflag_id)})
    # return jsonify(
    #     {"status": 204,
    #      "message": "redflag with that redflag_id is not available"})
    return redflag.delete_record(redflag_id)