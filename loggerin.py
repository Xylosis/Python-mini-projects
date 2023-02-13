#
from fileinput import filename
import webbrowser
#import pyautogui as ag
from pynput.keyboard import Key, Controller
from googlesearch import search
from selenium import webdriver
import urllogindata
import os

global filenametxt
filenametxt = "URLs.txt"

'''THIS PROGRAM IS GOING TO BE AN AUTO LOGIN FOR WEBSITES OR AUTOMATED THING FOR WEBSITES'''
'''STORE DATA IN FILES RESPECTIVE TO: WEBNAME, URL, USERNAME, PASSWORD, ELEMENT ID FOR USER,ELEMENT ID FOR PASSWORD, CLASS NAME FOR BUTTON'''
#ag.displayMousePosition()
keyboard = Controller()
#keyboard.type("Hello World")

#Change this if you use a different browser
webbrowser.Mozilla()

def checkFile(webname):
#check for duplicate URLs in the file
    urlFile = open(filenametxt, "r")
    contents = urlFile.readlines()
    urlFile.close()
    #index = 0
    for line in contents:
        if webname in line:
            return True, line
        #index += 1
    return False, None

def appendURLwLogin(webname, URL, user, passWord):
    urlFile = open(filenametxt,"a")
    urlFile.seek(0)
    urlFile.write("\n" + webname + " " + URL + " " + user + " " + passWord)
    urlFile.write("\n")
    urlFile.close()

def appendURL(webname,URL):
    urlFile = open(filenametxt,"a")
    urlFile.seek(0)
    urlFile.write("\n" + webname + " " + URL)
    urlFile.write("\n")
    urlFile.close()

def searchURL(webname):
    query = "{}".format(webname)
    for j in search(query, tld="co.in", num=1, stop=1):
        url = j
    return url

def openWebsite(url):
    webbrowser.open(url,new=2)

print("Type help to see commands, or enter the website name with an appropriate command following seperated by a space.")
while True:
    usrInput = input("Enter the website name with a command:\n")
    while usrInput == 'help' or usrInput == "Help":
        print("Commands: -l or -login to login to website, or -o or -open to just open website.")
        print("Here is an example line:\n [website name] -o")
        print("More features will be added soon.")
        usrInput = input("Enter the website name with a command:\n")
    try:
        webName, command = usrInput.split(" -")

    except ValueError:
        print("No command was issued, please enter a command after the webname.")
        print("Type help to see a list of commands.")
        continue
    break

while True:
    isinFile, line = checkFile(webName)
    if isinFile:
        splitLine = line.split(" ")
        url = splitLine[1]
        #url = splitLine[1]
        if command == 'l' or command == 'login':
            username = splitLine[2]
            password = splitLine[3]
            HTMLelementIDuser= splitLine[4]
            HTMLelementIDpassword = splitLine[5]
            try:
                HTMLelementLogin = splitLine[6]
            except IndexError:
                HTMLelementLogin = None
            urllogindata.login(url,username,password,HTMLelementIDuser,HTMLelementIDpassword,HTMLelementLogin)
            if HTMLelementLogin == None:
                keyboard.press(Key.enter)
            break

        elif command == 'o' or command == 'open':
            #url = "{}".format(input("Enter the URL\n"))
            openWebsite(url)
            break
        else:
            print("No command issued.")
            quit()
    else:
        if command == 'l' or command == 'login':
            url = searchURL(webName+" login")
            username = input("Please enter your username for the website.")
            password = input("Please enter your password for the website.")
            appendURLwLogin(webName, url, username, password)
            confirmation = input("Please add the HTML userid and passid to the notepad, then type '1'.")
            openWebsite(url)
            os.system("notepad.exe URLs.txt")
            if confirmation =='1':
                continue

        elif command == 'o' or command == 'open':
            url = searchURL(webName)
            appendURL(webName, url)
            openWebsite(url)
            break
        else:
            print("No command issued.")
            quit()

