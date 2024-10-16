from selenium import webdriver  
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By  

# Path to your ChromeDriver  
service = Service("C:\\Users\\HP\\OneDrive\\Desktop\\chromedriver.exe")  
driver = webdriver.Chrome(service=service)
driver.get('https://www.zoho.com/forms/?zredirect=f')  
driver.find_element(By.CSS_SELECTOR,'input#portalcompanyname').send_keys('Ashlyn')
driver.find_element(By.CSS_SELECTOR,'input#email').send_keys('Ashlyn')
input("Press Enter to close the browser...")

