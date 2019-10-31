import time
from selenium import webdriver

print("Enter qtest server:")
server = input()

print("Enter account email:")
text = input()

#mac OS
#browser = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')

#Windows
browser = webdriver.Chrome()

def expand_shadow_element(element):
    shadow_root = browser.execute_script('return arguments[0].shadowRoot', element)
    return shadow_root

#Subscription page
browser.get('https://'+server+'.abcmouse.com/abt/subscription')

root1 = browser.find_element_by_tag_name('subscription-form')
shadow_root1 = expand_shadow_element(root1)

emailElem = shadow_root1.find_element_by_css_selector('#email')
emailElem.send_keys(text)
emailConfirmElem = shadow_root1.find_element_by_css_selector('#confirm-email')
emailConfirmElem.send_keys(text)
passElem = shadow_root1.find_element_by_css_selector('#password')
passElem.send_keys('password')
confirmPassElem = shadow_root1.find_element_by_css_selector('#confirm-password')
confirmPassElem.send_keys('password')


cardNameElem = shadow_root1.find_element_by_css_selector('#card-name')
cardNameElem.send_keys('Emilio Test')
ccNumElem = shadow_root1.find_element_by_css_selector('#cc-num')
ccNumElem.send_keys('378750082492053')
cvvElem = shadow_root1.find_element_by_css_selector('#cvv')
cvvElem.send_keys('4882')
zipElem = shadow_root1.find_element_by_css_selector('#zipcode')
zipElem.send_keys('91203')

time.sleep(10)

button = shadow_root1.find_element_by_css_selector('button')
button.click()

#goes to upgrade page. Wait for page to load
time.sleep(10)
#expand shadow root elements
root2 = browser.find_element_by_tag_name('landscape-upgrade-form')
shadow_root2 = expand_shadow_element(root2)

root3 = shadow_root2.find_element_by_css_selector('#no-thanks')
shadow_root3 = expand_shadow_element(root3)

noThanks = shadow_root3.find_element_by_css_selector('#radio-wrapper')
noThanks.click()

submitButton = shadow_root2.find_element_by_css_selector('#upgrade-form-container > button')
submitButton.click()

#Goes to upgrade offer pop-up. 
root4 = browser.find_element_by_css_selector('upgrade-offer-popup')
shadow_root4 = expand_shadow_element(root4)

noUpgrade = shadow_root4.find_element_by_css_selector('upgrade-popup-redirect-button')
noUpgrade.click()

#Goes to assessment purchase page.
time.sleep(4)

root5 = browser.find_element_by_css_selector('assessment-monthly-form')
shadow_root5 = expand_shadow_element(root5)

root6 = shadow_root5.find_element_by_css_selector('abcmouse-radio-button')
shadow_root6 = expand_shadow_element(root6)

#Does not work. Clicks wrong check box. Will purchase assesment for now. Need to figure out how to click 'no thanks' checknbox
radioButton = shadow_root6.find_element_by_css_selector('#radio-wrapper')
radioButton.click()


submitButton2 = shadow_root5.find_element_by_css_selector('button')
submitButton2.click()

#Goes to Assessment Monthly Thank You Pop Up
time.sleep(3)

root7 = browser.find_element_by_css_selector('assessment-monthly-thank-you-popup')
shadow_root7 = expand_shadow_element(root7)

nextButton = shadow_root7.find_element_by_css_selector('button')
nextButton.click()

#Goes to Sub-Confirm page
time.sleep(5)

root8 = browser.find_element_by_css_selector('continue-button-reg')
shadow_root8 = expand_shadow_element(root8)

contButton = shadow_root8.find_element_by_css_selector('button')
contButton.click()
time.sleep(4)
browser.close()

