import time
import autoit
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
# loads cookies and data of our chrome browser
options.add_argument(
    r'user-data-dir=C:/Users/adity/AppData/Local/Google/Chrome/User Data')
options.add_argument(r'--profile-directory=Default')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome('chromedriver.exe', chrome_options=options)

# print('Browser opened')

loc = r"D:/Python Automation/whatsappauto.xlsx"
df = pd.read_excel(loc, engine='openpyxl')
print(df)
for i in range(len(df)):
    name = df.iloc[i, 0]
    number = df.iloc[i, 1]
    print("Opening tab")
    # browser.execute_script("window.open('about:blank', 'tab2');")
    # browser.switch_to.window("tab2")
    url = r"https://web.whatsapp.com/send?phone=91" + str(number)
    try:
        browser.get(url)
        print("bbb")
    except:
        continue
    time.sleep(20)
    try:
        msz_box = browser.find_element_by_xpath(
            r'/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div')
        print("Finding msg box")
    except:
        continue
    msz = "Hi, " + name + ". \nI am GIDEON sending u msg from ADITYA'S System."
    msz_box.send_keys(msz)
    send_button_msz = browser.find_element_by_xpath(
        r'/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')
    send_button_msz.click()

    time.sleep(5)
browser.close()
print("I did my service of sending messages!")
