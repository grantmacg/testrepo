from django.test import TestCase

# Create your tests here.
def test_button(self):
	response = self.client.get('/button/')
	self.assertEqual(response.status_code, 200)