from models.scope_model import Scope
from flask import Blueprint, jsonify, request, abort
from request_util import Request_Util

scope_endpoint = Blueprint('scope_endpoint',
                                __name__)

# A GET endpoint to get all the scopes
@scope_endpoint.route('/scopes', methods=['GET'])
def get_all_scopes():
    return Request_Util.basic_get_request(Scope)

# A POST endpoint used to create the scope objects in the 
# scope table
@scope_endpoint.route('/scopes', methods=['POST'])
def create_scopes():
    body = Request_Util.get_body(request)
    points = body.get('points')

    if points is None:
        abort(422)

    # Delete all items from the table
    Scope.query.delete()

    small = current_small = 2
    average = current_average = 4
    large = current_large = 6
    total_weeks = 9
    
    # This does not include the final week, which has
    # special logic aruond it.
    for x in range(1, total_weeks):
        if not small * x > points:
            current_small = small * x
        else:
            current_small = points

        if not average * x > points:
            current_average = average * x
        else: 
            current_average = points 
        
        if not large * x > points:
            current_large = large * x
        else:
            current_large = points
        
        Scope(x, current_small, current_average, 
              current_large, points).insert()
    
    # Add one more datapoint 
    Scope(total_weeks, current_small, current_average, 
              current_large, points).insert()

    return jsonify({
        'success': True,
        'number of created scopes': total_weeks
    })
    