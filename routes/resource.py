from models.resource_model import ResourceManagement
from flask import Blueprint, jsonify, request, abort
from util import Util

resource_endpoint = Blueprint('resource_endpoint',
                                __name__)

# A GET endpoint to get all the resources
@resource_endpoint.route('/resources', methods=['GET'])
def get_all_capabilities():
    return Util.basic_get_request(ResourceManagement)


# A POST endpoint used to create new resources
@resource_endpoint.route('/resources', methods=['POST'])
def create_resource():
    body = Util.get_body(request)

    projectName = body.get('projectName')
    duration = body.get('duration')
    resourceName = body.get('resourceName')
    status = body.get('status')
    updatedDate = body.get('updatedDate')
    new_resource = ResourceManagement(projectName, duration,
                                      resourceName,
                                      status, updatedDate)

    return Util.basic_post_request(new_resource)

# A DELETE endpoint used to delete a resource 
@resource_endpoint.route('/resources/<resource_id>', 
                         methods=['DELETE'])
def delete_project(resource_id):
    return Util.basic_delete_request(ResourceManagement, 
                                        resource_id)