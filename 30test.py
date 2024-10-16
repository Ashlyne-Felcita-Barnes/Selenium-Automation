import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service 



class Micro(unittest.TestCase):
    def test_microo(self):
        service = Service("C:\\Users\\HP\\OneDrive\\Desktop\\chromedriver.exe")  
        driver = webdriver.Chrome(service=service)
        
       
        self.assertIsNone(driver)
        self.assertIsNotNone(driver)

   


if __name__  =="__main__":
    unittest.main()