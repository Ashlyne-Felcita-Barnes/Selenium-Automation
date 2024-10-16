from selenium import webdriver  
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By  
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains

# Path to your ChromeDriver  
service = Service("C:\\Users\\HP\\OneDrive\\Desktop\\chromedriver.exe")  
driver = webdriver.Chrome(service=service)
driver.get('https://www.w3schools.com/HTML/html5_draganddrop.asp')
s=driver.find_element(By.ID,'div1')
t=driver.find_element(By.ID,'div2')
action=ActionChains(driver)

action.drag_and_drop(s,t).perform()
input("Press Enter to close the browser...")

