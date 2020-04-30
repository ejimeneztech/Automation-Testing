from selenium import webdriver
import time
import requests,bs4

browser = webdriver.Chrome()
browser.get('https://tableau.aofl.com/#/signin?redirect=%2Fprojects')


#Add code for Logging in
try:

	#Loging In
	time.sleep(5)
	inputUserName = browser.find_element_by_name('username')
	inputUserName.send_keys('emilio.jimenez')

	inputUserName = browser.find_element_by_name('password')
	inputUserName.send_keys('J1M3N32LOgin!')

	signIn = browser.find_element_by_tag_name('button')
	signIn.click()

	
	print('Logged In Successfully')
except:
	print('Did not Login: Verify Html element exists')


#Add code for navigating to the User List
try:

	#Navigate to User List
	time.sleep(5)
	usersLink = browser.find_element_by_link_text('Users')
	usersLink.click()
	print('Navigation to Users list successfull')
except:	
	print('Did not find element for User list link')



#Extract all rows in the User List
try:

	res = requests.get('https://tableau.aofl.com/#/usersl')
	res.raise_for_sest_status()
	userListSoup = bs4.BeautifulSoup(res.text, 'html.parser')
	Print(type(userListSoup))
except:
	print('Could not extract User list')
