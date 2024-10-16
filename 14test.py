from selenium import webdriver  
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By  

# Path to your ChromeDriver  
service = Service("C:\\Users\\HP\\OneDrive\\Desktop\\chromedriver.exe")  
driver = webdriver.Chrome(service=service)
driver.get('https://tally.so/r/3ylqax?Course=ATS')  
driver.find_element(By.XPATH,'html/body/div/div/main/section/form/div/div/div/div/input').send_keys('Ashlyn')
driver.find_element(By.XPATH,'html/body/div/div/main/section/form/div/div/div/div/input').clear()
driver.find_element(By.XPATH,'//input').send_keys('Ashlynn')
input("Press Enter to close the browser...")