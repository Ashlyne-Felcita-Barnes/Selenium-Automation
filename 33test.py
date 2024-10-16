import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service 



class Micro(unittest.TestCase):
    def test_microo(self):
        list=['Mango','Cherry',"Kiwi","Apple"]
        
        self.assertGreater(1,10)
        self.assertGreaterEqual(9,90)
        self.assertLess(1,10)
        self.assertLessEqual(9,90)
        

   


if __name__  =="__main__":
    unittest.main()