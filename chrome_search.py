import selenium
from selenium import webdriver
browser = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')


def expand_shadow_element(element):
  shadow_root = browser.execute_script('return arguments[0].shadowRoot', element)
  return shadow_root

browser.get("chrome://downloads")
root1 = browser.find_element_by_tag_name('downloads-manager')
shadow_root1 = expand_shadow_element(root1)

root2 = shadow_root1.find_element_by_css_selector('downloads-toolbar')
shadow_root2 = expand_shadow_element(root2)

root3 = shadow_root2.find_element_by_css_selector('cr-toolbar')
shadow_root3 = expand_shadow_element(root3)

root4 = shadow_root3.find_element_by_css_selector('cr-toolbar-search-field')
shadow_root4 = expand_shadow_element(root4)

search_box = shadow_root4.find_element_by_css_selector("#searchInput")
search_box.send_keys('test')
