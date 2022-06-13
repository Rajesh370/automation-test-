# pip3 install selenium -- This will install selenium libary
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import service

def open_url():
    driver = webdriver.chrome("D:\\webdriver\\chromedriver.exe")
    driver.get('https://goggle.com')
    time.sleep(4)
    driver.quit()

def open_url2()
    s = service(ChromeDriverManager().install())

if __name__ == "__main__":
    open_url()


