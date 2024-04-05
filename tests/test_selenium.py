from selenium import webdriver
from unittest  import TestCase


class TestSelenium(TestCase):
    def test_firefox(self):
        browser = webdriver.Firefox()
        browser.get('https://selenium.dev/')

        assert True
    