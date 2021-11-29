from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time



def control():
    PATH = (r"C:\Users\HeDar\Documents\GitHub\RoadTestBot\chromedriver.exe")

    driver = webdriver.Chrome(PATH)
    driver.get("https://www.icbc.com/driver-licensing/visit-dl-office/Pages/Book-a-road-test.aspx")

    book_button = driver.find_element_by_link_text("Book online")
    book_button.click()

    next_button = driver.find_element_by_link_text("Next")
    next_button.click()

def sign_in_input():
    str(input("Input last name\n"))
    try:
        int(input("Enter B.C. Licence Number\n"))
    except ValueError:
        print ("Input must be numbers only.")
    str(input("Enter keyword \n"))


def is_int(input):



time.sleep(5)
