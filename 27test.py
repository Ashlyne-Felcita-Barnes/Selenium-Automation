import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service 



class Amazon(unittest.TestCase):
    @unittest.SkipTest


    def test1_account(self):
        print('account')

    @unittest.skip('not ready')

    def test2_orders(self):
        print('orders')


    @unittest.skipIf('link'=='link','link available')

    def test3_wishlist(self):
        print('wishlist')

    def test4_recommendation(self):
        print('recommendation')

    def test5_prime_membership(self):
        print('prime membership')


if __name__  =="__main__":
    unittest.main()