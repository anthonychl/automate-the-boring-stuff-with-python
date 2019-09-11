# search stackOverflow 
# pip install selenium    beforehand
# we must have Firefox and the geckodriver (geckodriver.exe must be added to the PATH)

import sys, pyperclip
from selenium import webdriver

if len(sys.argv) > 1: 
    subject = ' '.join(sys.argv[1:]) # the search text starts from 1  
else:
    subject = pyperclip.paste()

browser = webdriver.Firefox()
browser.get('https://stackoverflow.com')

searchElem = browser.find_element_by_css_selector('#search > div > input')
searchElem.send_keys(subject) # look for selenium on stackoverflow
searchElem.submit()