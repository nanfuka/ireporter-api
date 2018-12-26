from flask import Flask, jsonify, request
from validations import validate_data, validateprescence

app = Flask(__name__)

# methods = Methods()
"""index route"""
@app.route('/')
def index():
    return jsonify({"status": 200, "message": "Wtrialsp"}),200
@app.route('/api', methods=['POST'])
def creates_red_flag():
    red_flag = request.get_json()
    name = red_flag.get('name')
    religion = red_flag.get('religion')
    
    validkey = validate_data('name', red_flag.keys())
    if validkey:
        return validkey

    
    validate = validateprescence(name)
    if validate:
        return validate


    return jsonify({"name":"my sweet girls"})

if __name__ == '__main__':
    app.run(debug = True) 
        
