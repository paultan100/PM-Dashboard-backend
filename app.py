import os
from flask import Flask, request, abort, jsonify, redirect
from flask_cors import CORS
from models import Project, setup_db, db
from flask_migrate import Migrate


def create_app(test_config=None):

    app = Flask(__name__)
    #setup_db(app)
    CORS(app)
    #migrate = Migrate(app, db)

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
    @app.route('/projects', methods=['GET'])
    def get_all_projects():
        #projects = Project.query.all()
        projects = [Project('title', 10, 'Isaac'), Project('titel2', 3, 'Joe')]
        return jsonify({
            'success': True,
            'projects': [project.format() for project in projects]
        })


    # A POST endpoint used to create new blog posts.
    @app.route('/projects', methods=['POST'])
    def create_project():
        body = get_body(request)

        title = body.get('title')
        duration = body.get('duration')
        owner = body.get('owner')

        try:
            new_project = Project(title, duration, owner)
            # new_project.insert()

            return jsonify({
                'success': True,
                'created': new_project.id,
            })
        except Exception as e:
            print(e)
            abort(422)


    # A DELETE endpoint used to delete blog posts
    @app.route('/projects', methods=['DELETE'])
    def delete_project(project_id):
        #project = Project.query.filter(Project.id == project_id).one_or_none()
        # if(project is None):
            # abort(404)

        try:
            # project.delete()
            return jsonify({
                'success': True,
                'deleted': project_id,
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
