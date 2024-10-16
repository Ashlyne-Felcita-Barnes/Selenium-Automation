from selenium import webdriver  
from selenium.webdriver.chrome.service import Service  

# Path to your ChromeDriver  
service = Service("C:\\Users\\HP\\OneDrive\\Desktop\\chromedriver.exe")  
driver = webdriver.Chrome(service=service)  

# Example of opening a website  
driver.get("https://www.facebook.com")  
input("Press Enter to close the browser...")  




