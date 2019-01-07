#! python3
# Program prompts user for ProtonMail credentials and sends message to a select
# recipient with specified subject.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

def ProtonMailer(username, password, recipient, subject, message):
    try:
        browser = webdriver.Chrome()
        browser.get('https://mail.protonmail.com/login')
        usernameElem = browser.find_element_by_id('username')
        passwordElem = browser.find_element_by_id('password')
        usernameElem.send_keys(username)
        passwordElem.send_keys(password)
        browser.find_element_by_id('login_btn').click()
        sleep(15)
        browser.find_element_by_css_selector('section button').click()
        sleep(5)
        browser.switch_to.active_element.send_keys(recipient + Keys.ENTER + '\t')
        sleep(2)
        browser.switch_to.active_element.send_keys(subject + '\t' + message + '\t' + '\t' + '\t' + '\t' + '\t' + '\t' + Keys.ENTER)
        sleep(5)
        browser.quit()
        print('Email sent!')
    except Exception as err:
        browser.quit()
        print('An error occurred while sending email:')
        print(str(err))

print('Welcome to ProtonMail.')
print('Please enter your username:')
username = input()
print('Please enter your password:')
password = input()
print("Please enter the recipient's email address:")
recipient = input()
print('Please enter the subject:')
subject = input()
print('Please enter the message:')
message = input()

ProtonMailer(username, password, recipient, subject, message)
