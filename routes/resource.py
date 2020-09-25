from models.resource_model import ResourceManagement
from flask import Blueprint, jsonify, request, abort
from request_util import Request_Util

resource_endpoint = Blueprint('resource_endpoint',
                                __name__)

# A GET endpoint to get all the resources
@resource_endpoint.route('/resources', methods=['GET'])
def get_all_capabilities():
    return Request_Util.basic_get_request(ResourceManagement)


# A POST endpoint used to create new resources
@resource_endpoint.route('/resources', methods=['POST'])
def create_resource():
    body = Request_Util.get_body(request)

    projectName = body.get('projectName')
    roles = body.get('roles')
    resourceName = body.get('resourceName')
    status = body.get('status')
    updatedDate = body.get('updatedDate')
    new_resource = ResourceManagement(projectName, roles,
                                      resourceName,
                                      status, updatedDate)

    return Request_Util.basic_post_request(new_resource)

# A DELETE endpoint used to delete a resource 
@resource_endpoint.route('/resources/<resource_id>', 
                         methods=['DELETE'])
def delete_project(resource_id):
    return Request_Util.basic_delete_request(ResourceManagement, 
                                        resource_id)