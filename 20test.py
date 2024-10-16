from selenium import webdriver  
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By  
from selenium.webdriver.support.ui import Select

# Path to your ChromeDriver  
service = Service("C:\\Users\\HP\\OneDrive\\Desktop\\chromedriver.exe")  
driver = webdriver.Chrome(service=service)
driver.get('https://licindia.in/')
drop=Select(driver.find_element(By.CLASS_NAME,'form-select'))
#drop.select_by_visible_text('Create wealth')
#drop.select_by_index(3)
#drop.select_by_value('/have-health-cover')
print(len(drop.options))
for plan in drop.options:
    print(plan.text)


input("Press Enter to close the browser...")