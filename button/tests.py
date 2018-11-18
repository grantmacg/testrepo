from django.test import TestCase

# Create your tests here.
def test_button(self):
	response = sel.client.get('/button/')
	self.assertEqual(response.status_code, 200)