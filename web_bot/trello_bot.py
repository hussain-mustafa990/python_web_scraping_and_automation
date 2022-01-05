from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from datetime import date
import os
import json

CHROME_DRIVER_PATH = os.path.join(os.getcwd(), "chromedriver")
OP = webdriver.ChromeOptions()
OP.add_argument('--headless')
DRIVER = webdriver.Chrome(CHROME_DRIVER_PATH)


def screenshotPage():
    time.sleep(2)
    date_str = date.today().strftime("%m-%d-%Y")
    fpath = os.path.join(os.getcwd(), 'downloads/{}.png'.format(date_str))
    DRIVER.get_screenshot_as_file(fpath)


def addTask():
    time.sleep(2)
    DRIVER.find_element(
        By.XPATH, value="//textarea[@aria-label='To Do']/ancestor::div/descendant::div[@class='card-composer-container js-card-composer-container']/child::a").click()
    task_text_area = DRIVER.find_element(
        By.XPATH, value="//div[@class='card-composer']/descendant::textarea")
    task_text_area.clear()
    task_text_area.send_keys("Bot Added Task")
    DRIVER.find_element(By.XPATH, value="//input[@value='Add card']").click()
    time.sleep(5)


def login():
    with open('config.json') as configFile:
        credentials = json.load(configFile)
        time.sleep(2)
        DRIVER.find_element(By.XPATH, value="//a[@href='/login']").click()
        time.sleep(2)
        username = DRIVER.find_element(
            By.CSS_SELECTOR, value="input[name='user']")
        password = DRIVER.find_element(
            By.CSS_SELECTOR, value="input[name='password']")
        username.clear()
        password.clear()
        username.send_keys(credentials["USERNAME"])
        password.send_keys(credentials["PASSWORD"])
        DRIVER.find_element_by_css_selector("input[type='submit']").click()
        time.sleep(5)
        password = DRIVER.find_element(
            By.CSS_SELECTOR, value="input[name='password']")
        password.clear()
        password.send_keys(credentials["PASSWORD"])
        time.sleep(5)
        DRIVER.find_element_by_css_selector("button[type='submit']").click()


def navigateToBoard():
    time.sleep(5)
    DRIVER.find_element(
        By.XPATH, value="//div[@title='{}']/ancestor::a".format('Bot Board')).click()
    time.sleep(5)


def main():
    try:
        DRIVER.get("https://trello.com")
        login()
        navigateToBoard()
        addTask()
        screenshotPage()
        input("Bot Operation Completed. Press any key...")
        DRIVER.close()
    except Exception as e:
        print(e)
        DRIVER.close()


if __name__ == "__main__":
    main()
