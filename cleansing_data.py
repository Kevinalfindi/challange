import pandas as pd
import re

data = "archive/data.csv"
data_abusive = "archive/abusive.csv"
data_alay = "archive/new_kamusalay.csv"

df = pd.read_csv(data, encoding='latin-1')
print("info df", df.info())

df_abusive= pd.read_csv(data_abusive, encoding ='latin-1')
print("info df_abusive", df_abusive.info())

df_alay= pd.read_csv(data_alay, encoding='latin-1')
print("info df_alay", df_alay.info())

df.HS.value_counts()
df.Abusive.value_counts()
print("Toxic shape: ", df[(df['HS'] == 1) | (df['Abusive'] == 1)].shape)
print("Non-toxic shape: ", df[(df['HS'] == 0) & (df['Abusive'] == 0)].shape)