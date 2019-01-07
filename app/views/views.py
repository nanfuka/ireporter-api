from flask import Flask, jsonify, request, json
# from flasgger import Swagger, swag_from
from app.controllers.incident_cont import Redflag
from app.models.incident import Incident, incidents


app = Flask(__name__)
redflag = Redflag()


@app.route('/')
def index():
    """index url"""
    return jsonify({"status": 201, "message": "hi welcome to ireporter"})


@app.route('/api/v1/red-flags')
def get_redflags():
    """ A user can retrieve all redflag records """
    return redflag.get_allredflags()



@app.route('/api/v1/red-flags/<int:redflag_id>', methods=['GET'])
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
    redflags = data.get('redflags')
    intervention = data.get('intervention')
    status = data.get('status')
    images = data.get('images')
    videos = data.get('videos')
    redflag = Redflag()
    error_message = redflag.validate_input(
        createdby, location, redflags, intervention, status)
    if error_message:
        return jsonify({"status": 404, 'error': error_message}), 404
    new_incident = redflag.create_redflag(
        data['createdby'],
        data['location'],
        data['comment'],
        data['redflags'],
        data['intervention'],
        data['status'],
        data['images'],
        data['videos'])
    return jsonify({
        "status": 201, "id": new_incident['redflag_id'],
        "message": "Added a new incident", "data": new_incident}), 201


@app.route('/api/v1/red-flags/<int:redflag_id>/location', methods=['PATCH'])
def edit_location(redflag_id):
    # """
    # using this route a user can modify the location of a single redflag
    # """
    return redflag.edits_record_location(redflag_id, 'location')



@app.route('/api/v1/red-flags/<int:redflag_id>/comment', methods=['PATCH'])
def edit_comment(redflag_id):
    # """
    # Route where a user can edit the comment of a particular redfalg
    # """
    return redflag.edits_record_location(redflag_id, 'comment')


# @app.errorhandler(405)
# def url_not_found(error):
#     return jsonify
#     ({
#         'message': 'Requested method not allowed, try a different method'
#     }), 405


# @app.errorhandler(404)
# def page_not_found(error):
#     return jsonify({'message': 'page not found on server, check the url'}), 404
