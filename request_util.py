from flask import jsonify, abort
from models.models import Basic_Model

"""
    A Util Class which handles basic HTTP Requests operations.
"""
class Request_Util(): 

    """
        A GET endpoint
        returns all the domain items from the database
        of the query type passed
    """
    @staticmethod
    def basic_get_request(query_type: Basic_Model):
        items = query_type.query.all()
        return jsonify({
            'success': True,
            'items': [item.format() for item in items] 
        })
        
    # A DELETE endpoint used to delete an item
    @staticmethod
    def basic_delete_request(query_type: Basic_Model, item_id):
        item = query_type.query.filter(
            query_type.id == item_id).one_or_none()
        if(item is None):
            abort(404)

        try:
            item.delete()
            return jsonify({
                'success': True,
                'deleted': item_id,
            })
        except Exception as e:
            print(e)
            abort(422)

    '''
        Gets the json body for the request.
        If there is no json, then it throws an error.
    '''
    @staticmethod
    def get_body(request):
        body = request.get_json()
        if body is None:
            abort(400)
        return body

    # A POST endpoint used to create an item
    @staticmethod
    def basic_post_request(new_item: Basic_Model):
        try:
            new_item.insert()
            return jsonify({
                'success': True,
                'created': new_item.id,
            })
        except Exception as e:
            print(e)
            abort(422)
    
    # Handles basic patch requests
    @staticmethod
    def basic_patch_request(new_item: Basic_Model):
        try:
            new_item.update()
            return jsonify({
                'success': True,
                'updated': new_item.id,
            })
        except Exception as e:
            print(e)
            abort(422)