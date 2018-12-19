import flask, functools
from flask import jsonify, make_response





def validate_data(key):
    if not key or key.isspace():
        return True

def validate_data_length(key):
    if len(str(key)) < 13:
        return True