'''
where the search() method will return the first instance
of the matching text
the findall() method will return every match of the searched
string as a list
if there is only one group returns a list of the groups
if there are 2 or more groups in the regex the findall method
will return a list of tuples
'''
import re

phnum = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
m = phnum.search("blah 444-444-7777 blah 789-456-1122 blah 456-789-3322")
print(m.group()) # 444-444-7777

phnum = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
m = phnum.findall("blah 444-444-7777 blah 789-456-1122 blah 456-789-3322")
print(m) # ['444-444-7777', '789-456-1122', '456-789-3322']

phnum = re.compile(r"(\d\d\d)-\d\d\d-\d\d\d\d")
m = phnum.findall("blah 444-444-7777 blah 789-456-1122 blah 456-789-3322")
print(m) # ['444', '789', '456']

phnum = re.compile(r"(\d\d\d)-(\d\d\d)-(\d\d\d\d)")
m = phnum.findall("blah 444-444-7777 blah 789-456-1122 blah 456-789-3322")
print(m) # [('444', '444', '7777'), ('789', '456', '1122'), ('456', '789', '3322')]

phnum = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d\d)")
m = phnum.findall("blah 444-444-7777 blah 789-456-1122 blah 456-789-3322")
print(m) # [('444', '444-7777'), ('789', '456-1122'), ('456', '789-3322')]

phnum = re.compile(r"((\d\d\d)-(\d\d\d-\d\d\d\d))")
m = phnum.findall("blah 444-444-7777 blah 789-456-1122 blah 456-789-3322")
print(m) # [('444-444-7777', '444', '444-7777'), ('789-456-1122', '789', '456-1122'), ('456-789-3322', '456', '789-3322')]

'''
character classes

\d numeric digits 0 to 9
\D any char that's NOT a numeric digit 0 to 9
\w any letter, numeric digit or underscore
\W any char that's NOT a letter, numeric digit or underscore
\s any space tab or new line
\S any char that's NOT a space tab or new line
'''
xmasRegex = re.compile(r'\d+\s\w+') # this will match 1 or more digits followed by a space followed by 1 or more letters
m = xmasRegex.findall('12 drummers drumming, 11 pipers piping, ..., 3 hens blah, 2 doves blah, 1 partridge blah')
print(m) # ['12 drummers', '11 pipers', '3 hens', '2 doves', '1 partridge']

#notice that '12 drummers drumming' returns '12 drummers' the match stops at the space char

######### creating your own character class
'''
the character classes might be to broad sometimes
\w searches for any letter, but what if we are 
only searching for vowels?
you can define your own character class using brackets []
'''
vowelRegex = re.compile(r'[aeiouAEIOU]') # this will match any vowel in a string
m = vowelRegex.findall('12 drummers drumming, 11 pipers piping, ..., 3 hens blah, 2 doves blah, 1 partridge blah')
print(m) # ['u', 'e', 'u', 'i', 'i', 'e', 'i', 'i', 'e', 'a', 'o', 'e', 'a', 'a', 'i', 'e', 'a']

'''
what if we want to search for non-vowel chars?
we can use the caret sign ^
to make a negative character class
matching all the characters not in the class
'''
notvowelRegex = re.compile(r'[^aeiouAEIOU]') # this will match any non vowel char in a string
m = notvowelRegex.findall('12 drummers drumming, 11 pipers piping, ..., 3 hens blah, 2 doves blah, 1 partridge blah')
print(m) # ['1', '2', ' ', 'd', 'r', 'm', 'm', 'r', 's', ' ', 'd', 'r', 'm', 'm', 'n', 'g', ',', ' ', ........, ',', ' ', '1', ' ', 'p', 'r', 't', 'r', 'd', 'g', ' ', 'b', 'l', 'h']
