import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


print("Enter qtest server:")
server = input()

print("Enter account email:")
text = input()

browser = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
browser.get('https://'+server+'.abcmouse.com')

linkElem = browser.find_element_by_tag_name('login-button')
linkElem.click()

emailElem = browser.find_element_by_class_name('login_email')
emailElem.send_keys(text)
passwordElem = browser.find_element_by_class_name('login_password')
passwordElem.send_keys('password')

loginSubmit = browser.find_element_by_class_name('submit_button')
loginSubmit.click()

time.sleep(8)
iframe = browser.find_element_by_css_selector('#content-iframe')
browser.switch_to.frame(iframe)

browser.execute_script('document.querySelector("#survey-link").click()')

time.sleep(4)

browser.execute_script('document.querySelector("#survey-2-link").click()')

time.sleep(4)

browser.execute_script('document.querySelector("#setup-parent-link").click()')

time.sleep(4)

FNinput = browser.find_element_by_name('firstName')
FNinput.send_keys('Parent')
famName = browser.find_element_by_name('familyName')
famName.send_keys('Test')

time.sleep(4)
browser.execute_script('document.querySelector("#setup-parent-continue").click()')

time.sleep(4)
kidName = browser.find_element_by_name('firstName')
kidName.send_keys('Kid 1')

browser.execute_script('document.querySelector("#onboarding > div > div > div.onboarding-content > form > div.first-row > div.child-gender.prevent-stretch > div > div.aofl-radio.boy > label").click()')

#Only Edit BELOW this line (Month/Year dropdowns)



wrappers = browser.find_elements_by_class_name('options-wrapper')


months = wrappers[0].find_elements_by_tag_name('aofl-option')


years = wrappers[1].find_elements_by_tag_name('aofl-option')


label = years[1].find_element_by_tag_name('label')

browser.execute_script('document.querySelector("#onboarding > div > div > div.onboarding-content > form > div.first-row > div.child-birthday.prevent-stretch > aofl-dropdown.child-month > div > div > div.dropdown.dropdown-collapsed").click()')

months[2].click()

browser.execute_script('document.querySelector("#onboarding > div > div > div.onboarding-content > form > div.first-row > div.child-birthday.prevent-stretch > aofl-dropdown.child-year > div > div > div.dropdown.dropdown-collapsed").click()')


browser.execute_script("arguments[0].click();", label)


#Only Edit Above this line
browser.execute_script('document.querySelector("#pre-k").click()')

browser.execute_script('document.querySelector("#setup-parent-continue").click()')
time.sleep(4)

browser.execute_script('document.querySelector("#boy_avatar16").click()')
browser.execute_script('document.querySelector("#onboarding > div > div > div > div:nth-child(5)").click()')
time.sleep(4)

browser.execute_script('document.querySelector("#hamster-1").click()')
browser.execute_script('document.querySelector("#fish-1").click()')
petName = browser.find_element_by_css_selector('#onboarding > div > div > div > form > div.left-content > div > div.child-hamster-name > input')
petName.send_keys('test')
browser.execute_script('document.querySelector("#onboarding > div > div > div > div:nth-child(4)").click()')
time.sleep(4)

browser.execute_script('document.querySelector("#onboarding > div > div > div > div.onboarding-video-container > a").click()')
browser.execute_script('document.querySelector("#ngdialog1 > div.ngdialog-content > div.std-modal-body.with-title-bar > div.std-modal-buttons.multiple-buttons > button:nth-child(2)").click()')
time.sleep(4)

#TO SHP
browser.execute_script('document.querySelector("#student-homepage-link").click()')
time.sleep(4)
browser.close()
