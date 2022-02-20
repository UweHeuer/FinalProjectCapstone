import json
import os
from flask import Flask, jsonify, request, abort
from models import Movie, setup_db
from flask_cors import CORS

from auth import AuthError, requires_auth

def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.route('/')
    def root():
        return "Hi there - this is my final Udacity Nanodegree project!"
        
    # get movies
    @app.route('/movies', methods = ['GET'])
    @requires_auth('get:movies')
    def get_movies(payload):
        try:
            movies = Movie.query.all()
            return jsonify({
                'success': True,
                'movies': [movie.format() for movie in movies]
            }), 200
        except:
            # something went wrong => return internal error
            abort(500)            


    # create movie
    @app.route('/movies', methods = ['POST'])
    @requires_auth('post:movies')    
    def post_movies(payload):
        movie_data = request.get_json()
        if 'title' and 'release_date' not in movie_data:
            # bad request
            abort(400)
        try:
            new_movie = Movie(title = movie_data['title'], release_date = movie_data['release_date'])
            new_movie.insert()

            return jsonify({
                'success': True,
                'movie_id': new_movie.id
            })
        except:
            # something went wrong => return internal error
            abort(500)


    # update movie
    @app.route('/movies/<int:id>', methods = ['PATCH'])
    @requires_auth('patch:movies')
    def patch_movies(payload, id):

        movie = Movie.query.get(id)
        if movie is None:
            # not found
            abort(404)

        try:
            movie_data = request.get_json()
            if 'title' in movie_data:
                movie.title = movie_data['title']
            if 'release_date' in movie_data:
                movie.release_date = movie_data['release_date']

            movie.update()

            return jsonify({
                'success': True,
                'movie_id': movie.id
            }), 200

        except:
            # something went wrong => return internal error
            abort(500)            


    @app.route('/movies/<int:id>', methods = ['DELETE'])
    @requires_auth('delete:movies')
    def delete_movies(payload, id):

        movie = Movie.query.get(id)
        if movie is None:
            # not found
            abort(404)

        try:
            movie.delete()    
            return jsonify({
                'success': True,
                'movie_id': id
            }), 200       

        except:         
            # something went wrong => return internal error
            abort(500) 

            
    #
    # define error handling
    #

    @app.errorhandler(AuthError)
    def authError(error):
        return jsonify({
            'success': False,
            'error': error.status_code,
            'message': error.error['description']
        }), error.status_code

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "bad request"
        }), 400

    @app.errorhandler(404)
    def notFound(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404

    return app

# create application
app = create_app()

if __name__ == '__main__':
    app.run()
