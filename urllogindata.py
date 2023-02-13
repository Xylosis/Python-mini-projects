from selenium import webdriver
from selenium.webdriver.common.by import By

def login(url, username, password, HTMLelementIDuser, HTMLelementIDpass,HTMLelementIDlogin):
    browser = webdriver.Firefox()
    browser.get((url))
    user = browser.find_element(By.ID, HTMLelementIDuser)
    user.send_keys(username)
    passWord = browser.find_element(By.ID, HTMLelementIDpass)
    passWord.send_keys(password)
    if HTMLelementIDlogin != None:
        htmllogin = browser.find_element(By.CLASS_NAME, HTMLelementIDlogin)
        htmllogin.click()

