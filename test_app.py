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

    def tearDown(self):
        # executed after each test
        pass

    def test_post_movie_error(self):
        new_movie_json = {'title': 'movie test title 1', 'release_date': '22-02-2022'}
        res = self.client().post('/movies', json = new_movie_json)
        self.assertEqual(res.status_code, 401)
    
    def test_post_movie_success(self):
        new_movie_json = {'title': 'movie test title 1', 'release_date': '22-02-2022'}
        res = self.client().post(
            '/movies', 
            headers = {
                'Authorization': 'Bearer ' + self.token_executive_producer
            },
            json = new_movie_json
        )
        self.assertEqual(res.status_code, 200)

if __name__ == "__main__":
    unittest.main()
