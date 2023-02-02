import pandas as pd
import win32com.client as win32

"""
The purpose of this script is to automate the single task of 
checking for laptops (company assets) that need to be reimaged and 
loaded with basic software until re-deployment to a new user.

The script will convert a Microsfot Excel (xlsx) file to a csv file.

The automation comes in three phases; 1. checking for assets less than zero, 
2. sending the text file via email, 3. task is run through task manager on the computer.
"""

xlsx = r'A\path\to\the\xlsx\file' # Enter file path for the xlsx document.

df = pd.read_excel(xlsx, sheet_name='some sheet name') # Enter the sheet name from the xlsx file.
df = df[df['enter column header'].notna()] # Pulls the value (number) from the column if applicable.
df.to_csv('csv_to.csv', index=False)

read_csv = pd.read_csv('csv_to.csv')
# dtype_before = type(test['enter column header']) # Getting the type.
asset_list = read_csv['enter column header'].tolist()
hold_list = read_csv['enter column header'].tolist()
# dtype_after = type(hold_list) # Getting the type.
# print('Data type before converting = {}\nData type after converting = {}'.format(dtype_before,dtype_after)) # Showing the conversion to a list.
to_dict = dict(zip(asset_list, hold_list))

asset_less_zero = []

for asset, laptop in to_dict.items(): # Looping through the dictionary list checking for any laptops that are less than zero (negative values).
    try:
        value = int(laptop)
    except ValueError:
        continue    
        
    if value < 0:    
        asset_less_zero.append(asset)

email_file = open(r'A\path\to\the\txt\file', 'r+') # Setting up the text file to be written
email_file.truncate(0)
email_file.write(str(asset_less_zero)) # Writing the assets that have past the 30 day holding period and are currently less than zero.
email_file.close()

outlook = win32.Dispatch('outlook.application') # Automating the process of the text file being sent via email.
mail = outlook.CreateItem(0)
mail.To = 'Enter email address here'
mail.Subject = 'Enter subject title here'
mail.Body = 'Enter the body of the email here'

attachment  = r'A\path\to\the\txt\file'
mail.Attachments.Add(attachment)

mail.Send()
