'''
# a script that can run from the cmd
# take an address and look it up
# in a browser using google maps

import webbrowser, sys # cmd line arguments need the sys module

# the cmd line arguments are stored as a list in the sys.argv variable:
# sys.argv = ['mapit.py', '870', 'Valencia' 'St.']  It would look like that
# if we pressed Win + R and typed: mapit.py 870 Valencia St.

if len(sys.argv) > 1: # if at least two arguments were passed
    webbrowser.open('https://www.google.com/maps/place/'+' '.join(sys.argv[1:])) # opens the browser at this address https://www.google.com/maps/place/978+Valencia+St ....

# notice how the slice in sys.argv[1:] starts in 1, we dont want to add 'mapit.py' to the string which is in positon 0
'''
# if we want a script to run from the cmd line we must add the #!, also called 'shebang', at the top of the file and specify with program is running it
#! python3
import webbrowser, sys, pyperclip # the pyperclip module to add more functionality 

if len(sys.argv) > 1: 
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()
webbrowser.open('https://www.google.com/maps/place/'+ address)

'''
now to actually be able to execute this script from the cmd line
we need to create a batch file in the same folder:
mapit.bat

which contains:
@python E:\AutoEstudio\Python\Automate the boring stuff with Python\MY CODE\web-scraping\mapit.py %*

the program that's executing the script (python) - the address where the script is - %* symbol to pass the cmd line arguments to the script

NOTICE we must add first to the PATH environment variable (or user variable)
and PATH system variable the address where the batch and python files are 
to be able to execute them from the 'Run window' (Win + R )
'''