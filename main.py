##########################################################
# Task         : Website Automation Test                 #
# Organization : M2                                      #
# Author       : Rabiya Basreen                          #
# Reference    : Google.com, Stackoverflow, Browserstack #
##########################################################

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

def executeTestCase():
    #find the entry point on the webpage to enter the project details
    project_entry = driver.find_element("xpath", "//input[@placeholder='+ Add project']")
    project_entry.click()
    project_entry.send_keys("Selenium Project 12")
    project_entry.send_keys(Keys.RETURN)
    time.sleep(5)

    #find the last entry of the record from the floating new group grid
    find_proj_entry = driver.find_element("xpath",
                                          "//div[@class = 'pulse-component-wrapper board-id-1160391072 pulseWrapper--ywR3E last-pulse lastPulse--JhvJJ pulse-new-layout']//div[starts-with(@id,'row-pulse')]")
    latest_project_id = find_proj_entry.get_attribute("id")
    split_proj_id = latest_project_id.split('-')
    final_proj_id = split_proj_id[4]
    time.sleep(2)

    #open the person details
    person_open = driver.find_element("xpath", "//div[@id='" + latest_project_id + "-focus-person-']")
    person_open.click()
    #fill the person details
    person_fill = driver.find_element("xpath", "//div[@id = 'combobox-item-40438731']")
    person_fill.click()
    time.sleep(2)

    # open the status details
    status_open = driver.find_element("xpath", "//div[@id='" + latest_project_id + "-focus-status-']")
    status_open.click()
    #fill the person details
    status_fill = driver.find_element("xpath", "//li[@id ='1160391072_status_1']")
    status_fill.click()
    time.sleep(2)

    # enter the date details
    date_open = driver.find_element("xpath", "//div[@id='" + latest_project_id + "-focus-date4-']")
    date_open.click()

    #move back to previous month
    date_navigate = driver.find_element("xpath", "//button[@aria-label='Move backward to switch to the previous month']//div[@class='ds-date-navigation-item-component']//*[name()='svg']")
    time.sleep(2)
    date_navigate.click()

    #fill the date details. The below two lines represent types of approach to choose date
    date_fill = driver.find_element("xpath", "//td[@class='CalendarDay CalendarDay--valid']//button[@class='CalendarDay__button' and @tabindex = '-1']")
    #date_fill = driver.find_element("xpath", "//button[@aria-label='Friday, March 31, 2023']")
    time.sleep(2)
    date_fill.click()


def loadAndSetWebPage(url, user, password):
    driver.maximize_window()# maximize the broswer window
    driver.get(url)# open the testing URL

    #enter the username and password into the fields
    user_email = driver.find_element("id", "user_email")
    user_email.clear()
    user_email.send_keys(user)
    user_password = driver.find_element("id", "user_password")
    user_password.clear()
    user_password.send_keys(password)
    driver.find_element("xpath", "//button[@aria-label='Log in']").click()
    time.sleep(2)

    #call the function to execute test cases
    executeTestCase()


if __name__ == '__main__':
    # chrome oprtions added to stop the chrome browser from auto closing
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    # chrome browser initialized as the testing browser
    driver = webdriver.Chrome(options=chrome_options)

    # enter values via the console
    url = input("Enter the URL to test: ")
    user = input("Enter the username: ")
    password = input("Enter the password: ")

    # call the setup function
    loadAndSetWebPage(url, user, password)










