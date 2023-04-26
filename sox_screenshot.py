"""
This script will be used to automate the SOX complaince procedure
at The Company.
"""
from PIL import ImageGrab
import win32com.client as win32

image_title = input('Name image: ')
counter = 0

while image_title != '':
    counter += 1
    ss_region = (1207, 515, 1870, 1080)
    ss_img = ImageGrab.grab(ss_region)
    ss_img.save(f'some\path\to\the\{image_title}.jpg', 'JPEG')

    if counter == 1:
        another = input('Do you need another screenshot? ').lower()
        if another == 'y':
            image_title = input('Name image: ')
            ss_region = (1207, 515, 1870, 1080)
            ss_img = ImageGrab.grab(ss_region)
            ss_img.save(image_title + '.jpg')
            break
        elif another == 'n':
            break
print('All screenshots have been taken!')

username = input('Name of account: ')
ticket_number = input('Corresponding ticket: ')
enabled_disabled = input('Is the account getting enabled or disabled? ').lower()

if enabled_disabled == 'e':
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = 'email.address@email.com'
    mail.Subject = f'Account Enabled: {username}'
    mail.Body = f'Account Enabled: {username}\n Ticket number: {ticket_number}'
    
    attachment  = r'some\path\to\the\file'
    attachment1  = r'some\path\to\the\file'
    mail.Attachments.Add(attachment)
    mail.Attachments.Add(attachment1)
    mail.Send()

elif enabled_disabled == 'd':
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = 'email.address@email.com'
    mail.Subject = f'Account Disabled: {username}'
    mail.Body = f'Account Disabled: {username}\n Ticket number: {ticket_number}'
    
    attachment  = r'some\path\to\the\file'
    attachment1  = r'some\path\to\the\file'
    mail.Attachments.Add(attachment)
    mail.Attachments.Add(attachment1)
    mail.Send()

# Documentation:
# https://www.askpython.com/python/examples/capture-screenshots
# https://stackoverflow.com/questions/69759056/getting-coordinate-of-elements-on-my-laptop-screen
# https://stackoverflow.com/questions/56305787/adding-multiple-attachments-to-outlook-email-based-off-elements-in-a-list - used to add multiple attachments to email
