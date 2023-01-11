import pandas as pd

xlsx = r'**File path removed, please insert file path**' # File path location is needed here set as a xlsx file.

df = pd.read_excel(xlsx, sheet_name='Asset - Laptop & Other Devices')
df = df[df['IT Asset Hold'].notna()]
df.to_csv('csv_to.csv', index=False)

read_csv = pd.read_csv('csv_to.csv')
# dtype_before = type(test['IT Asset Hold']) # Getting the type
hold_list = read_csv['IT Asset Hold'].tolist()
# dtype_after = type(hold_list) # Getting the type
# print('Data type before converting = {}\nData type after converting = {}'.format(dtype_before,dtype_after)) # showing the conversion to a list.

for day in hold_list:
    try:
        asset = int(day)
        if asset < 0:
            # print(test['Asset'])
            email_file = open(r'**File path removed, please insert file path**','r+') # File path location is needed here - set as a txt file.
            email_file.write(str(read_csv['Asset'])) # Throws a TypeError: write() argument must be str, not Series - str call needed for call to work.
            email_file.close()
    
    except ValueError:
        continue
