import os
#### deleting a single file
os.unlink('E:\\AutoEstudio\\Python\\Automate the boring stuff with Python\\MY CODE\\reading-and-writing-files\\new5\\test.txt')

#### delete an empty folder
os.rmdir('E:\\AutoEstudio\\Python\\Automate the boring stuff with Python\\MY CODE\\reading-and-writing-files\\new5\\new2')

#### delete a folder and all it contains
import shutil
shutil.rmtree('E:\\AutoEstudio\\Python\\Automate the boring stuff with Python\\MY CODE\\reading-and-writing-files\\new5\\renamed_new_backup')

'''
all the previous functions delete permanently the
files/folders so we need to be extra careful

there's a module that allows to send the files to the 
OS 'recycle bin' instead:
send2trash

pip install send2trash
'''

from send2trash import send2trash
send2trash('E:\\AutoEstudio\\Python\\Automate the boring stuff with Python\\MY CODE\\reading-and-writing-files\\new5\\test.txt')
