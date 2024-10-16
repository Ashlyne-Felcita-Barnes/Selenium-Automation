from selenium import webdriver  
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By  
import time

# Path to your ChromeDriver  
service = Service("C:\\Users\\HP\\OneDrive\\Desktop\\chromedriver.exe")  
driver = webdriver.Chrome(service=service)
driver.get('https://forms.office.com/r/NGvhiFBEg9')
driver.find_element(By.ID,'QuestionChoiceOption2').click()
input("Press Enter to close the browser...")