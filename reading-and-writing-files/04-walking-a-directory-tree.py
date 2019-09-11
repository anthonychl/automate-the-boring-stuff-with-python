'''
os.walk()
allows walk a provided directory tree by returning 3 variables
a string with the current folder name, 
a list of strings with the names of the subfolders to the current folder
and a list of strings with names of the files in the current folder

os.walk() is usually used in a loop to walk the entire tree
'''

import os
for fileName, subfolders, files in os.walk('E:\\AutoEstudio\\Python\\Automate the boring stuff with Python\\MY CODE\\reading-and-writing-files'):
    print('the folder is '+fileName)
    print('the subfolders in '+fileName+' are '+ str(subfolders))
    print('the files in '+fileName+' are '+ str(files))
    print()

    for file in files:  # this is an example of what we could do by walking a dir tree
        if file.endswith('.txt'):
            print(' a .txt file named '+ file) # here we could be deleting files, renaming them, etc
            print()