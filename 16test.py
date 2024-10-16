from selenium import webdriver  
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By  

# Path to your ChromeDriver  
service = Service("C:\\Users\\HP\\OneDrive\\Desktop\\chromedriver.exe")  
driver = webdriver.Chrome(service=service)
driver.get('https://tally.so/r/3ylqax?Course=ATS')  
driver.find_element(By.XPATH,'//*[@id="7cfe053f-6268-45d8-9ce1-76ed1aa0f68d"]').send_keys('Ashlyn')

input("Press Enter to close the browser...")