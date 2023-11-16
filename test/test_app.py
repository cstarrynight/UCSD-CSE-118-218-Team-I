import unittest
import app as tested_app
import json

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        tested_app.app.config['TESTING'] = True
        self.app = tested_app.app.test_client()

    def test_get_endpoint(self):
        r = self.app.get('/')
        self.assertEqual(r.status_code, 405)

    def test_correct_post_api_endpoint(self):
        r = self.app.post('/',
                          content_type='application/json',
                          data=json.dumps({'bpm': 100, 'stress': 100}))
        
        self.assertEqual(r.json, {'status': 'ok'})
        self.assertEqual(r.status_code, 200)

if __name__ == '__main__':
    unittest.main()

    # python -m unittest