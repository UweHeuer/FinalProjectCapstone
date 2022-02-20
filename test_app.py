import unittest
import json
import os
from app import create_app

from models import setup_db, Movie

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

        

if __name__ == "__main__":
    unittest.main()
