from selenium import webdriver 
from selenium.webdriver.chrome.service import Service 
from config import chrome_driver_path 

def create_chrome_driver():
    service = Service(executable_path = chrome_driver_path)
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(service = service, options = options)
    driver.implicitly_wait(10)
    return driver 
    