from os.path import dirname
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
import random
import time
import string
import secrets
import os

chrome_options = Options()
chrome_options.add_extension('extension_1_3_1_0.crx')

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options) # USES CHROMEDRIVERMANAGER TO AUTO UPDATE CHROMEDRIVER

def gen():
    # GENERATE PASSWORD
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(16))
    # PASSWORD GENERATION FINISHED

    # NAME GENERATION
    driver.get('https://en.wikipedia.org/wiki/Special:Random')
    temp = driver.find_element_by_class_name("firstHeading").text
    for char in string.punctuation:
        temp = temp.replace(char, '') #REMOVES ALL PUNCTUATION
    for char in string.digits:
        temp = temp.replace(char, '') #REMOVES SPACES
    temp = "".join(filter(lambda char: char in string.printable, temp)) #REMOVES NON ASCII CHARACTERS
    name = ''.join(temp.split())
    name = name[:random.randint(5,7)] #KEEPS 5 TO 7 LETTERS OF THE ORIGINAL STRING


    randomNumber = random.randint(10000,99999)


    finalName = name+str(randomNumber)
    time.sleep(1)
    # NAME GENERATION FINISHED

    # REDDIT ACCOUNT CREATION
    driver.get('https://www.reddit.com/register/')
    driver.find_element_by_id('regEmail').send_keys('pixelbotdev@protonmail.com')
    time.sleep(1)
    driver.find_element_by_xpath ("//button[contains(text(),'Fortsetzen')]").click()
    time.sleep(3)
    driver.find_element_by_id('regUsername').send_keys(finalName)
    driver.find_element_by_id('regPassword').send_keys(password)
    os.system('cls' if os.name=='nt' else 'clear')
    print("Please solve the Capture either manually or by pressing the Captcha Buster Button")

    dirname = os.path.dirname(__file__)
    text_file_path = os.path.join(dirname, 'namesforreddit.txt')
    text_file = open(text_file_path, "a")
    text_file.write("USR: " + name + str(randomNumber) + " PWD: " + password) #OUTPUTS NAME AND NUMBER
    text_file.write("\n")
    text_file.close()

if __name__ == '__main__':
    amount = 0
    while True:
        os.system(f'title Accounts Created:{amount}')
        gen()
        amount += 1
        print("Press Any Key to start the Process Again")
        input()
        os.system('cls' if os.name=='nt' else 'clear')
        driver.delete_all_cookies()

# driver.close()