from selenium import webdriver  
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By  

# Path to your ChromeDriver  
service = Service("C:\\Users\\HP\\OneDrive\\Desktop\\chromedriver.exe")  
driver = webdriver.Chrome(service=service)
driver.get("https://practice.microdegree.work")  
driver.find_element(By.ID,'video').click()
print(driver.current_url)
curent_url=driver.current_url
excepted_url='https://practice.microdegre.work/'

if curent_url==excepted_url:
    print('success')
else:
    print('failed')
input("Press Enter to close the browser...")