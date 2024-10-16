from selenium import webdriver  
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By  

# Path to your ChromeDriver  
service = Service("C:\\Users\\HP\\OneDrive\\Desktop\\chromedriver.exe")  
driver = webdriver.Chrome(service=service)
driver.get('https://tally.so/r/3ylqax?Course=ATS')  
driver.find_element(By.XPATH,'//form/div/div/div/div/input[@class="sc-e7c900b2-0 gvcJBA"]').send_keys('Ashlyn')

input("Press Enter to close the browser...")