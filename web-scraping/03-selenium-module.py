# controlling the browser using the selenium module
# pip install selenium
# we must have Firefox and the geckodriver (geckodriver.exe must be added to the PATH)

from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://automatetheboringstuff.com')

# assigning an element ( in this case a link) on the page, based on its CSS selector, to a variable.  
element = browser.find_element_by_css_selector('.main > div:nth-child(1) > ul:nth-child(19) > li:nth-child(1) > a:nth-child(1)')
# executing action on the element
element.click()

elems = browser.find_elements_by_css_selector('p') #this returns a list of all the elements that match that selector, in this case <p></p>
print( len(elems) ) # amount of elements in the list



browser.get('https://stackoverflow.com')
# finding elements and sending data 
'''
this could be used for a comment section
to fill user and passwords fields etc

in this case is a search element
'''
searchElem = browser.find_element_by_css_selector('#search > div > input')
searchElem.send_keys('selenium') # look for selenium on stackoverflow
searchElem.submit()

# playing around with the browser
browser.refresh()
browser.back()
browser.forward()
# browser.quit()

# grabing text
browser.get('https://automatetheboringstuff.com')
var = browser.find_element_by_css_selector('p') # the first paragraph
print( var.text )