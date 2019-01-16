from flask import Flask, jsonify, request, json
# from flasgger import Swagger, swag_from
from app.controllers.incident_cont import Redflag
from app.controllers.users_controllers import User
from app.models.incident import Incident, incidents
from flask_jwt_extended import create_access_token, JWTManager, jwt_required, get_jwt_identity

# from app.models.users import User, users

app = Flask(__name__)
jwt = JWTManager(app)
app.config['JWT_SECRET_KEY'] = 'thisismysecret'
redflag = Redflag()


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
    error_message = redflag.validate_user_details(firstname, lastname, email, username, password, phoneNumber, isAdmin, othernames)
    if error_message:
        return jsonify({"status": 404, 'error': error_message}), 404
    elif invalid_detail:
        return jsonify({"status": 404, 'error': invalid_detail}), 404
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
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    user = User()
    loggedin_user = user.login(username, password)

    if loggedin_user:
        token = create_access_token(username)
        return jsonify(loggedin_user, {"access_token": token})
    else:
        return jsonify({"status": 404, "error": "user with such credentials does not exist"}), 404


@app.route('/api/v1/red-flags')
# @jwt_required
def get_redflags():
    """ A user can retrieve all redflag records\
    only after including the bearer token in the header
    """
    return redflag.get_allredflags()


@app.route('/api/v1/red-flags/<int:redflag_id>', methods=['GET'])
@jwt_required
def get_sepecific_record(redflag_id):
    """route to rertieve a redflag at a specific route"""
    return redflag.get_a_redflag(redflag_id), 200


@app.route('/api/v1/red-flags', methods=['POST'])
def create_redflags():
    """A user can create a redflag by entering all the required data"""
    data = request.get_json()
    createdby = data.get('createdby')
    location = data.get('location')
    comment = data.get('comment')
    incident_type = data.get('incident_type')
    # intervention = data.get('intervention')
    status = data.get('status')
    images = data.get('images')
    videos = data.get('videos')
    redflag = Redflag()
    error_message = redflag.validate_input(
        createdby, incident_type, status)
    wrong_location = redflag.validate_location(location)
    if wrong_location:
        return jsonify({"status": 404, 'error': wrong_location}), 404
    elif error_message:
        return jsonify({"status": 404, 'error': error_message}), 404
    new_incident = redflag.create_redflag(
        data['createdby'],
        data['incident_type'],
        data['location'],
        data['status'],
        # data['intervention'],
        data['images'],
        data['videos'],
        data['comment'])

    return jsonify({
        "status": 201, "id": new_incident['redflag_id'],
        "message": "Added a new incident", "data": new_incident}), 201


@app.route('/api/v1/red-flags/<int:redflag_id>/location', methods=['PATCH'])
@jwt_required
def edit_location(redflag_id):
    """
    using this route a user can modify the location of a single redflag
    """
    data = request.get_json()
    location = data.get('location')
    wrong_location = redflag.validate_location(location)
    if wrong_location:
        return jsonify({"status": 404, 'error': wrong_location}), 404
    # return redflag.edits_record_location(redflag_id, 'location', location), 200

    return redflag.edits_record_location(redflag_id, 'location', location)


@app.route('/api/v1/red-flags/<int:redflag_id>/comment', methods=['PATCH'])
@jwt_required
def edit_comment(redflag_id):

    # """
    # Route where a user can edit the comment of a particular redfalg
    # """
    data = request.get_json()
    comment = data.get('comment')

    error_message = redflag.validate_coment(comment)

    if error_message:
        return jsonify({"status": 404, 'error': error_message}), 404

    # incidents["comment"] =request.json.get(item, comment)
    # return redflag.edits_record_location(redflag_id, 'comment', comment)
    return redflag.edits_record_location(redflag_id, 'comment', comment)

# @app.errorhandler(405)
# def url_not_found(error):
#     return jsonify
#     ({
#         'message': 'Requested method not allowed, try a different method'
#     }), 405


# @app.errorhandler(404)
# def page_not_found(error):
#     return jsonify({'message': 'page not found on server, check the url'}), 404
