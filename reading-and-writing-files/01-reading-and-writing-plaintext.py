'''
You can save variables in your Python programs to binary shelf files using
the shelve module. This way, your program can restore data to variables
from the hard drive. The shelve module will let you add Save and Open
features to your program. For example, if you ran a program and entered
some configuration settings, you could save those settings to a shelf file and
then have the program load them the next time it is run
'''

import shelve 
# save the data
shelfFile = shelve.open('mydata') # create a handler and create or open a file called mydata, 
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats # use the handler to stoore the data in the mydata file, much like in a dictionary using a key
shelfFile.close()

# get the data
shelfFile = shelve.open('mydata')
print(type(shelfFile)) # <class 'shelve.DbfilenameShelf'>
print( shelfFile['cats'] ) #use the key to get the data from the file  ['Zophie', 'Pooka', 'Simon']
shelfFile.close()

'''
 on Windows, you will see three new files
in the current working directory: mydata.bak, mydata.dat, and mydata.dir. On
OS X, only a single mydata.db file will be created.
'''

'''
Just like dictionaries, shelf values have keys() and values() methods that
will return list-like values of the keys and values in the shelf. Since these
methods return list-like values instead of true lists, you should pass them
to the list() function to get them in list form.
'''
shelfFile = shelve.open('mydata')
print( list(shelfFile.keys()) ) # ['cats']
print( list(shelfFile.values()) ) #  [['Zophie', 'Pooka', 'Simon']]
shelfFile.close()