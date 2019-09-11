import shutil # utility functions for copying archiving files and directory trees

##### copying a file
shutil.copy(
    'E:\\AutoEstudio\\Python\\Automate the boring stuff with Python\\MY CODE\\reading-and-writing-files\\new\\test.txt', # what we want to copy 
    'E:\\AutoEstudio\\Python\\Automate the boring stuff with Python\\MY CODE\\reading-and-writing-files\\new3' # and where we want to paste it
    ) # after copying the file, copy returns a string with the path of the copied file

shutil.copy(
    'E:\\AutoEstudio\\Python\\Automate the boring stuff with Python\\MY CODE\\reading-and-writing-files\\new\\test.txt', 
    'E:\\AutoEstudio\\Python\\Automate the boring stuff with Python\\MY CODE\\reading-and-writing-files\\new3\\test_renamed.txt' # we can rename the copy of the file like this
    )

##### if we want to copy a folder and all it contains
shutil.copytree(
    'E:\\AutoEstudio\\Python\\Automate the boring stuff with Python\\MY CODE\\reading-and-writing-files\\new',
    'E:\\AutoEstudio\\Python\\Automate the boring stuff with Python\\MY CODE\\reading-and-writing-files\\new_backup' # copy 'new' and rename it as 'new_backup'
)

#### move
shutil.move(
    'E:\\AutoEstudio\\Python\\Automate the boring stuff with Python\\MY CODE\\reading-and-writing-files\\new_backup',
    'E:\\AutoEstudio\\Python\\Automate the boring stuff with Python\\MY CODE\\reading-and-writing-files\\new\\new_backup' 
)

#### rename a folder using move()
shutil.move(
    'E:\\AutoEstudio\\Python\\Automate the boring stuff with Python\\MY CODE\\reading-and-writing-files\\new\\new_backup',
    'E:\\AutoEstudio\\Python\\Automate the boring stuff with Python\\MY CODE\\reading-and-writing-files\\new\\renamed_new_backup' # move to the same folder and specify the new name
)

