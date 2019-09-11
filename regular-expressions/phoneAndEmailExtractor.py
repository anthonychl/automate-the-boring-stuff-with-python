'''
finds phone numbers and emails in the clipboard
'''
import re
import pyperclip # pyperclip allows to copy/paste from/to the clipboard

phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))?           # area code
(\s|-|\.)?                   # separator
(\d{3})                      # first 3 digits
(\s|-|\.)                    # separator
(\d{4})                      # last 4 digits
(\s*(ext|x|ext.)\s*\d{2,5})? # extension
)''', re.VERBOSE)

emailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+    # username
@                    # @ symbol
[a-zA-Z0-9.-]+       # domain name
(\.[a-zA-Z]{2,4})    # dot-something
)''', re.VERBOSE)

# find matches in the clipboard text
text = str(pyperclip.paste()) # casting to string the content of the clipboard and storing it in the 'text' variable
matches = [] # a new list to store the matches we find
for groups in phoneRegex.findall(text): # search for phone numbers 
    phoneNum = '-'.join([groups[1], groups[3], groups[5]]) # group[1] is area code, group[3] is first 3 digits, group[5] is last 4 digits
    if groups[6] != '': # if an extension number exists add it to the phone number
        phoneNum += ' x ' + groups[6]
    matches.append(phoneNum)
for group in emailRegex.findall(text): # search for emails
    matches.append(group[0]) # group[0] is the entire email

# copy the results to the clipboard
if len(matches) > 0 :
    pyperclip.copy('\n'.join(matches)) # add every match in a new line
    print('Copied to clipboard')
    print('\n'.join(matches))
else:
    print('No phone numbers or emails found')

