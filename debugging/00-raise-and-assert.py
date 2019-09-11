'''
saving error messages to a file 
using the traceback module
'''
import traceback

try:
    raise Exception("A custom error message")
except:
    errorFile = open('debugging\\error_log.txt', 'a') # open in append mode so we can keep all error records
    errorFile.write( traceback.format_exc()) # write the traceback exception to the file
    errorFile.write('\n')
    errorFile.close()

'''
assert False, "Error message here"

if the condition following the keyword assert 
evaluates to False, raise the error message

assert is for programmer errors not user errors
is for detecting potential bugs in our code
and they should crash our programs
letting us find our errors sooner rather than later 
'''

Blvd_and_80th = {'ns':'green', 'we':'red'}

def switchLights(intesection):
    for key in intesection.keys():
        if intesection[key] == 'green':
            intesection[key] = 'yellow'
        elif intesection[key] == 'yellow':
            intesection[key] = 'red'
        elif intesection[key] == 'red':
            intesection[key] = 'green'
        
print( Blvd_and_80th )
switchLights(Blvd_and_80th)
print( Blvd_and_80th )

'''
output:
{'ns': 'green', 'we': 'red'}
{'ns': 'yellow', 'we': 'green'}

the previous example logic is faulty as we can see
there are no red lights in either direction.
But there are no errors thrown, because there are no syntax errors
It's our mistake.
But we might have not noticed until we run the script
a couple times. Especially if we only called our function and 
didnt use print() to check the before and after values

we can make sure we get a heads up early by writing
an assert statement
'''
# the same faulty logic is present here, we just crash and print a message letting us know
Blvd_and_80th = {'ns':'green', 'we':'red'}

def switchLights(intesection):
    for key in intesection.keys():
        if intesection[key] == 'green':
            intesection[key] = 'yellow'
        elif intesection[key] == 'yellow':
            intesection[key] = 'red'
        elif intesection[key] == 'red':
            intesection[key] = 'green'
        assert 'red' in intesection.values(), "NEITHER LIGHT IS RED IN THE INTERSECTION!"+str(intesection) # if 'red' is not in either value of the intesection
        
switchLights(Blvd_and_80th)


  