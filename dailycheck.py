from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://dailycheck.cornell.edu/login')

assert "Daily" in driver.title

loginButton = driver.find_element_by_xpath('//*[@id="main-article"]/div[2]/div/div/a[1]')
loginButton.click()

username = driver.find_element_by_id('username')
username.send_keys('email') #ADD EMAIL ADDRESS HERE

password = driver.find_element_by_id('password') #ADD PASSWORD HERE
password.send_keys('password')

loginButton = driver.find_element_by_xpath('//*[@id="login"]/fieldset/div/div[1]/input')
loginButton.click()

scheduleTest = driver.find_element_by_xpath('//*[@id="main-article"]/div[2]/div/p/a/strong')
scheduleTest.click()

#SHADOW ROOT IS CAUSING THE ERROR
