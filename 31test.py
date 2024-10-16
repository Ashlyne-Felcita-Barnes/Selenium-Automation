import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service 



class Micro(unittest.TestCase):
    def test_microo(self):
        list=['Mango','Cherry',"Kiwi","Apple"]
        
        #self.assertIn("Manmgo",list)
        self.assertNotIn("Mango",list)
        

   


if __name__  =="__main__":
    unittest.main()