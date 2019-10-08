#This is the only file intended to run onboarding test cases
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

browser = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
browser.get('https://ef.qtest.abcmouse.com')

linkElem = browser.find_element_by_tag_name('login-button')
linkElem.click()

emailElem = browser.find_element_by_class_name('login_email')
emailElem.send_keys('testme@e.test')
passwordElem = browser.find_element_by_class_name('login_password')
passwordElem.send_keys('password')

loginSubmit = browser.find_element_by_class_name('submit_button')
loginSubmit.click()

time.sleep(8)
iframe = browser.find_element_by_css_selector('#content-iframe')
browser.switch_to.frame(iframe)

#Test Case 1: User can click on 'Continue' in initial onboarding screen
def test_click_1():
    try:
        browser.execute_script('document.querySelector("#survey-link").click()')
    except:
        print('Continue button was not clicked')

time.sleep(4)

#Test Case 2: User can click on all radio buttons and continue button (split this into two)
def test_click_2():
    try:
        browser.execute_script('document.querySelector("#survey-2-link").click()')
    except:
        print('Step 1: Continue button was not clicked')
