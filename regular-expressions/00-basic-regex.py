# basic regular expressions
'''
the next function is an example of how long
and complicated can get just checking if 
a string is a phone number 
'''

def isPhoneNumber(text):
    if len(text) != 12:
        return False # not a phone number
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False # no area code
    if text[3] != '-':
        return False # no - after area code
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False # no first 3 digits
    if text[7] != '-':
        return False # no - after first 3 digits
    for i in range(8, 11):
        if not text[i].isdecimal():
            return False # no last 4 digits
    return True
    
print('is it a phone number? :'+ str( isPhoneNumber("305-123-1234") ) )

'''
 but what if the string is much longer? 
 we'd have to check 12 chars chunks of the string
 until the end o it
'''
foundNumber = False
string = "Hello blah blah ... call me at 305-555-9998 or at 305-555-8888"

for i in range(0,len(string)):
    chunck = string[i:i+12]
    if isPhoneNumber(chunck):
        print('Phone Number found: '+chunck)
        foundNumber = True
if not foundNumber:
    print('No phone number found')

    
#---------------------------------------------------------
'''
regular expresions help simplify
our code compared to the previous
example, and even with more complex
patterns than a phone number's
'''
import re # regular expressions lib

phnumber = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d") # \d is for single digit. phnumber is a regex object with the pattern we passed it
check_pattern = phnumber.search("call me at 305-444-5555") # check if the string inserted fits the pattern. regex objects have the method search() to do this
print(check_pattern) # shows the span where the string matches the pattern ie: span(7,19), and shows the string that matched
print(check_pattern.group())  # group() grabs the match, this line works if there's a match, if not it throws an error

check_pattern2 = phnumber.findall("call me at 305-444-5555 or at 305-481-8888") # while search() only returns the first occurrence of the pattern, findall() returns a list of them all
print(check_pattern2) #we dont need the group() method here

