"""
This script will be used to automate the SOX complaince procedure
at The Company.

The process is being reducded to prompts from the script instead
of manually taking screenshots and emailing them to the IT team. This
script also captures a copy of the email and sends it to the SOX compliance
folder on a company server.
"""
from PIL import ImageGrab
import win32com.client as win32
from win32com.client import Dispatch
import os
from os import listdir
import re
import time

image_title = input('Screenshot Name: ')
counter = 0
folder_dir = 'C:\\a\\path\\to\\the\\folder\\dir'
image = []

while image_title != '':
    counter += 1
    ss_region = (1207, 515, 1870, 1080)
    ss_img = ImageGrab.grab(ss_region)
    ss_img.save(f'C:\\a\\path\\to\\the\\folder\\{image_title}.jpg', 'JPEG')
    
    for images in os.listdir(folder_dir):
        if images.endswith('.jpg'):
            image.append(images)
            print(image)

    if counter == 1:
        another = input('Do you need another screenshot? ').lower()
        if another == 'y':
            image_title = input('Name image: ')
            ss_region = (1207, 515, 1870, 1080)
            ss_img = ImageGrab.grab(ss_region)
            ss_img.save(f'C:\\a\\path\\to\\the\\folder\\{image_title}.jpg', 'JPEG')

            for images in os.listdir(folder_dir):
                if images.endswith('.jpg'):
                    image.append(images)
                    print(image)
            break
        elif another == 'n':
            break
print('All screenshots have been taken!')

vpn = input('Are you connected to the VPN or at a office location? ').lower()

if vpn == 'y':
    username = input('Name of account: ')
    ticket_number = input('Corresponding ticket: ')
    enabled_disabled = input('Is the account getting enabled or disabled? ').lower()
    if enabled_disabled == 'e':
        outlook = win32.Dispatch('outlook.application')
        mail = outlook.CreateItem(0)
        mail.To = 'email.address@email.com'
        mail.Subject = f'Account Enabled: {username}'
        mail.Body = f'Account Enabled: {username}\n Ticket number: {ticket_number}'

        file = f'C:\\a\\path\\to\\the\\folder\\{image_title}.jpg'
        for screenshot in image:
            file_path = os.path.join(file, f'{screenshot}.jpg')
            if os.path.exists(file_path):
                mail.Attachments.Add(file_path)
        mail.Send()
        print('Email has been sent.')

        time.sleep(15)

        outlook = Dispatch("Outlook.Application").GetNamespace("MAPI")
        inbox = outlook.GetDefaultFolder(6)
        messages = inbox.items
        message = messages.GetLast()
        name = str(message.subject)
        name = re.sub('[^A-Za-z0-9]+', '', name)+'.msg' # to eliminate any special charecters in the name
        folder_path = ('C:\\a\\path\\to\\the\\folder')
        for folder in os.listdir(folder_path):
            if 'SOX_Screenshots' in folder:
                message.SaveAs(f'C:\\a\\path\\to\\the\\folder\\{name}')

    elif enabled_disabled == 'd':
        outlook = win32.Dispatch('outlook.application')
        mail = outlook.CreateItem(0)
        mail.To = 'email.address@email.com'
        mail.Subject = f'Account Disabled: {username}'
        mail.Body = f'Account Disabled: {username}\n Ticket number: {ticket_number}'
    
        file = f'C:\\a\\path\\to\\the\\folder\\{image_title}.jpg'
        for screenshot in image:
            mail.Attachments.Add(file)
            mail.Send()
        print('Email has been sent.')

        time.sleep(15)

        outlook = Dispatch("Outlook.Application").GetNamespace("MAPI")
        inbox = outlook.GetDefaultFolder(6)
        messages = inbox.items
        message = messages.GetLast()
        name = str(message.subject)
        name = re.sub('[^A-Za-z0-9]+', '', name)+'.msg' # to eliminate any special charecters in the name
        folder_path = ('C:\\a\\path\\to\\the\\folder')
        for folder in os.listdir(folder_path):
            if 'SOX_Screenshots' in folder:
                message.SaveAs(f'C:\\a\\path\\to\\the\\folder\\{name}')

elif vpn == 'n':
    print('Please connect to the VPN before proceeding!')

# Documentation:
# https://www.askpython.com/python/examples/capture-screenshots
# https://stackoverflow.com/questions/69759056/getting-coordinate-of-elements-on-my-laptop-screen
# https://stackoverflow.com/questions/56305787/adding-multiple-attachments-to-outlook-email-based-off-elements-in-a-list - used to add multiple attachments to email.
# https://stackoverflow.com/questions/51621535/saving-email-from-outlook-into-folder-with-python - used to automatically save the email to a folder.
# https://www.geeksforgeeks.org/how-to-iterate-through-images-in-a-folder-python/ - creating a for loop to append images to a list.
