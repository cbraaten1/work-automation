import os
import shutil
import schedule
import time

"""
This script is used for configuring a new laptop for a user that 
is either returning to the company or a new employee. This script will be
run using WinPython through a USB hard drive since Python is not installed
on the users machine.

These programs are necessary for users to complete the
necessary functions in their job role at The Company. Some programs will
include Google Chrome, Google Earth Pro, Microsoft Office, etc.

All programs have been downloaded and packaged into a Microsoft
Software Installer (.msi) file to automate the installation process.
"""
def software1():
    print('Installing software1.')
    os.system('msiexec /i %s /qn' 'C:\a\path\to\some\msi\file')
    print('ConnectWise installed.')
    return schedule.CancelJob

def software2():
    print('Installing software2.')
    os.system('msiexec /i %s /qn' 'C:\a\path\to\some\msi\file')
    return schedule.CancelJob

def software3():
    print('Installing software3.')
    os.system('msiexec /i %s /qn' 'C:\a\path\to\some\msi\file')
    return schedule.CancelJob

def software4():
    print('Installing software4.')
    os.system('msiexec /i %s /qn' 'C:\a\path\to\some\msi\file')
    return schedule.CancelJob

def software5():
    print('Installing software5.')
    os.system('msiexec /i %s /qn' 'C:\a\path\to\some\msi\file')
    return schedule.CancelJob

def software6():
    bb = input('Does software6 need to be installed? Y/N: ')
    if bb == 'Y':
        print('Installing software6.')
        os.system('msiexec /i %s /qn' 'C:\a\path\to\some\msi\file')
        return schedule.CancelJob
    else:
        print('Software is not a requested software to be installed.')

def software7():
    p6= input('Does software7 need to be installed? Y/N: ')
    if p6 == 'Y':
        print('Installing software7.')
        os.system('C:\a\path\to\some\msi\file')
        return schedule.CancelJob
    else:
        print('Software7 is not a requested software to be installed.')

folder_path = 'C:\temp'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

source = 'D:\a\path\to\external\hard\drive'
destination = 'C:\temp'

all_files = os.listdir(source)

for files in all_files:
    src_path = os.path.join(source, files)
    dst_path = os.path.join(destination, files)
    shutil.move(src_path, dst_path)

schedule.every(1).seconds.do(software1)
schedule.every(3).minute.do(software2)
schedule.every(7).minute.do(software3)
schedule.every(13).minute.do(software4)
schedule.every(18).minute.do(software5)
schedule.every(23).minute.do(software6)
schedule.every(30).minute.do(software7)

while 1:
    n = schedule.idel_seconds()

    if n is None:
        print('All requested programs have been installed on the computer.')
        break
    elif n > 0:
        time.sleep(n)
    schedule.run_pending()

# Internet Documentation:
#   https://stackoverflow.com/questions/14519958/how-to-install-a-msi-using-python-script - Structure of the functions comes from this Stack Overflow.
#   https://www.geeksforgeeks.org/python-script-that-is-executed-every-5-minutes/ - Original idea on how to execute code on a timer; see module #2.
#   https://schedule.readthedocs.io/en/stable/examples.html - The while loop is pulling from "Time Until Next Execution".
#   https://stackoverflow.com/questions/70235696/checking-folder-and-if-it-doesnt-exist-create-it - Used to create the temp folder in C:\ if not there.
#   https://www.geeksforgeeks.org/how-to-move-all-files-from-one-directory-to-another-using-python/ - Using shutil.move() to move software programs onto the computer.
