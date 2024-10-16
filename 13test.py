from selenium import webdriver  
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By  

# Path to your ChromeDriver  
service = Service("C:\\Users\\HP\\OneDrive\\Desktop\\chromedriver.exe")  
driver = webdriver.Chrome(service=service)
driver.get('https://www.daijiworld.com/news')  
driver.find_element(By.XPATH,'html/body/div/header/nav/div/div/div/a').click()
#driver.find_element(By.CSS_SELECTOR,'div header nav div div div:nth-child(2) a').click()

input("Press Enter to close the browser...")