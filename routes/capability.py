from models import Capability
from flask import Blueprint, jsonify
from util import Util

capability_endpoint = Blueprint('capability_endpoint',
                                __name__)

# A GET endpoint to get all the capabilities
@capability_endpoint.route('/capabilities', methods=['GET'])
def get_all_capabilities():
    return Util.basic_get_request(Capability)