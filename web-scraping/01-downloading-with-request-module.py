# we need the third party module 'requests'. read more on requests.readthedocs.org
# pip install requests
import requests


'''
 to download a file

 the get() method returns a response object
 it contains the response the server gave for this request

 we can check the response status too
'''
res = requests.get('http://automatetheboringstuff.com/files/rj.txt')
print( res.status_code ) # 200 is ok

# if the requests succeded the downloaded web page is on the response 'text' variable
# res.text 

print ( len( res.text ) )
print( res.text[:500] )

# lets say we sent a request to a file that didnt exist
BadRes = requests.get('http://automatetheboringstuff.com/filessss/rrrrj.txt')
# BadRes.raise_for_status() # we can use this to halt our program or wrap it in a try catch block to deal with it without crashing

# saving our download 
playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000): #  100k bytes
    playFile.write( chunk ) # writing 100000 bytes chunks at a time


playFile.close()

