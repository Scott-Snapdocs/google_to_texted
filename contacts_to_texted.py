import pandas as pd

#read in the file
df = pd.read_csv('contacts.csv') #, encoding='iso-8859-1')

#first names are the index, so reset it and pull the right columns
df.reset_index(inplace=True)
df = df[['index', 'Middle Name', 'Home Phone 2']]
df.columns = ['First', 'Last', 'Phone']

#drop any row without a number
df = df[df['Phone'].notnull()]


import re
#number cleaning
def clean_number(p):
    cp = re.sub('[^0-9]', '', p)
    if len(cp) == 11: #includes preceding 1
        return cp[1:]
    if len(cp) > 10: #weird numbers
        return 'weird'
    return cp

#clean up the numbers
df['Phone Number'] = df['Phone'].apply(clean_number)

#remove nonUS, 800 numbers
df = df[df['Phone Number']!='weird'] 

#drop any row without a first or last name
df = df[(df['First'].notnull()) | (df['Last'].notnull())]

import math

limit = 100
nrows = df.shape[0]
iterations = math.ceil(nrows/limit)

for i in range(iterations):
    end = limit * (i+1)
    if nrows < end:
        end = nrows

    my_df = df.iloc[i*limit:end]
    my_df = my_df[['First', 'Last', 'Phone Number']]
    file = 'cleaned contacts - ' + str(i+1) + '.csv'
    my_df.to_csv(file, index=False)
    print('created ', file)