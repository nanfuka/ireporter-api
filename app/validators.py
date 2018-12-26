from flask import Flask, jsonify, make_response, request
def validate_data(username):
    if not username or username.isspace() or len(username)<2 or len(username)>24:
        return jsonify({"status":404, "message":"please enter all items"}), 404
def validate_data_type(username):
    if not type(username) == str:
        return 'status must be an String!!'

def validate_intdata_type(numbers):
    if not type(numbers) == int:
        return 'status must be a number!!'

def validate_keys(value, lst):
    if value not in lst:
        return jsonify({"status":404, "message":"field must be present"}), 404

def input_jsonformat(data):
    if not type(data) == dict:
        return jsonify({
            "message":'Data must be in dictionary format',
            "required format":{"userid": "int", "weight": "float",
                "status":"string","destination":"string","pickup":"string"}
            }), 400
