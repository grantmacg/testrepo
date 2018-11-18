from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Create your tests here.
class ButtonTest(TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome()
		
	def test_button(self):
		driver = self.driver
		driver.get("http://localhost:8000/button/")
		driver.find_element_by_id("greeting").click()
		elem = driver.find_element_by_id("showit")
		assert "...world!" in elem
		
	def tearDown(self):
		self.driver.close()