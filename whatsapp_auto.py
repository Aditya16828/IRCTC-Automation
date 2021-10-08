import time
import autoit
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument(r'--user-data-dir=C:/Users/ADITYA MUKHERJEE/AppData/Local/Google/Chrome/User')
options.add_argument('--profile-directory=Default')
browser = webdriver.Chrome(options=options)

loc = "A:/whatsappauto.xlsx"
df = pd.read_excel(loc, engine='openpyxl')
for i in range(len(df)):
    name = df.iloc[i, 0]
    number = df.iloc[i, 1]
    browser.execute_script("window.open('about:blank', 'tab2');")
    browser.switch_to.window("tab2")
    url = 'https://web.whatsapp.com/send?phone=91' + str(number)
    try:
        browser.get(url)
    except:
        continue
    time.sleep(15)
    try:
        msz_box = browser.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]")
    except:
        continue
    msz = "Hi, " + name + ". \nI am GIDEON sending u msg from ADITYA'S System."
    msz_box.send_keys(msz)
    send_button_msz = browser.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[3]')
    send_button_msz.click()

    time.sleep(5)

    """clip = browser.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[1]/div[""2]/div/div/span")
    clip.click()
    time.sleep(1)
    img_box = browser.find_element_by_xpath(
        "/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[1]/div[2]/div/span/div[1]/div/ul/li["
        "1]/button/span")
    # time.sleep(2)
    img_box.click()
    time.sleep(2)
    autoit.control_focus("Open", "Edit1")
    autoit.control_set_text("Open", "Edit1", "partha")
    autoit.control_click("Open", "Button1")
    time.sleep(1)
    send_button_img = browser.find_element_by_xpath(
        '/html/body/div/div[1]/div[1]/div[2]/div[2]/span/div[1]/span/div[1]/div/div[2]/span/div/div/span')
    send_button_img.click()
    time.sleep(2)

    msz_box = browser.find_element_by_xpath(
        '/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]')
    msz = ("*STEPS -                                                                                                 \n"
           "                       * 1. Give test and finish it within 30min - *test link - \n"
           "https://forms.office.com/r/L2pk8mh8A2*                                                         \n "
           "2. Our team will get back to you if you perform well!                                \n "
           "3. We will provide you coupon also for availing discounts *based \n "
           "on your performance.*                                              \n "
           "4. visit \n "
           "classroomstudy.org and register for 2 year PARTHA program.                             *Ask your queries "
           "here - https://t.me/classroomstudy09*                                                   *-classRoomSTudy* "
           "")
    msz_box.send_keys(msz)
    send_button_msz = browser.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[3]')
    send_button_msz.click()
    time.sleep(2)"""

browser.close()
print("I did my service of sending messages!")
