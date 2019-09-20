from selenium import webdriver
browser = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
browser.get('https://be.qtest.abcmouse.com')

linkElem = browser.find_element_by_tag_name('login-button')
linkElem.click()

emailElem = browser.find_element_by_class_name('login_email')
emailElem.send_keys('tue20@e.test')
passwordElem = browser.find_element_by_class_name('login_password')
passwordElem.send_keys('password')

loginSubmit = browser.find_element_by_class_name('submit_button')
loginSubmit.click()

