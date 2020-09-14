from models import Capability
from flask import Blueprint, jsonify, request, abort
from util import Util

capability_endpoint = Blueprint('capability_endpoint',
                                __name__)

# A GET endpoint to get all the capabilities
@capability_endpoint.route('/capabilities', methods=['GET'])
def get_all_capabilities():
    return Util.basic_get_request(Capability)

# A POST endpoint to create a new capability
@capability_endpoint.route('/capabilities', methods=['POST'])
def create_resource():
    body = Util.get_body(request)

    number = body.get('number')
    name = body.get('name')
    size = body.get('size')
    status = body.get('status')
    length = body.get('length')
    dependency = body.get('dependency')
    new_capability = Capability(number, name, size,
                                status, length, dependency)
    return Util.basic_post_request(new_capability)

# A DELETE endpoint to delete a capability
@capability_endpoint.route('/capabilities/<capability_id>', 
                         methods=['DELETE'])
def delete_project(capability_id):
    return Util.basic_delete_request(Capability, 
                                        capability_id)