'''
lets say we have a list
of folder and file names that 
we want to join to represent a path
'''
print('\\'.join(['folder1', 'folder2', 'file.jpg']))
'''
that would print out:
folder1\folder2\file.jpg

NOTICE that Windows uses backslashes and
that the backslashes are doubled because 
each backslash needs to be escaped by another
backslash character. 
If you want your programs to work on all operating
systems, you will have to write your Python scripts
to handle both cases.

that's where the 'os' module comes in

'''

import os
print( os.path.join('folder1', 'folder2', 'file.jpg')) # folder1\folder2\file.jpg

'''
If I had called this function on OS X or Linux, 
the string would have been
folder1/folder2/file.jpg
notice the forward slashes
'''

####### os module examples

# creating strings for file names 
myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(os.path.join('D:\\new\\', filename))
'''
D:\new\accounts.txt
D:\new\details.csv
D:\new\invite.docx
'''

####### current working directory(cwd) or '.'
print( os.getcwd() ) # e:\AutoEstudio\Python\Automate the boring stuff with Python\MY CODE

'''
os.chdir('C:\\Windows\\System32') # also -> os.chdir(r'C:\Windows\System32')
print( os.getcwd() ) # 'C:\Windows\System32'

'''

###### absolute and relative paths
'''
There are two ways to specify a file path.
•	 An absolute path, which always begins with the root folder
•	 A relative path, which is relative to the program’s current working
directory

There are also the dot (.) and dot-dot (..) folders. These are not real
folders but special names that can be used in a path. A single period (“dot”)
for a folder name is shorthand for “this directory.” Two periods (“dot-dot”)
means “the parent folder.”

'''
####### get the absolute path of a file or folder in the current directory.     os.path.abspath()

print( os.path.abspath('00-filenames-and-paths.py') )
# E:\AutoEstudio\Python\Automate the boring stuff with Python\MY CODE\reading-and-writing-files\00-filenames-and-paths.py

print( os.path.abspath('new') )
# E:\AutoEstudio\Python\Automate the boring stuff with Python\MY CODE\reading-and-writing-files\new

###### is the string an absolute path.  os.path.isabs()

# here i pass a raw string (r'') not to use double \\. We could've passed a string and use \\ instead
print( os.path.isabs(r'E:\AutoEstudio\Python\Automate the boring stuff with Python\MY CODE\reading-and-writing-files\new') )
# True


####### getting a relative path given the current directory as starting point
cwd = r'E:\AutoEstudio\Python\Automate the boring stuff with Python\MY CODE\reading-and-writing-files'
f = r'E:\AutoEstudio\Python\Automate the boring stuff with Python\MY CODE\reading-and-writing-files\new\test.txt' # the file we want the relpath for
print ( os.path.relpath(f, cwd) ) # new\test.txt

# getting the directory part of the path
print( os.path.dirname( f ) ) #excludes the file: test.txt
# E:\AutoEstudio\Python\Automate the boring stuff with Python\MY CODE\reading-and-writing-files\new

# getting the basename, for a file
print( os.path.basename( f ) ) # test.txt
# or folder
print( os.path.basename( cwd ) ) # reading-and-writing-files

######### does the path exist? 

print( os.path.exists( f ) ) # True

print( os.path.exists( r'Z:\folderThatDoesntExist\file.txt' ) ) # false

print( os.path.isfile( f ) ) # True

print( os.path.isdir( cwd ) ) # True

print( os.path.getsize( f ) ) # 0  size in bytes as an integer

print( os.path.getsize( r'E:\AutoEstudio\Python\Automate the boring stuff with Python' ) ) # 4096


####### return a list of all files and folders within a folder, notice is os.listdir() not os.path.listdir()
print( os.listdir(r'E:\AutoEstudio\Python\Automate the boring stuff with Python')) 
'''
['01 Python Basics', '02 Flow Control', '03 Functions', '04 Handling Errors with tryexcept',
 '05 Writing a Complete Program Guess the Number', '06 Lists', '07 Dictionaries', '08 More About Strings', 
 '09 Running Programs from the Command Line', '10 Regular Expressions', '11 Files', '12 Debugging',
 '13 Web Scraping', '14 Excel Word and PDF Documents', '15 Email', '16 GUI Automation', 
 'automate-the-boring-stuff-with-python-2015-.pdf', 'MY CODE']
'''

totalSize = 0
for filename in os.listdir(r'E:\AutoEstudio\Python\Automate the boring stuff with Python'):
    file = os.path.join('E:\\AutoEstudio\\Python\\Automate the boring stuff with Python', filename)
    if os.path.isfile(file):
        totalSize += os.path.getsize(file)

print( totalSize) 

###### creating new folders
'''
cwd = os.getcwd()
newfolders = cwd + '\\new\\new2'
os.makedirs(newfolders) # creates new and new2 under the cwd

'''
os.makedirs(os.getcwd() + '\\new3\\new4') # this will create both new3 and new4

'''
or
os.makedirs('D:\\new3\\new4')
or
os.makedirs(r'D:\new3\new4')
'''

