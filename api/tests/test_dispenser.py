import unittest
import json
from api.app import app


class TestBeerDispenserAPI(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_get_dispensers(self):
        response = self.app.get('/dispensers')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, dict)

    def test_get_dispenser(self):
        response = self.app.get('/dispensers/1')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, dict)
        self.assertEqual(data['name'], "Tap 1")

    def test_get_nonexistent_dispenser(self):
        response = self.app.get('/dispensers/100')
        self.assertEqual(response.status_code, 404)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['error'], "Dispenser not found")

    def test_update_dispenser(self):
        data = {"status": "on"}
        response = self.app.put('/dispensers/1', json=data)
        self.assertEqual(response.status_code, 200)
        updated_dispenser = json.loads(response.get_data(as_text=True))
        self.assertEqual(updated_dispenser['status'], "on")


if __name__ == '__main__':
    unittest.main()