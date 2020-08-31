import os
from flask import Flask, request, abort, jsonify, redirect
from flask_cors import CORS
from models import Blog, User, setup_db, db
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
            'Access-Control-Allow-Headers',
            'Content-Type, Authorization'
        )
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
    @app.route('/blogs', methods=['GET'])
    def get_all_blogs():
        blogs = Blog.query.all()
        return jsonify({
            'success': True,
            'blogs': [blog.format() for blog in blogs]
        })


    # A POST endpoint used to create new blog posts.
    @app.route('/blogs', methods=['POST'])
    @requires_auth('post:blogs')
    def create_blog():
        body = get_body(request)

        title = body.get('title')
        blog_body = body.get('body')
        author_id = body.get('author_id')

        try:
            new_blog = Blog(title, blog_body, author_id)
            new_blog.insert()

            return jsonify({
                'success': True,
                'created': new_blog.id,
            })
        except Exception as e:
            print(e)
            abort(422)


    # A DELETE endpoint used to delete blog posts
    @app.route('/blogs/<int:blog_id>', methods=['DELETE'])
    @requires_auth('delete:blogs')
    def delete_blog(blog_id):
        blog = Blog.query.filter(Blog.id == blog_id).one_or_none()
        if(blog is None):
            abort(404)

        try:
            blog.delete()
            return jsonify({
                'success': True,
                'deleted': blog_id,
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
    app.run(debug=True)
