import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

browser = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
browser.get('https://cr.qtest.abcmouse.com')

linkElem = browser.find_element_by_tag_name('login-button')
linkElem.click()

emailElem = browser.find_element_by_class_name('login_email')
emailElem.send_keys('lv36@ejtest.test')
passwordElem = browser.find_element_by_class_name('login_password')
passwordElem.send_keys('password')

loginSubmit = browser.find_element_by_class_name('submit_button')
loginSubmit.click()

time.sleep(10)

iframe = browser.find_element_by_css_selector('#content-iframe')
browser.switch_to.frame(iframe)
shpDiv = browser.find_element_by_css_selector('#student-home')

def test_login():
    assert shpDiv != None#check if shp loads by checking shpDiv is defined
