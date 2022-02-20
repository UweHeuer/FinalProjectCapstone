import unittest
import json
import os
from app import create_app

from models import setup_db, Movie, Actor

class CapstoneTestCase(unittest.TestCase):

    def setUp(self):
        # define test variables and set up
        self.app = create_app()
        self.client = self.app.test_client
        self.token_executive_producer = os.getenv('EP')
        self.token_casting_assistant = os.getenv('CA')

    def tearDown(self):
        # executed after each test
        pass


    def test_get_movies_success(self):
        res = self.client().get(
            'movies',
            headers = {
                'Authorization': 'Bearer ' + self.token_executive_producer
            }
        )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue('movies' in data)        


    def test_get_movies_invalid_token(self):
        res = self.client().get(
            'movies',
            headers = {
                'Authorization': 'Bearer ' + 'abcdefg'
            }
        )
        self.assertEqual(res.status_code, 401)


    def test_post_movie_missing_token(self):
        new_movie_json = {
            'title': 'movie test title 1', 
            'release_date': '22-02-2022'
        }
        res = self.client().post('/movies', json = new_movie_json)
        self.assertEqual(res.status_code, 401)


    def test_post_movie_success(self):
        new_movie_json = {
            'title': 'movie test title 1', 
            'release_date': '22-02-2022'
        }
        res = self.client().post(
            '/movies', 
            headers = {
                'Authorization': 'Bearer ' + self.token_executive_producer
            },
            json = new_movie_json
        )
        self.assertEqual(res.status_code, 200)


    def test_update_movie_success(self):
        # create movie for testing
        test_movie = Movie(title = 'test for update', release_date = '22-02-2022')
        test_movie.insert()

        update_movie_json = {
            'title': 'patched title',
            'release_date': '31-12-2099'
        }

        res = self.client().patch(
            '/movies/{}'.format(test_movie.id),
            headers = {
                'Authorization': 'Bearer ' + self.token_executive_producer
            },  
           json = update_movie_json,                     
        )

        self.assertEqual(res.status_code, 200)

        # clean up
        test_movie.delete()


    def test_update_movie_wrong_id(self):

        update_movie_json = {
            'title': 'patched title',
            'release_date': '31-12-2099'
        }

        res = self.client().patch(
            '/movies/{}'.format(99999),
            headers = {
                'Authorization': 'Bearer ' + self.token_executive_producer
            },  
           json = update_movie_json,                     
        )              

        self.assertEqual(res.status_code, 404)  


    def test_update_movie_missing_rights(self):
        # create movie for testing
        test_movie = Movie(title = 'test for update', release_date = '22-02-2022')
        test_movie.insert()      

        update_movie_json = {
            'title': 'patched title',
            'release_date': '31-12-2099'
        }

        res = self.client().patch(
            '/movies/{}'.format(test_movie.id),
            headers = {
                'Authorization': 'Bearer ' + self.token_casting_assistant
            },  
           json = update_movie_json,                     
        )

        self.assertEqual(res.status_code, 401)

        # clean up
        test_movie.delete()        


    def test_delete_movie_success(self):
        # create movie for testing
        test_movie = Movie(title = 'test for delete', release_date = '22-02-2022')
        test_movie.insert()      

        res = self.client().delete(
            '/movies/{}'.format(test_movie.id),
            headers = {
                'Authorization': 'Bearer ' + self.token_executive_producer
            }                  
        )

        self.assertEqual(res.status_code, 200)    


    def test_delete_movie_missing_rights(self):
        # create movie for testing
        test_movie = Movie(title = 'test for delete', release_date = '22-02-2022')
        test_movie.insert()      

        res = self.client().delete(
            '/movies/{}'.format(test_movie.id),
            headers = {
                'Authorization': 'Bearer ' + self.token_casting_assistant
            }                  
        )

        self.assertEqual(res.status_code, 401)

        # clean up
        test_movie.delete() 


    def test_get_actors_success(self):
        res = self.client().get(
            'actors',
            headers = {
                'Authorization': 'Bearer ' + self.token_executive_producer
            }
        )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue('actors' in data)        


    def test_get_actors_invalid_token(self):
        res = self.client().get(
            'actors',
            headers = {
                'Authorization': 'Bearer ' + 'uhgcfg'
            }
        )
        self.assertEqual(res.status_code, 401)


    def test_post_actor_missing_token(self):
        new_actor_json = {
            'name': 'actor test name', 
            'gender': 'M',
            'age': '22'
        }
        res = self.client().post('/actors', json = new_actor_json)
        self.assertEqual(res.status_code, 401)


    def test_post_actor_success(self):
        new_actor_json = {
            'name': 'actor test name', 
            'gender': 'M',
            'age': '22'
        }
        res = self.client().post(
            '/actors', 
            headers = {
                'Authorization': 'Bearer ' + self.token_executive_producer
            },
            json = new_actor_json
        )
        self.assertEqual(res.status_code, 200)


    def test_update_actor_success(self):
        # create actor for testing
        test_actor = Actor(name = 'test for update', gender = 'F', age = '2')
        test_actor.insert()

        update_actor_json = {
            'name': 'patched name',
            'gender': 'M',
            'age': '22'
        }

        res = self.client().patch(
            '/actors/{}'.format(test_actor.id),
            headers = {
                'Authorization': 'Bearer ' + self.token_executive_producer
            },  
           json = update_actor_json,                     
        )

        self.assertEqual(res.status_code, 200)

        # clean up
        test_actor.delete()


    def test_update_actor_wrong_id(self):

        update_actor_json = {
            'name': 'patched name',
            'gender': 'M',
            'age': '22'
        }

        res = self.client().patch(
            '/actors/{}'.format(99999),
            headers = {
                'Authorization': 'Bearer ' + self.token_executive_producer
            },  
           json = update_actor_json,                     
        )              

        self.assertEqual(res.status_code, 404)  


    def test_update_actor_missing_rights(self):
        # create actor for testing
        test_actor = Actor(name = 'test for update', gender = 'F', age = '2')
        test_actor.insert()   

        update_actor_json = {
            'name': 'patched name',
            'gender': 'M',
            'age': '22'
        }

        res = self.client().patch(
            '/actors/{}'.format(test_actor.id),
            headers = {
                'Authorization': 'Bearer ' + self.token_casting_assistant
            },  
           json = update_actor_json,                     
        )

        self.assertEqual(res.status_code, 401)

        # clean up
        test_actor.delete()        


    def test_delete_actor_success(self):
        # create actor for testing
        test_actor = Actor(name = 'test for update', gender = 'F', age = '2')
        test_actor.insert()      

        res = self.client().delete(
            '/actors/{}'.format(test_actor.id),
            headers = {
                'Authorization': 'Bearer ' + self.token_executive_producer
            }                  
        )

        self.assertEqual(res.status_code, 200)    


    def test_delete_actor_missing_rights(self):
        # create actor for testing
        test_actor = Actor(name = 'test for update', gender = 'F', age = '2')
        test_actor.insert()      

        res = self.client().delete(
            '/actors/{}'.format(test_actor.id),
            headers = {
                'Authorization': 'Bearer ' + self.token_casting_assistant
            }                  
        )

        self.assertEqual(res.status_code, 401)

        # clean up
        test_actor.delete()        

if __name__ == "__main__":
    unittest.main()
