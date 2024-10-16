import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service 



class Micro(unittest.TestCase):
    def test_micro(self):
        service = Service("C:\\Users\\HP\\OneDrive\\Desktop\\chromedriver.exe")  
        driver = webdriver.Chrome(service=service)
        driver.get('https://www.microdegree.work/')  
        pagettle=driver.title
        self.assertEqual('MicroDegree',pagettle,"Incorrect")
        self.assertNotEqual('MicroDegre',pagettle,'Correct')

   


if __name__  =="__main__":
    unittest.main()