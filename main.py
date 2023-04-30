import time, webbrowser, sys
import os
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from dec import *
from webdriver_manager.chrome import ChromeDriverManager
'''email = input("Enter the email: ")
password = input("Enter the password: ")
theory = int(input("Enter the number of theory subjects: "))
labs = int(input("Enter the number of lab subjects: "))
comment = input("Enter the comment: ")'''
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.get("https://academia.srmist.edu.in/#Course_Feedback")
for keys in email:
    pyautogui.press(keys)
pyautogui.press("enter")
time.sleep(3)
for keys in password:
    pyautogui.press(keys)
pyautogui.press("enter")

time.sleep(30)
for i in range(theory):
    for j in range(14):
        if j == 0:
            pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("enter")
        time.sleep(3)
        pyautogui.press("down")
        pyautogui.press("enter")

    pyautogui.press("tab")
    for keys in comment:
        pyautogui.press(keys)
pyautogui.press("tab")
for i in range(labs):
    for j in range(13):
        if j == 0:
            pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("enter")
        time.sleep(3)
        pyautogui.press("down")
        pyautogui.press("enter")

    pyautogui.press("tab")
    for keys in comment:
        pyautogui.press(keys)
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(15)




