import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def user_chat(driver, name_user):
    try:
        # Locate the search box and type the contact's name
        search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
        search_box.click()
        search_box.send_keys(name_user)
        time.sleep(2)  # Wait for search results to load

        # Click the user's chat from search results
        user = driver.find_element(By.XPATH, f'//span[@title="{name_user}"]')
        user.click()
        print(f"Chat with {name_user} opened.")

    except Exception as e:
        print(f"Error: Could not find the contact '{name_user}'. {e}")
        sys.exit()

if __name__ == '__main__':
    # Set up ChromeDriver service
    service = Service("C:\\Users\\HP\\OneDrive\\Desktop\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    # Open WhatsApp Web
    driver.get('https://web.whatsapp.com')
    print("Please scan the QR code to log in.")
    time.sleep(30)  # Allow time for manual login

    # Wait until the main chat list is loaded
    time.sleep(10)  # Adjust this if necessary

    # Define the list of contacts to message
    name_list = ['']

    for name_user in name_list:
        try:
            user_chat(driver, name_user)

            # Wait briefly before trying to locate the message box
            time.sleep(2)  # Give time for the chat to fully load

            # Locate the message input box and type the message
            time.sleep(3)
            message_box = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div/div/p')
            message_box.click()
            message_box.send_keys("Hi ... using the WhatsApp bot")
            time.sleep(2)  # Give time for the input

            # Click the send button
            send_button = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[2]/button/span')
            send_button.click()
            print(f"Message sent to {name_user}")

        except Exception as e:
            print(f"An error occurred while sending a message to {name_user}: {e}")
            # Additional debugging: Print current page source
            print(driver.page_source)

    input("Press Enter to close the browser...")
    
