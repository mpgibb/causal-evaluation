import unittest
from fastapi.testclient import TestClient
from research.api import app
class ApiTests(unittest.TestCase):
 def test_health(self):
  with TestClient(app) as client:
   self.assertEqual(client.get('/health').json()['implementation'],'research_baseline')
 def test_unknown_payload_rejected(self):
  with TestClient(app) as client:
   self.assertEqual(client.post('/v1/baseline',json={'unexpected':'field'}).status_code,422)
 def test_valid_baseline(self):
  with TestClient(app) as client:
   response=client.post('/v1/baseline',json={'treated_before': 100, 'treated_after': 115, 'control_before': 90, 'control_after': 95})
   self.assertEqual(response.status_code,200)
   self.assertEqual(response.json()['contrast'],10.0)
