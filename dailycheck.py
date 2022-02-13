from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

netId = r'NETID'
password = r'PASSWORD'
firstName = r'FIRSTNAME'
lastName = r'LASTNAME'
phone = r'PHONENUMBER' #xxxxxxxxxx
birthMonth = r'MONTH' #xx
birthDay = r'DAY' #xx
birthYear = r'YEAR' #xxxx


driver = webdriver.Chrome()
driver.get('https://dailycheck.cornell.edu/login')

actions = ActionChains(driver)

""" Find and click a button using xpath (NOT used for next button) """
def clickButton(xpath):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
    button= driver.find_element_by_xpath(xpath)
    actions.move_to_element(button).perform()
    button.click()

""" Find input by xpath and fill it with information """
def sendText(xpath, text):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
    input= driver.find_element_by_xpath(xpath)
    actions.move_to_element(input).perform()
    input.send_keys('', text)

""" Find and click next button on cayugahealth.org """
def nextButton():
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'nextButton')))
    nextButton = driver.find_element_by_id('nextButton')
    actions.move_to_element(nextButton).perform()
    nextButton.click()

""" Find dropdown button and click """
def dropDownOpen(id):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, id)))
    button= driver.execute_script('return document.getElementById("' + id + '").shadowRoot.querySelector("button")')
    actions.move_to_element(button).perform()
    button.click()

""" Find dropdown selection and click """
def dropDownSelect(xpath, js):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
    selection= driver.execute_script(js)
    selection.click()

""" Fills in information for users who have previously registered """
def fillPrevInfo(firstname, phone, birthMonth, birthDay, birthYear):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/ion-app/ion-router-outlet/app-patient-registration/ion-content/div/div/div[2]/form/div[1]/div/span[2]/span/ion-item[1]/ion-input/input')))
    firstNameInput = driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-router-outlet/app-patient-registration/ion-content/div/div/div[2]/form/div[1]/div/span[2]/span/ion-item[1]/ion-input/input')
    firstNameInput.send_keys(firstname)
    actions.send_keys(Keys.TAB).perform()
    actions.send_keys(phone).perform()
    actions.send_keys(Keys.TAB).perform()
    actions.send_keys(birthMonth).perform()
    actions.send_keys(birthDay).perform()
    actions.send_keys(birthYear).perform()

#Login Button (Cornell NetId login only)
clickButton('/html/body/div[2]/main/div/article/div/div/div/a[1]')

#Net Id input is filled
sendText('/html/body/div[2]/main/article/div/div[1]/form/fieldset/input[1]', netId)
#Password input is filled
sendText('/html/body/div[2]/main/article/div/div[1]/form/fieldset/input[2]', password)
#Finished Cornell NetId loginButton
clickButton('/html/body/div[2]/main/article/div/div[1]/form/fieldset/div/div[1]/input')

#Click on link in banner to go to scheduling site
#clickButton('/html/body/div[2]/main/article/div/div[1]/form/fieldset/input[1]')

#Click on supplemental test link (Used mainly for debugging purposes)
clickButton('/html/body/div[2]/main/div/article/div/div[4]/div/div/p[3]/a')

#Webpage should be cayugahealth.org
assert 'Patient Registration' in driver.title

nextButton()

#Select yes for having already filled out the application
dropDownOpen('previously-regd-dd')
dropDownSelect('/html/body/app-root/ion-app/ion-popover/div/div[2]/ion-select-popover/ion-list/ion-radio-group/ion-item[2]/ion-radio', 'return document.getElementsByClassName("sc-ion-select-popover-md md in-item interactive hydrated")[1].shadowRoot.querySelector("button")')

#Fill out name, phone number, and birthday
fillPrevInfo(firstName, phone, birthMonth, birthDay, birthYear)

#Completes the Capthca
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']")))
try:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='recaptcha-checkbox goog-inline-block recaptcha-checkbox-unchecked rc-anchor-checkbox']/div[@class='recaptcha-checkbox-checkmark']")))
    reCaptcha = driver.find_element_by_xpath('//span[@class="recaptcha-checkbox goog-inline-block recaptcha-checkbox-unchecked rc-anchor-checkbox"]/div[@class="recaptcha-checkbox-checkmark"]')
    driver.execute_script('arguments[0].click()', reCaptcha)
except:
    input('press Enter to continue')

driver.switch_to.parent_frame()
nextButton()
nextButton()

#Sign legal document
dropDownOpen('agreed-to-policy-chk')
sendText('/html/body/app-root/ion-app/ion-router-outlet/app-patient-registration/ion-content/div/div/div[2]/form/div[1]/div/ion-item[2]/ion-input/input', firstName + ' ' + lastName)
nextButton()

#WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'location-dd')))
#locationDropDown =  driver.execute_script('return document.getElementById("location-dd").shadowRoot.querySelector("button")')
#locationDropDown.click()

#time.sleep(.2)

#WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/ion-app/ion-popover/div/div[2]/ion-select-popover/ion-list/ion-radio-group/ion-item[6]/ion-radio')))
#westCampus = driver.execute_script('return document.getElementsByClassName("sc-ion-select-popover-md md in-item interactive hydrated")[5].shadowRoot.querySelector("button")')
#westCampus.click()
