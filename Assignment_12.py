# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 12:34:40 2018

@author: Ravikiran Bailkeri
"""
import pandas as pd
import numpy as np
df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm','Budapest_PaRis', 'Brussels_londOn'],'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )','12. Air France', '"Swiss Air"']})


'''#1. Some values in the the FlightNumber column are missing. These numbers are meant
to increase by 10 with each row so 10055 and 10075 need to be put in place. Fill in
these missing numbers and make the column an integer column (instead of a float
column).'''

                                                             
df['FlightNumber'] = df['FlightNumber'].interpolate().astype(int)

print("Interpolated df:: \n",df)

'''
2. The From_To column would be better as two separate columns! Split each string on
the underscore delimiter _ to give a new temporary DataFrame with the correct values.
Assign the correct column names to this temporary DataFrame.

'''

Temp_Newdf= pd.DataFrame(df.From_To)
#  new column added "From"
Temp_Newdf['From'] = Temp_Newdf.From_To.str.split('_').str.get(0)
print ("Show 1st Split::\n",Temp_Newdf)
# New Column Added: "To"
Temp_Newdf['To'] = Temp_Newdf.From_To.str.split('_').str.get(1)
print ("Show 2nd Split:: \n",Temp_Newdf)
# remove or drop old column
Temp_Newdf = Temp_Newdf.drop('From_To', 1)
print ("Show updated df:: \n",Temp_Newdf)

'''
3. Notice how the capitalisation of the city names is all mixed up in this temporary
DataFrame. Standardise the strings so that only the first letter is uppercase (e.g.
"londON" should become "London".)
'''

Temp_Newdf['From'] = Temp_Newdf.From.str.title()
Temp_Newdf['To'] = Temp_Newdf.To.str.title()
print ("londON should become London :: \n",Temp_Newdf)

'''
4. Delete the From_To column from df and attach the temporary DataFrame from the
previous questions.
'''

df = df.drop('From_To', 1)
df = pd.concat([Temp_Newdf,df], axis = 1)
print("New Modified df looks like ::\n ",df)

'''
5. In the RecentDelays column, the values have been entered into the DataFrame as a
list. We would like each first value in its own column, each second value in its own
column, and so on. If there isn't an Nth value, the value should be NaN.
Expand the Series of lists into a DataFrame named delays, rename the columns delay_1,
delay_2, etc. and replace the unwanted RecentDelays column in df with delays.
'''

df3 = pd.DataFrame(df['RecentDelays'].values.tolist(), columns=['delay_1','delay_2','delay_3'])
print ("Updated df \n",df3)

df= df.drop('RecentDelays', 1)

df = pd.concat([df, df3], axis = 1)

print ("Concatinated with delay columns\n",df)





