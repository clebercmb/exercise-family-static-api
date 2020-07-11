"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for,json 
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members2', methods=['GET'])
def handle_hello():

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    response_body = {
        "hello": "world",
        "family": members
    }


    return jsonify(response_body), 200

@app.route('/members', methods=['GET'])
def getMembers():

    members = jackson_family.get_all_members()

    return jsonify(members), 200

@app.route('/member', methods=['POST'])
def addMember():
    print('==> appy.addMember:')
    request_body = request.data
    decode_object = json.loads(request_body)

    newMember=jackson_family.add_member(decode_object)

    return jsonify(newMember), 200

@app.route('/member/<int:id>', methods=['GET'])
def getMember(id):
    print('==> appy.getMember')
    print('id_member=', id)
    member = jackson_family.get_member(id)

    return jsonify(member), 200


@app.route('/member/<int:id_member>', methods=['DELETE'])
def deleteMember(id_member):
    print('==> appy.deleteMember')
    print('id_member=', id_member)
    jackson_family.delete_member(id_member)

    return jsonify({'done':True}), 200




# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(port=PORT, debug=True)
