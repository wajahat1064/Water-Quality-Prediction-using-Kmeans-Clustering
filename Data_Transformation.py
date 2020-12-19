#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df = pd.read_excel("WATER_DATA.xlsx", encoding='utf-8')
df = df.drop_duplicates( keep='last')
print(df.count())
df_for_test = df
df_for_test = df_for_test[['pH','DO','% Sat','Temp','Conductivity','Drainage Area','Nitrate + Nitrite']]
#df_for_test = df_for_test[['pH','DO','% Sat','Temp','Conductivity']]
df_for_test.describe()
import numpy as np
from sklearn.preprocessing import minmax_scale
df_for_test = df_for_test.rename(columns = {'Drainage Area':'Drainage_Area', 'Nitrate + Nitrite':'Nitrate_Plus_Nitrite', '% Sat':'Saturation'})
def data_summary(df):
    '''Summary dataframe information'''

    df = pd.DataFrame({'type': df.dtypes,
                       'amount': df.isna().sum(),
                       'null_values (%)': (df.isna().sum() / df.shape[0]) * 100,
                       'unique': df.nunique()})
    return df
def remove_R(x):
    """ If the value is a string, then remove currency symbol and delimiters
    otherwise, the value is numeric and can be converted
    """
    if isinstance(x, str):
        return(x.replace('R', '').replace(',', ''))
    return(x)
def remove_lesssign(x):
    """ If the value is a string, then remove currency symbol and delimiters
    otherwise, the value is numeric and can be converted
    """
    if isinstance(x, str):
        return(x.replace('<', '').replace(',', ''))
    return(x)
df_for_test['Nitrate_Plus_Nitrite'] = df_for_test['Nitrate_Plus_Nitrite'].apply(remove_lesssign).astype('float')
df_for_test['DO'] = df_for_test['DO'].apply(remove_R).astype('float')
df_for_test["Saturation"] = df_for_test.Saturation.astype(float)
df_for_test = df_for_test.fillna(df_for_test.mean())
from sklearn.preprocessing import minmax_scale
df_for_test['pH'] = df_for_test['pH'].transform(lambda x: minmax_scale(x.astype(float)))
df_for_test['pH'] = df_for_test['pH']*100
df_for_test["pH"] = df_for_test.pH.astype(int)

df_for_test['DO'] = df_for_test['DO'].transform(lambda x: minmax_scale(x.astype(float)))
df_for_test['DO'] = df_for_test['DO']*100
df_for_test["DO"] = df_for_test.DO.astype(int)

df_for_test['Temp'] = df_for_test['Temp'].transform(lambda x: minmax_scale(x.astype(float)))
df_for_test['Temp'] = df_for_test['Temp']*100
df_for_test["Temp"] = df_for_test.Temp.astype(int)

df_for_test['Saturation'] = df_for_test['Saturation'].transform(lambda x: minmax_scale(x.astype(float)))
df_for_test['Saturation'] = df_for_test['Saturation']*100
df_for_test["Saturation"] = df_for_test.Saturation.astype(int)

df_for_test['Conductivity'] = df_for_test['Conductivity'].transform(lambda x: minmax_scale(x.astype(float)))
df_for_test['Conductivity'] = df_for_test['Conductivity']*100
df_for_test["Conductivity"] = df_for_test.Conductivity.astype(int)

df_for_test['Drainage_Area'] = df_for_test['Drainage_Area'].transform(lambda x: minmax_scale(x.astype(float)))
df_for_test['Drainage_Area'] = df_for_test['Drainage_Area']*100
df_for_test["Drainage_Area"] = df_for_test.Drainage_Area.astype(int)

df_for_test['Nitrate_Plus_Nitrite'] = df_for_test['Nitrate_Plus_Nitrite'].transform(lambda x: minmax_scale(x.astype(float)))
df_for_test['Nitrate_Plus_Nitrite'] = df_for_test['Nitrate_Plus_Nitrite']*100
df_for_test["Nitrate_Plus_Nitrite"] = df_for_test.Nitrate_Plus_Nitrite.astype(int)

df_for_test.mean()
df_for_test.describe()
data_summary(df_for_test)

df_for_test
#df_for_test.to_csv("TRANSFORED_WATER_DATA_7_NORMALIZED.csv")

