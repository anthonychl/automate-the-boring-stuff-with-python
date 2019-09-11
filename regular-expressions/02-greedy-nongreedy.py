import re

#####################  ()?
batRegex = re.compile(r'Bat(wo)?man') # the ()? means that whatever is inside the paretheses can appear once or not at all
m = batRegex.findall(" Batman and Batwoman in a Batmobile getting out of the Batcave")
print(m) # ['', 'wo']

batRegex = re.compile(r'Bat(wo)?man') # the ()? means that whatever is inside the paretheses can appear once or not at all, its optional
m = batRegex.search(" Batman getting out of the Batcave")
print(m.group()) # Batman

batRegex = re.compile(r'Bat(wo)?man') # the ()? means that whatever is inside the paretheses can appear once or not at all
m = batRegex.search(" Batwoman getting out of the Batcave")
print(m.group()) # Batwoman

batRegex = re.compile(r'Bat(wo)?man') # the ()? means that whatever is inside the paretheses can appear once or not at all
m = batRegex.search(" Batwowowowoman getting out of the Batcave")
if m == None: # because ()? only catches zero or one ocurrence of whats inside, in this case 'wo'
    print('no match')

phNumber = re.compile(r"(\d\d\d-)?(\d\d\d-\d\d\d\d)") # making the area code optional
m = phNumber.search(" Bruce Wayne's phone number is 555-444-3333")
print(m.group()) # 555-444-3333

phNumber = re.compile(r"(\d\d\d-)?(\d\d\d-\d\d\d\d)") # making the area code optional
m = phNumber.search(" Bruce Wayne's phone number is 444-3333")
print(m.group()) # 444-3333

#####################  ()*
batRegex = re.compile(r'Bat(wo)*man') # the ()* means that whatever is inside the paretheses can appear zero or more times
m = batRegex.search(" Batman getting out of the Batcave")
print(m.group()) # Batman

batRegex = re.compile(r'Bat(wo)*man') 
m = batRegex.search(" Batwoman getting out of the Batcave")
print(m.group()) # Batwoman

batRegex = re.compile(r'Bat(wo)*man') 
m = batRegex.search(" Batwowowowoman getting out of the Batcave")
print(m.group()) # Batwowowowoman

#####################  ()+
batRegex = re.compile(r'Bat(wo)+man') # the ()+ means that whatever is inside the paretheses must appear at least once
m = batRegex.search(" Batman getting out of the Batcave")
if m == None: # because ()+ needs at least one occurrence of 'wo'
    print('no match')

batRegex = re.compile(r'Bat(wo)+man') 
m = batRegex.search(" Batwoman getting out of the Batcave")
print(m.group()) # Batwoman

batRegex = re.compile(r'Bat(wo)+man') 
m = batRegex.search(" Batwowowowoman getting out of the Batcave")
print(m.group()) # Batwowowowoman

########### escaping special characters using \
rx = re.compile(r"\+\*\?")
m = rx.search("I learned about the use of +*? characters in regular expressions")
print(m.group()) # +*?

########### specific repetitions
'''
lets say we want to match a specific amount of
repetitions of a certain pattern
we use curly brackets to set the amount ie:
regex = re.compile(r"(Ha){3}") 
this would match HaHaHa
'''
phNumbers = re.compile(r"((\d\d\d\-)?(\d\d\d-\d\d\d\d(,)?)){3}") # this regex would match up to 3 phone numbers( with optional area code) separated by comma
m = phNumbers.search("My phone numbers are 444-777-8888,555-5555,414-777-9999")
print(m.group()) # 444-777-8888,555-5555,414-777-9999

'''
we can also use curly brackets to set the boundaries
the min and max amount of repetitions
'''
regex = re.compile(r"(Ha){3,5}") # pattern 'Ha', we want the matches that repeat 3 to 5 times the pattern
m = regex.search("that made me laugh HaHa HaHaHa")
print(m.group()) # it will match HaHaHa. Not HaHa

regex = re.compile(r"(Ha){3,5}") # pattern 'Ha', we want the matches that repeat 3 to 5 times the pattern
m = regex.search("that made me laugh HaHa HaHaHaHaHa")
print(m.group()) # it will match HaHaHaHaHa. Not HaHa

'''
greedy vs nongreedy:

regular expressions are set greedy by default 
this means they will match the longest string possible 
in ambiguous situations
declaring a nongreedy regex will match the shortest 
string possible
'''

greedyRegex = re.compile(r"(Ha){3,5}")
m = greedyRegex.search("HaHaHaHaHaHaHa")
print(m.group()) # HaHaHaHaHa the longest string possible given the boundaries

nongreedyRegex = re.compile(r"(Ha){3,5}?") # using ? for nongreedy
m = nongreedyRegex.search("HaHaHaHaHa")
print(m.group()) # HaHaHa the shortest string possible given the boundaries

'''
notice how the ? character has two meanings in regex, 
declaring a nongreedy match
or flagging an optional group

we can also just set one of the limits:
Regex = re.compile(r"(Ha){3,}") this means 3 or more

Regex = re.compile(r"(Ha){,5}") this means up to 5
'''



