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

    return jsonify({"status": 201, 'data': redflag.get_allredflags()}), 201


@app.route('/api/v1/red-flags/<int:redflag_id>', methods=['GET'])
def get_sepecific_record(redflag_id):
    return redflag.get_a_redflag(redflag_id), 200


@app.route('/api/v1/red-flags', methods=['POST'])
def add_parcels():
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
def edist_location(redflag_id):
    """
    method for editing location of a single redflag
    """
    oneredflag = redflag.edit_redflag(redflag_id)
    if oneredflag:
        oneredflag[0]['location'] = request.json.get(
            'location', oneredflag[0]['location'])
    if oneredflag[0]['location']:
        return jsonify({"status": 200, "data": [{"redflag_id": redflag_id, "message": "Updated redflag's location"}]}), 200
    return jsonify({"status": 404, "error": "no incident with such an id"}), 404

@app.route("/api/v1/red-flags/<redflag_id>/comment", methods=["PATCH"])
def edit_location(redflag_id):
    """a user can use this route to edit the comment of a particular\
    redflag record"""
    data = request.get_json()

    comment = data.get('comment')
    newrecord = redflag.edit_record_comments(redflag_id, comment)
    return newrecord

@app.route('/api/v1/red-flags/<int:redflag_id>/locations', methods=['PATCH'])
def edit_locations(redflag_id):
    """
    route for editing location of a single redflag
    """
    edit_redflag = redflag.edit_redflag(redflag_id)
    if edit_redflag:
        edit_redflag[0]['location'] = request.json.get(
            'location', edit_redflag[0]['location'])
    if edit_redflag[0]['location']:
        return jsonify({"status": 200, "data": [{"incident_id": redflag_id, "message": "Updated redflag's location"}]}), 200
    return jsonify({"status": 404, "error": "no incident with such an id"}), 404

@app.route('/api/v1/red-flags/<int:redflag_id>/comment', methods=['PATCH'])
def edit_comment(redflag_id):
    """
    Route where a user can edit the comment of a particular redfalg
    """
    edit_redflag = redflag.edit_redflag(redflag_id)
    if edit_redflag:
        edit_redflag[0]['comment'] = request.json.get(
            'comment', edit_redflag[0]['comment'])
    if edit_redflag[0]['comment']:
        return jsonify({"status": 200, "data": [{"redflag_id": redflag_id, "message": "Updated redflag's comment"}]}), 200
    return jsonify({"status": 404, "error": "no redflag_id with such an id"}), 404

@app.errorhandler(405)
def url_not_found(error):
    return jsonify({'message':'Requested method not allowed, try a different method'}), 405

@app.errorhandler(404)
def page_not_found(error):
    return jsonify({'message':'page not found on server, check the url'}), 404

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({'message':'internal server error, check the inputs'}), 500