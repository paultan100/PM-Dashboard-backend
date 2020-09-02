from flask import Flask, request, abort, jsonify
from flask_cors import CORS
from models import ResourceManagement, setup_db, db
from flask_migrate import Migrate


def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app)
    Migrate(app, db)

    '''
        The after_request decorator to set Access-Control-Allow
    '''
    @app.after_request
    def after_request(response):
        response.headers.add(
            'Access-Control-Allow-Methods',
            'GET,POST,PATCH,DELETE,OPTIONS'
        )
        return response

    '''
        Gets the json body for the request.
        If there is no json, then it throws an error.
    '''
    def get_body(request):
        body = request.get_json()
        if body is None:
            abort(400)
        return body

    @app.route('/')
    def home():
        return 'Hello!'

    # A GET endpoint to get all the blog posts
    @app.route('/resources', methods=['GET'])
    def get_all_projects():
        resources = ResourceManagement.query.all()
        return jsonify({
            'success': True,
            'projects': [resource.format() for resource in resources]
        })

    # A POST endpoint used to create new blog posts.
    @app.route('/resources', methods=['POST'])
    def create_project():
        body = get_body(request)

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

    # A DELETE endpoint used to delete blog posts
    @app.route('/resources/<resource_id>', methods=['DELETE'])
    def delete_project(resource_id):
        resource = ResourceManagement.query.filter(
            ResourceManagement.id == resource_id).one_or_none()
        if(resource is None):
            abort(404)

        try:
            resource.delete()
            return jsonify({
                'success': True,
                'deleted': resource_id,
            })
        except Exception as e:
            print(e)
            abort(422)

    @app.errorhandler(400)
    def bad_request(error):
        return handle_error(400, 'Bad request')

    @app.errorhandler(404)
    def not_found(error):
        return handle_error(404, 'Not found')

    @app.errorhandler(422)
    def unprocessable_entity(error):
        return handle_error(422, 'Unprocessable entity')

    def handle_error(code, message):
        return jsonify({
            'success': False,
            'error': code,
            'message': message
        }), code

    return app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True, )
