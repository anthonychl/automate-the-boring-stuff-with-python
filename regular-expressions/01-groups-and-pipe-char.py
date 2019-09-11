'''
we can split our matches in groups

let's say we want to find a phone number in a string
but also be able to grab just the area code
because we need to count how many numbers are from
that area for example.

we can do this by using parentheses in our pattern
to make groups
'''
import re

phNumber = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d\d)") # one group would be the area code and the other the rest of the number
match = phNumber.search("My number is 444-888-8888") # notice how in the string provided there are no parentheses
print(match.group()) # this shows the entire match. the phone number
print(match.group(1)) # this shows the first group. the area code
print(match.group(2)) # # this shows the second group. the last 7 digits

# if we want to match actual parentheses we need to use a \ before them in the regex ie:
phNumber = re.compile(r"(\(\d\d\d\))-(\d\d\d-\d\d\d\d)") # theres a set of parentheses for the area code group and another set \(XXX\) that's part of the pattern we want to match 
m = phNumber.search("My number is (444)-888-8888") 
print(m.group(0)) # (444)-888-8888 calling group() or group(0) returns the entire match
print(m.group(1)) # (444)
print(m.group(2)) # 888-8888

'''
let's say we want to find similar words that share
the same prefix for example 
batman
batmobile
batwoman 
'''
batRegex = re.compile(r'Bat(man|mobile|cave|woman)') # they share the prefix Bat and we give the suffix options with the pipe character |
m = batRegex.search(" Batman and Batwoman in a Batmobile getting out of the Batcave")
print(m.group()) # Batman


batRegex = re.compile(r'Bat(man|mobile|cave|woman)') # they share the prefix Bat and we give the suffix options with the pipe character |
m = batRegex.findall(" Batman and Batwoman in a Batmobile getting out of the Batcave")
print(m) # ['man', 'woman', 'mobile', 'cave']
