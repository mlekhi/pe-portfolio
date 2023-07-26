# tests/test_app.py

import unittest
import os
os.environ['TESTING'] = 'true'

from app import app

class AppTestCase(unittest.TestCase):
        def setUp(self):
                self.client = app.test_client()

        def test_home(self):
                response = self.client.get("/")
                assert response.status_code == 200
                html = response.get_data(as_text=True)
                assert "<title>Maya Lekhi</title>" in html
                # TODO Add more tests relating to the home page
                assert "<img" in html
                
        
        def test_timeline(self):
                response = self.client.get("/api/timeline_post")
                assert response.status_code == 200
                assert response.is_json
                json = response.get_json()

                assert "timeline_post" in json
                assert len(json["timeline_post"]) == 0
  
        # TODO Add more tests relating to the /api/timeline_post GET and POST apis 
        def test_get(self):
                response = self.client.get("/api/timeline_post")
                assert response.status_code == 200

        def test_post(self):
                 data = {
                        'name': 'John Doe',
                        'email': 'john@example.com',
                        'content': "Hello world, I'm John!"}
                response = self.client.post("/api/timeline_post", json=data)
                assert response.status_code == 201

        # TODO Add more tests relating to the timeline page
        def test_timeline_access(self):
                response = self.client.get("/timeline")
                assert response.status_code == 200

