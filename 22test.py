from selenium import webdriver  
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By  
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains

# Path to your ChromeDriver  
service = Service("C:\\Users\\HP\\OneDrive\\Desktop\\chromedriver.exe")  
driver = webdriver.Chrome(service=service)
driver.get('https://www.selenium.dev/')
action=ActionChains(driver)
b=driver.find_element(By.CLASS_NAME,'selenium-button.selenium-webdriver.text-uppercase.fw-bold')
print(b.text)
action.context_click(b).perform() 
input("Press Enter to close the browser...")