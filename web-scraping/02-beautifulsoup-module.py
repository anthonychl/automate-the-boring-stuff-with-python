# pip install beautifulsoup4
import bs4 # beautifulsoup4
import requests

res = requests.get('https://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994')
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, "html.parser") # returns a beautifulsoup object
# we want to pass html.parser as a second argument or else it'll throw a warning
# bs4 can parse some things other than html so we better specify it, the markup type.

# to find a section on a web page we use select()
elements = soup.select('#buyNewSection > h5 > div > div.a-column.a-span8.a-text-right.a-span-last > div > span.a-size-medium.a-color-price.offer-price.a-text-normal')
'''
we must do it the first time manually if we dont know the css path before hand.

we can go to the web page, inspect an element
and then on the source code right click and copy css path
or copy selector or css selcetor ...
it may vary according to the browser.

then we paste it in the select() method as we see above

select() will grab all the matching elements 
in this example the element is unique
but if we select <p> tags we might get multiple matches
'''
print(elements[0]) # <span class="a-size-medium a-color-price offer-price a-text-normal">$19.66</span>

# it also conatains a variable with just the text inside the html tags
print(elements[0].text) # $19.66

'''
in case the 'text' has a lot of empty spaces ie:
'\t \t \n \n   \n     \t  $19.66   \n   \n   \t \n'

we could call the strip() method on it:
print(elements[0].text.strip()) # $19.66
'''