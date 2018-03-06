import os
import flaskr
import unittest
import tempfile

class FlaskrTestCase(unittest.TestCase):
    #create a new test client & init new db
    def setUp(self):
        self.db_fd,flaskr.app.config['DATABASE'] = tempfile.mkstemp()
        flaskr.app.testing = True #disable error catching
        self.app = flaskr.app.test_client()

        with flaskr.app.app_context():
            flaskr.initdb()

    # delete database after the test
    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(flaskr.app.config['DATABASE'])

    #first test
    def test_empty_db(self):
        rv = self.app.get('/')
        assert(b'No entries here so far') in rv.data

if __name__ == '__main__':
    unittest.main()
