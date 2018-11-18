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
		print(driver.page_source.encode("utf-8"))
		driver.find_element_by_id("greeting").click()
		elem = driver.find_element_by_id("showit")
		assert "...world!" in elem
		
	def tearDown(self):
		self.driver.close()