import unittest
from unittest import TestCase
from selenium import webdriver


class TestSelenium(TestCase):


    def test_page_title(self):
        self.assertEqual(2,2)

    
if __name__ == "__main__":
    unittest.main(verbosity=2)
