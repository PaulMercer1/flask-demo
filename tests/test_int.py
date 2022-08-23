from flask_testing import LiveServerTestCase
from urllib.request import urlopen
from flask import url_for

from application import app, db
from application.models import Games

class TestBase(LiveServerTestCase):
    TEST_PORT = 5050 # test port, doesn't need to be open

    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///",
            LIVESERVER_PORT=self.TEST_PORT,            
            DEBUG=True,
            TESTING=True
        )
        return app

def setUp(self):
        db.create_all() # create schema before we try to get the page
class TestAdd(TestBase):
   
    def test_index_route(self):
        response = app.test_client().get('/')

        assert response.status_code == 200
