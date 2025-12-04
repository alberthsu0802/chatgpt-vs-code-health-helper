# tests/test_health.py
import unittest
from app import app
import json

class HealthTrackerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_health_advice(self):
        user_data = {
            "age": 28,
            "gender": "female",
            "height": 1.65,
            "weight": 58,
            "target": "減脂",
            "exercise_frequency": 3
        }

        response = self.app.post('/health', data=json.dumps(user_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        response_json = json.loads(response.data)
        self.assertIn("bmi", response_json)
        self.assertIn("diet_advice", response_json)
        self.assertIn("exercise_advice", response_json)

if __name__ == '__main__':
    unittest.main()
