import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service 

class PageTitleTest(unittest.TestCase):
    def test1_goopt(self):
        service = Service("C:\\Users\\HP\\OneDrive\\Desktop\\chromedriver.exe")  
        self.driver=webdriver.Chrome(service=service)
        self.driver.get('https://www.google.com/')
        print('Title is'+ self.driver.title)


    def test1_yaho(self):
        service = Service("C:\\Users\\HP\\OneDrive\\Desktop\\chromedriver.exe")  
        self.driver=webdriver.Chrome(service=service)
        self.driver.get('https://in.search.yahoo.com/?fr2=inr')
        print('Title is'+ self.driver.title)


if __name__  =="__main__":
    unittest.main()