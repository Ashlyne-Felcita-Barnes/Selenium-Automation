from selenium import webdriver  
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By  

# Path to your ChromeDriver  
service = Service("C:\\Users\\HP\\OneDrive\\Desktop\\chromedriver.exe")  
driver = webdriver.Chrome(service=service)
driver.get('https://www.microdegree.work/')  
#driver.find_element(By.LINK_TEXT,'Login').click()
driver.find_element(By.PARTIAL_LINK_TEXT,'Log').click()

input("Press Enter to close the browser...")