from selenium import webdriver
import pandas as pd
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def extract_targets():
    workbook = pd.read_excel('whatsappauto.xlsx')
    # workbook.head()
    return (workbook['Names'], workbook['Number'])


# load the cache and the cookies of the chrome browser
options = webdriver.ChromeOptions()
options.add_argument(
    r'user-data-dir=C:/Users/adity/AppData/Local/Google/Chrome/User Data')

# opens chrome automatically using Chrome-webdriver
driver = webdriver.Chrome('chromedriver.exe', chrome_options=options)
# driver.get('https://web.whatsapp.com/')
wait_time = WebDriverWait(driver, 6000)

target_values = extract_targets()
# print(target_values)
names = target_values[0]
numbers = target_values[1]
# print(names)
# print(numbers)

for i in range(len(names)):
    name = names[i]
    number = numbers[i]
    print(name, " = ", number)

    # opening a new tab
    driver.execute_script("window.open('about:blank', 'tab2');")
    driver.switch_to.window("tab2")

    # opening the whatsapp chat
    url = 'https://web.whatsapp.com/send?phone=91'+str(number)
    driver.get(url)

    msg_box_path = '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
    msg_box = wait_time.until(
        ec.presence_of_element_located((By.XPATH, msg_box_path)))
    msg_box.click()
    msg = "Hello, " + name + \
        ". I am Gideon. I would like to *seek permission before spamming.*\n_*Plz reply ASAP.*_"
    msg_box.send_keys(msg + Keys.ENTER)
    time.sleep(20)
driver.close()
print("Job Done")
