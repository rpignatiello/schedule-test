from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

username = ''
password = ''
firstname = ''
phone = '' #xxxxxxxxxx
birthMonth = '' #xx
birthDay = '' #xx
birthYear = '' #xxxx


driver = webdriver.Chrome()
driver.get('https://dailycheck.cornell.edu/login')

assert "Daily" in driver.title

actions = ActionChains(driver)

loginButton = driver.find_element_by_xpath('//*[@id="main-article"]/div[2]/div/div/a[1]')
loginButton.click()

username = driver.find_element_by_id('username')
username.send_keys(username)

password = driver.find_element_by_id('password')
password.send_keys(password)

loginButton = driver.find_element_by_xpath('//*[@id="login"]/fieldset/div/div[1]/input')
loginButton.click()

#scheduleTest = driver.find_element_by_xpath('//*[@id="main-article"]/div[2]/div/p/a')
#scheduleTest.click()

scheduleTest = driver.find_element_by_xpath('//*[@id="main-article"]/div[2]/div[4]/div/div/p[3]/a')
actions.move_to_element(scheduleTest).perform()
scheduleTest.click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'nextButton')))
nextButton = driver.find_element_by_id('nextButton')
actions.move_to_element(nextButton).perform()
nextButton.click()

#CLICK REGISTERED BEFORE
#SHADOW ROOT
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'previously-regd-dd')))
#shadowRoot = driver.execute_script('return document.querySelector("previously-regd-dd").shadowRoot')
#shadowRoot.find_element_by_css('.button').click()
#time.sleep(3)
registeredBefore = driver.execute_script('return document.getElementById("previously-regd-dd").shadowRoot.querySelector("button")')
registeredBefore.click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/ion-app/ion-popover/div/div[2]/ion-select-popover/ion-list/ion-radio-group/ion-item[2]/ion-radio')))
#yesButton = driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-popover/div/div[2]/ion-select-popover/ion-list/ion-radio-group/ion-item[2]/ion-radio')
#yesButton1 = yesButton.find_element_by_xpath('/html/body/app-root/ion-app/ion-popover/div/div[2]/ion-select-popover/ion-list/ion-radio-group/ion-item[2]/ion-radio//button')
yesButton = driver.execute_script('return document.getElementsByClassName("sc-ion-select-popover-md md in-item interactive hydrated")[1].shadowRoot.querySelector("button")')
yesButton.click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/ion-app/ion-router-outlet/app-patient-registration/ion-content/div/div/div[2]/form/div[1]/div/span[2]/span/ion-item[1]/ion-input/input')))
firstNameInput = driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-router-outlet/app-patient-registration/ion-content/div/div/div[2]/form/div[1]/div/span[2]/span/ion-item[1]/ion-input/input')
firstNameInput.send_keys(firstname)
actions.send_keys(Keys.TAB).perform()
actions.send_keys(phone).perform()
actions.send_keys(Keys.TAB).perform()
actions.send_keys(birthMonth).perform()
actions.send_keys(birthDay).perform()
actions.send_keys(birthYear).perform()

#CAPTCHA MIGHT NEED TO BE DONE BY USER
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']")))

try:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='recaptcha-checkbox goog-inline-block recaptcha-checkbox-unchecked rc-anchor-checkbox']/div[@class='recaptcha-checkbox-checkmark']")))
    reCaptcha = driver.find_element_by_xpath('//span[@class="recaptcha-checkbox goog-inline-block recaptcha-checkbox-unchecked rc-anchor-checkbox"]/div[@class="recaptcha-checkbox-checkmark"]')
    driver.execute_script('arguments[0].click()', reCaptcha)
    until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[3]/div[1]/div/div/span/div[4]')))
    print('try')
except:
    print('captcha needs to be done by user')
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[3]/div[1]/div/div/span/div[4]')))
    print('except')

#WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[3]/div[1]/div/div/span/div[4]')))
print('done w try except')
driver.switch_to.parent_frame()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'nextButton')))
nextButton = driver.find_element_by_id('nextButton')
time.sleep(.5)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'nextButton')))
time.sleep(.5)
nextButton.click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'nextButton')))
nextButton = driver.find_element_by_id('nextButton')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'nextButton')))
nextButton.click()
#registeredBefore = driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-router-outlet/app-patient-registration/ion-content/div/div/div[2]/form/div[1]/div/span/ion-item/ion-select//button')
#registeredBefore.click()



#WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'nextButton')))
#nextButton = driver.find_element_by_id('nextButton')
#nextButton.click()

#WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, 'html/body/app-root/ion-app/ion-router-outlet/app-patient-registration/ion-content/div/div/div[2]/form/div[1]/div/ion-item[3]/date-field/div/div[1]/ion-input/input')))
#birthdayInput = driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-router-outlet/app-patient-registration/ion-content/div/div/div[2]/form/div[1]/div/ion-item[3]/date-field/div/div[1]/ion-input/input')
#birthdayInput.send_keys('12')
#actions.send_keys('22').perform()
#actions.send_keys('2001').perform()

#CHANGE WHICH PART OF INPUT
