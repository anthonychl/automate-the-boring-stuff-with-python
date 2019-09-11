###########  ^ and $
'''
the caret and dollar Sign characters

You can also use the caret symbol (^) at the start of a regex to indicate that
a match must occur at the beginning of the searched text. Likewise, you can
put a dollar sign ($) at the end of the regex to indicate the string must end
with this regex pattern. And you can use the ^ and $ together to indicate
that the entire string must match the regex—that is, it’s not enough for a
match to be made on some subset of the string
'''

import re

beginsWithHello = re.compile(r'^Hello')
m = beginsWithHello.search('Hello world!')
print(m.group())

endsWithNumber = re.compile(r'\d$')
m = endsWithNumber.search('Your number is 42')
print(m.group())

wholeStringIsNum = re.compile(r'^\d+$')
m = wholeStringIsNum.search('1234567890')
print(m.group())

############# .

'''
the wildcard character

The . (or dot) character in a regular expression is called a wildcard and will
match any character except for a newline.
'''
atRegex = re.compile(r'.at')
m = atRegex.findall('The cat in the hat sat on the flat mat.')
print(m) # ['cat', 'hat', 'sat', 'lat', 'mat']

'''
the dot character will match just one character, which
is why the match for the text flat in the previous example matched only lat.
To match an actual dot, escape the dot with a backslash: \.
'''

############ .*
'''
Matching Everything with Dot-Star .*

Remember that the
dot character means 
“any single character except the newline,”
and the star character means 
“zero or more of the preceding character.”
'''
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.group(1))
print(mo.group(2))

'''
The dot-star uses greedy mode: It will always try to match as much text as
possible. To match any and all text in a nongreedy fashion, use the dot, star,
and question mark (.*?)
'''
nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
print(mo.group()) # <To serve man>

greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
print(mo.group()) # <To serve man> for dinner.>

'''
Matching Newlines with the Dot Character

The dot-star will match everything except a newline. By passing re.DOTALL as
the second argument to re.compile(), you can make the dot character match
all characters, including the newline character.
'''
noNewlineRegex = re.compile('.*')
print(noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()) # Serve the public trust.

newlineRegex = re.compile('.*', re.DOTALL)
print(newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()) 
# Serve the public trust.
# Protect the innocent.
# Uphold the law.

############ Case insensitive matching 
'''
making a regex case insensitive
using the arguments re.I or re.IGNORECASE
'''
caseInsensitive = re.compile(r"[aeiou]", re.I)
m = caseInsensitive.findall("hello WORLD I am Anthony")
print(m) # ['e', 'o', 'O', 'I', 'a', 'A', 'o']