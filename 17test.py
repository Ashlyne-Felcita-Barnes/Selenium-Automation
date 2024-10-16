from selenium import webdriver  
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By  
import time

# Path to your ChromeDriver  
service = Service("C:\\Users\\HP\\OneDrive\\Desktop\\chromedriver.exe")  
driver = webdriver.Chrome(service=service)
driver.get('https://www.marutisuzuki.com/?srsltid=AfmBOooa6bTex37Gsa2lT6UtFNAV91cahm6alQX94ww9sLukhkWsnjpm')  
print(driver.find_element(By.ID,'BaSV-Home-red').text)
driver.find_element(By.ID,'BaSV-Home-red').click()
driver.find_element(By.ID,'lad-footer').click()
time.sleep(10)
driver.find_element(By.LINK_TEXT,'LOCATE A DEALER').text
driver.find_element(By.LINK_TEXT,'LOCATE A DEALER').click()


input("Press Enter to close the browser...")