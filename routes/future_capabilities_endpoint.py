from models.future_capabilities import Future_Capabilities
from flask import Blueprint, jsonify, request, abort
from request_util import Request_Util

future_capabilities_endpoint = Blueprint('future_capabilities_endpoint',
                                __name__)

# A GET endpoint to get all the future capabilities
@future_capabilities_endpoint.route('/future_capabilities', 
                                    methods=['GET'])
def get_all_future_capabilities():
    return Request_Util.basic_get_request(Future_Capabilities)

# A POST endpoint to create a new future capability
@future_capabilities_endpoint.route('/future_capabilities', methods=['POST'])
def create_future_capability():
    body = Request_Util.get_body(request)

    points = body.get('points')
    size = body.get('size')
    capabilities_count = body.get('capabilities_count')
    new_future_capability = Future_Capabilities(points, size,
                                                capabilities_count)
    return Request_Util.basic_post_request(new_future_capability)

# A PATCH endpoint to update the future capability
@future_capabilities_endpoint.route('/future_capabilities/<fut_cap_id>', 
                                    methods=['PATCH'])
def edit_future_capability(fut_cap_id):
    future_capability = Future_Capabilities.query.filter(
        Future_Capabilities.id == fut_cap_id).one_or_none()
    body = Request_Util.get_body(request)
    
    if body.get('points') is not None:
        future_capability.points = body.get('points')
    if body.get('size') is not None:
        future_capability.size = body.get('size')
    if body.get('capabilities_count') is not None:
        future_capability.capabilities_count = body.get('capabilities_count')

    return Request_Util.basic_patch_request(future_capability)

# A DELETE endpoint to delete a future capability
@future_capabilities_endpoint.route('/future_capabilities/<fut_cap_id>', 
                                    methods=['DELETE'])
def delete_future_capability(fut_cap_id):
    return Request_Util.basic_delete_request(Future_Capabilities, 
                                        fut_cap_id)
