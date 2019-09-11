'''
script to check the price of a product on amazon

run Win + R and type: getAmazonPrice https://www.amazon......

needs these modules to be pip installed beforehand
beatifulsoup4, requests and pyperclip modules

also the folder in which the .py and .bat files
are stored must be added to the path
'''

import bs4, requests, sys, pyperclip 

def getAmazonPrice( amazonUrl ):
    res = requests.get( amazonUrl )
    #res.raise_for_status()
    if res.status_code == 200:
        soup = bs4.BeautifulSoup(res.text, "html.parser")
        elements = soup.select('#buyNewSection > h5 > div > div.a-column.a-span8.a-text-right.a-span-last > div > span.a-size-medium.a-color-price.offer-price.a-text-normal')
        return res.status_code, elements[0].text.strip()
    else:
        return res.status_code, 'unavailable data, searching again for price' # a tuple


count = 0

for i in range(20):
    if len(sys.argv) > 1: 
        Url = sys.argv[1] # 0 should be getAmazonPrice.py and 1 the url
    else:
        Url = pyperclip.paste()

    status_price = getAmazonPrice(Url) 
    if status_price[0] == 200:
        print( status_price[1] ) # print price
        break
    else:
        print( status_price )
        count+=1
        print(f"on attempt number: {count} ")

if count == 20:
    print('-------------Data is unavailable try again later---------------')