import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

browser = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
browser.get('https://du.qtest.abcmouse.com')

linkElem = browser.find_element_by_tag_name('login-button')
linkElem.click()

emailElem = browser.find_element_by_class_name('login_email')
emailElem.send_keys('du12@e.test')
passwordElem = browser.find_element_by_class_name('login_password')
passwordElem.send_keys('password')

loginSubmit = browser.find_element_by_class_name('submit_button')
loginSubmit.click()

time.sleep(8)
iframe = browser.find_element_by_css_selector('#content-iframe')
browser.switch_to.frame(iframe)


browser.execute_script('document.querySelector("#survey-link").click()')


time.sleep(4)

surveyItems = browser.find_elements_by_class_name('survey-item')
for element in surveyItems:
    item = element.find_element_by_tag_name('label')
    browser.execute_script("arguments[0].click();", item)
    surveySection2 = browser.find_element_by_css_selector('#onboarding > div > div > div > div.onboarding-survey.secondary-survey')
    surveyItems2 = surveySection2.find_elements_by_class_name('survey-item')
    for element in surveyItems2:
        item2 = element.find_element_by_tag_name('label')
        browser.execute_script("arguments[0].click();", item2)
