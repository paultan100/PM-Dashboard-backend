from models import ResourceManagement
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

    try:
        new_resource = ResourceManagement(projectName, duration,
                                            resourceName,
                                            status, updatedDate)
        new_resource.insert()
        return jsonify({
            'success': True,
            'created': new_resource.id,
        })
    except Exception as e:
        print(e)
        abort(422)

@resource_endpoint.route('/resources/<resource_id>', 
                         methods=['DELETE'])
def delete_project(resource_id):
    return Util.basic_delete_request(ResourceManagement, 
                                        resource_id)