import pandas as pd

xlsx = r'**Please insert file path here.' # File path location is needed here set as a xlsx file.

df = pd.read_excel(xlsx, sheet_name='Asset - Laptop & Other Devices')
df = df[df['IT Asset Hold'].notna()]
df.to_csv('csv_to.csv', index=False)

read_csv = pd.read_csv('csv_to.csv')
# dtype_before = type(test['IT Asset Hold']) # Getting the type
asset_number = read_csv['Asset'].tolist()
hold_list = read_csv['IT Asset Hold'].tolist()
# dtype_after = type(hold_list) # Getting the type
# print('Data type before converting = {}\nData type after converting = {}'.format(dtype_before,dtype_after)) # showing the conversion to a list.
to_dict = dict(zip(asset_number, hold_list))

for laptop in to_dict.values():
    try:
        asset = int(laptop)
        if asset < 0:
            print('hello')
            # email_file = open(r'**Please insert file path here','r+') # File path location is needed here - set as a txt file.
            # email_file.write(str(asset_number)) # Throws a TypeError: write() argument must be str, not Series - str call needed for call to work.
            # email_file.close()
    except ValueError:
        continue
# {8: '2023-01-11 00:00:00', 1121: '-35', 1319: '4', 1408: '-28', 1599: '-52', 1605: '-41', 1625: '-49', 1811: '-13', 1814: '-24', 2014: '-37', 2020: '-31', 2055: '18', 2064: '2022-11-11 00:00:00', 2189: '-7'}
