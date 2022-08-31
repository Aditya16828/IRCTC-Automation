import time
import pandas as pd
import autoit
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument(
    r'user-data-dir=C:/Users/adity/AppData/Local/Google/Chrome/User Data')  # loads cookies and data of our chrome browser
options.add_argument('--profile-directory=Default')
browser = webdriver.Chrome('chromedriver.exe', chrome_options=options)
browser.execute_script("window.open('about:blank', 'tab2');")
browser.switch_to.window("tab2")
url = "https://www.irctc.co.in/nget/train-search"
try:
    browser.get(url)
except:
    print("Error!!!")
    browser.close()

time.sleep(3)
ok1_button = browser.find_element_by_xpath(
    '/html/body/app-root/app-home/div[1]/app-header/p-dialog[2]/div/div/div[2]/div/form/div[2]/button')
ok1_button.click()

try:
    from_box = browser.find_element_by_xpath(
        '/html/body/app-root/app-home/div[3]/div/app-main-page/div/div/div[1]/div[1]/div[1]/app-jp-input/div/form/div[2]/div[1]/div[1]/p-autocomplete/span/input')
except:
    print("Error!!!")
    browser.close()
time.sleep(1)

from_box = browser.find_element_by_xpath(
    '/html/body/app-root/app-home/div[3]/div/app-main-page/div/div/div[1]/div[1]/div[1]/app-jp-input/div/form/div[2]/div[1]/div[1]/p-autocomplete/span/input')
from_box.send_keys('NEW DELHI - NDLS')
# browser.find_element_by_xpath('/html/body/app-root/app-home/div[3]/div/app-main-page/div/div/div[1]/div[1]/div[1]/app-jp-input/div/form/div[2]/div[1]/div[1]/p-autocomplete/span/div/ul/li[1]').click()


to_box = browser.find_element_by_xpath(
    '/html/body/app-root/app-home/div[3]/div/app-main-page/div/div/div[1]/div[1]/div[1]/app-jp-input/div/form/div[2]/div[1]/div[2]/p-autocomplete/span/input')
to_box.send_keys('MGR CHENNAI CTL - MAS')
# browser.find_element_by_xpath('/html/body/app-root/app-home/div[3]/div/app-main-page/div/div/div[1]/div[1]/div[1]/app-jp-input/div/form/div[2]/div[1]/div[2]/p-autocomplete/span/div/ul/li[1]').click()


flexible_with_date_check_box = browser.find_element_by_xpath(
    '/html/body/app-root/app-home/div[3]/div/app-main-page/div/div/div[1]/div[1]/div[1]/app-jp-input/div/form/div[4]/div/span[2]/label')
flexible_with_date_check_box.click()


date_box = browser.find_element_by_xpath(
    '/html/body/app-root/app-home/div[3]/div/app-main-page/div/div/div[1]/div[1]/div[1]/app-jp-input/div/form/div[2]/div[2]/div[1]/p-calendar/span/input')
date_box.click()
browser.find_element_by_xpath(
    '/html/body/app-root/app-home/div[3]/div/app-main-page/div/div/div[1]/div[1]/div[1]/app-jp-input/div/form/div[2]/div[2]/div[1]/p-calendar/span/div/div/div[1]/a[2]').click()
browser.find_element_by_xpath(
    '/html/body/app-root/app-home/div[3]/div/app-main-page/div/div/div[1]/div[1]/div[1]/app-jp-input/div/form/div[2]/div[2]/div[1]/p-calendar/span/div/div/div[2]/table/tbody/tr[4]/td[6]/a').click()


search_box = browser.find_element_by_xpath(
    '/html/body/app-root/app-home/div[3]/div/app-main-page/div/div/div[1]/div[1]/div[1]/app-jp-input/div/form/div[5]/div/button')
search_box.click()
time.sleep(3)

browser.find_element_by_xpath(
    '/html/body/app-root/app-home/div[3]/div/app-train-list/div[4]/div/div[5]/div[1]/div[1]/app-train-avl-enq/div[1]/div[5]/div/table/tr/td[1]/div').click()
time.sleep(3)
browser.find_element_by_xpath(
    '/html/body/app-root/app-home/div[3]/div/app-train-list/div[4]/div/div[5]/div[1]/div[1]/app-train-avl-enq/div[2]/div/span/span/button[1]').click()
time.sleep(3)
browser.find_element_by_xpath(
    '/html/body/app-root/app-home/div[3]/div/app-train-list/p-confirmdialog[1]/div/div/div[3]/button[1]/span[2]').click()
time.sleep(3)
browser.find_element_by_xpath(
    '/html/body/app-root/app-home/div[3]/div/app-train-list/p-confirmdialog[2]/div/div/div[3]/button[1]/span[2]').click()
time.sleep(3)  # time for sleep

# login
username = ""
browser.find_element_by_xpath(
    '/html/body/app-root/app-home/div[3]/app-login/p-dialog[1]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[1]/input').send_keys(username)

