from selenium import webdriver
browser = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')


def expand_shadow_element(element):
    shadow_root = browser.execute_script('return arguments[0].shadowRoot', element)
    return shadow_root

browser.get('https://www.abcmouse.com/abt/register')
root1 = browser.find_element_by_tag_name('prospect-reg-form')
shadow_root1 = expand_shadow_element(root1)

emailElem = shadow_root1.find_element_by_css_selector('#email')
submitElem = shadow_root1.find_element_by_css_selector('button')
emailElem.send_keys("test@e.test")
submitElem.click()
