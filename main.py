from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = (r"C:\Users\HeDar\Documents\GitHub\RoadTestBot\chromedriver.exe")

driver = webdriver.Chrome(PATH)
driver.get("https://www.icbc.com/driver-licensing/visit-dl-office/Pages/Book-a-road-test.aspx")

book_button = driver.find_element_by_link_text("Book online")
book_button.click()


time.sleep(5)
