import json
import os
from flask import Flask, jsonify, request, abort
from models import Movie, Actor, setup_db
from flask_cors import CORS

from auth import AuthError, requires_auth

def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.route('/')
    def root():
        return "Hi there - this is my final Udacity Nanodegree project!"

    @app.route('/login')
    def login():
        return "You proabably have been redirected here because you loogged on via the Auth0 code flow"

    @app.route('/logout')
    def logout():
        return "You proabably have been redirected here because you loogged out via the Auth0 code flow"
        
    #
    # define endpoints for movies
    #

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
    # define endpoints for actors
    #

    # get actors
    @app.route('/actors', methods = ['GET'])
    @requires_auth('get:actors')
    def get_actors(payload):
        try:
            actors = Actor.query.all()
            return jsonify({
                'success': True,
                'actors': [actor.format() for actor in actors]
            }), 200
        except:
            # something went wrong => return internal error
            abort(500)            


    # create actor
    @app.route('/actors', methods = ['POST'])
    @requires_auth('post:actors')    
    def post_actors(payload):
        actor_data = request.get_json()
        if 'name' and 'age' and 'gender' not in actor_data:
            # bad request
            abort(400)
        try:
            new_actor = Actor(name = actor_data['name'], age = actor_data['age'], gender = actor_data['gender'])
            new_actor.insert()

            return jsonify({
                'success': True,
                'actor_id': new_actor.id
            })
        except:
            # something went wrong => return internal error
            abort(500)


    # update actor
    @app.route('/actors/<int:id>', methods = ['PATCH'])
    @requires_auth('patch:actors')
    def patch_actors(payload, id):

        actor = Actor.query.get(id)
        if actor is None:
            # not found
            abort(404)

        try:
            actor_data = request.get_json()
            if 'name' in actor_data:
                actor.name = actor_data['name']
            if 'age' in actor_data:
                actor.age = actor_data['age']
            if 'gender' in actor_data:
                actor.age = actor_data['gender']

            actor.update()

            return jsonify({
                'success': True,
                'actor_id': actor.id
            }), 200

        except:
            # something went wrong => return internal error
            abort(500)            


    @app.route('/actors/<int:id>', methods = ['DELETE'])
    @requires_auth('delete:actors')
    def delete_actors(payload, id):

        actor = Actor.query.get(id)
        if actor is None:
            # not found
            abort(404)

        try:
            actor.delete()    
            return jsonify({
                'success': True,
                'actor_id': id
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