password = ""
browser.find_element_by_xpath(
    '/html/body/app-root/app-home/div[3]/app-login/p-dialog[1]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[2]/input').send_keys(password)
time.sleep(10)

# captcha
browser.find_element_by_xpath(
    '/html/body/app-root/app-home/div[3]/app-login/p-dialog[1]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[3]/div/app-nlp-captcha/div/div[2]/div/div[3]/div[1]/input').send_keys("")
time.sleep(10)

# sign in button click
browser.find_element_by_xpath(
    '/html/body/app-root/app-home/div[3]/app-login/p-dialog[1]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/span/button').click()
time.sleep(10)

passenger_name = 'XXXXXXXX'
passenger_box = browser.find_element_by_xpath(
    '/html/body/app-root/app-home/div[3]/div/app-passenger-input/div[5]/form/div/div[1]/div[4]/p-panel/div/div[2]/div/div[1]/div[2]/div/app-passenger/div/div[1]/span/div[1]/p-autocomplete/span/input')
passenger_box.send_keys(passenger_name)

age = "25"
age_box = browser.find_element_by_xpath(
    '/html/body/app-root/app-home/div[3]/div/app-passenger-input/div[5]/form/div/div[1]/div[4]/p-panel/div/div[2]/div/div[1]/div[2]/div/app-passenger/div/div[1]/span/div[2]/input')
age_box.send_keys(age)

gender_box = browser.find_element_by_xpath(
    '/html/body/app-root/app-home/div[3]/div/app-passenger-input/div[5]/form/div/div[1]/div[4]/p-panel/div/div[2]/div/div[1]/div[2]/div/app-passenger/div/div[1]/span/div[3]/select')
gender_box.click()
time.sleep(3)

preference_box = browser.find_element_by_xpath(
    '/html/body/app-root/app-home/div[3]/div/app-passenger-input/div[5]/form/div/div[1]/div[4]/p-panel/div/div[2]/div/div[1]/div[2]/div/app-passenger/div/div[1]/div[1]/select')
preference_box.click()
time.sleep(3)

phnumber = "9999666622"
ph_box = browser.find_element_by_xpath(
    '/html/body/app-root/app-home/div[3]/div/app-passenger-input/div[5]/form/div/div[1]/div[6]/p-panel/div/div[2]/div/div[2]/div/input')
ph_box.send_keys(phnumber)

# address
browser.find_element_by_xpath(
    '/html/body/app-root/app-home/div[3]/div/app-passenger-input/div[5]/form/div/div[1]/div[8]/p-panel/div/div[2]/div/app-address-capture/div/div[1]/input').send_keys("44 Goutam Buddha Marg")
browser.find_element_by_xpath(
    '/html/body/app-root/app-home/div[3]/div/app-passenger-input/div[5]/form/div/div[1]/div[8]/p-panel/div/div[2]/div/app-address-capture/div/div[2]/input').send_keys("C-zone")
browser.find_element_by_xpath(
    '/html/body/app-root/app-home/div[3]/div/app-passenger-input/div[5]/form/div/div[1]/div[8]/p-panel/div/div[2]/div/app-address-capture/div/div[4]/input').send_keys("713205")
browser.find_element_by_xpath(
    '/html/body/app-root/app-home/div[3]/div/app-passenger-input/div[5]/form/div/div[1]/div[8]/p-panel/div/div[2]/div/app-address-capture/div/div[6]/select').click()
time.sleep(3)
browser.find_element_by_xpath(
    '/html/body/app-root/app-home/div[3]/div/app-passenger-input/div[5]/form/div/div[1]/div[8]/p-panel/div/div[2]/div/app-address-capture/div/div[7]/select').click()
time.sleep(3)

# payment
browser.find_element_by_xpath(
    '/html/body/app-root/app-home/div[3]/div/app-passenger-input/div[5]/form/div/div[1]/div[14]/p-panel/div/div[2]/div/table/tr[2]/label/p-radiobutton/div/div[2]').click()
time.sleep(15)  # for checking

# continue
browser.find_element_by_xpath(
    '/html/body/app-root/app-home/div[3]/div/app-passenger-input/div[5]/form/div/div[1]/div[16]/div/button[2]').click()
time.sleep(5)

# final captcha
browser.find_element_by_xpath(
    '/html/body/app-root/app-home/div[3]/div/app-review-booking/div[4]/div/div[1]/form/div[1]/div/div/app-nlp-captcha/div/div[2]/div/div[3]/div[1]/input').send_keys("")
time.sleep(7)

# final continue
browser.find_element_by_xpath(
    '/html/body/app-root/app-home/div[3]/div/app-review-booking/div[4]/div/div[1]/form/div[2]/div/button[2]').click()
time.sleep(10)

browser.close()
print("\nSuccessfully Booked Ticket.... Happy Journey....")
