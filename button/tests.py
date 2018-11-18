from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

# Create your tests here.
class ButtonTest(StaticLiveServerTestCase):

	def setUp(self):
		self.driver = webdriver.Chrome()
		
	def test_button(self):
		driver = self.driver
		driver.get("%s%s" % (self.live_server_url, "/button/"))
		driver.find_element_by_id("greeting").click()
		assert "...world!" in driver.find_element_by_id("showit").text
		
	def tearDown(self):
		self.driver.close()