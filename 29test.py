import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service 



class Micro(unittest.TestCase):
    def test_microo(self):
        service = Service("C:\\Users\\HP\\OneDrive\\Desktop\\chromedriver.exe")  
        driver = webdriver.Chrome(service=service)
        driver.get('https://www.microdegree.work/')  
        pagettle=driver.title
        self.assertTrue('MicroDegree'==pagettle,"Incorrect")
        self.assertFalse('MicroDegree'==pagettle,'Correct')

   


if __name__  =="__main__":
    unittest.main()