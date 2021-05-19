from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : 'D:\\New folder\\'}
chrome_options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(r"C:\Users\iamab\Downloads\chromedriver_win32\chromedriver.exe",options=chrome_options)

driver.get("http://the-internet.herokuapp.com/")
driver.maximize_window()
time.sleep(1)
driver.find_element_by_link_text("File Upload").click()
time.sleep(2)
upload=driver.find_element_by_id("file-upload")
time.sleep(1)
upload.send_keys(r"C:\Users\iamab\OneDrive\Desktop\check.txt")
time.sleep(1)
driver.find_element_by_id("file-submit").click()
time.sleep(1)
driver.get("http://the-internet.herokuapp.com/")
time.sleep(1)
driver.find_element_by_link_text("File Download").click()
time.sleep(1)
driver.find_element_by_link_text("newfile.xlsx").click()
driver.get("http://the-internet.herokuapp.com/")
time.sleep(1)
driver.find_element_by_link_text("Multiple Windows").click()
time.sleep(1)
driver.find_element_by_link_text("Click Here").click()
time.sleep(1)
