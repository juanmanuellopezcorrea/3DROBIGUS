import os
import pandas as pd
import matplotlib.pyplot as plt

path_save= "/result"

dataset= "/Users/juanmanuel/Documents/Projects/3Dphenotiping" # path donde esta la carpeta dataset/clips

ph = 3
pp = 20
pv = 2


df_result= pd.read_csv("result/features_ph_3pv_2_pp_20.csv")

df_result=df_result.astype('str')

df_result["wheat_typelst"] = df_result["wheat_typelst"].str.replace('DurumWheat', 'durum')
df_result["wheat_typelst"] = df_result["wheat_typelst"].str.replace('SoftWheat', 'soft')
df_result["wheat_typelst"] = df_result["wheat_typelst"].str.replace('Durum', 'durum')
df_result["wheat_typelst"] = df_result["wheat_typelst"].str.replace('Soft', 'soft')


df_result["fechal"] = df_result["fechal"].str.replace(':', '_')

lstdate=["04_02_2021" ,"17_02_2021", "04_03_2021", "12_03_2021"]

for i in lstdate:
    df_result.loc[df_result["fechal"] == str(i)].to_csv("/Users/juanmanuel/Desktop/"+str(i)+".csv")

df_result.loc[(df_result["wheat_typelst"] == 'soft') & (df_result["fechal"] == '17_02_2021')].to_csv("/Users/juanmanuel/Desktop/17_02_2021.csv")

df_result.loc[(df_result["wheat_typelst"] == 'soft') & (df_result["fechal"] == '17_02_2021')].to_csv("/Users/juanmanuel/Desktop/17_02_2021.csv")

df_result.loc[(df_result["wheat_typelst"] == 'soft') & (df_result["fechal"] == '12_03_2021')].to_csv("/Users/juanmanuel/Desktop/12_03_2021.csv")


# Join de Soft
#12 march
df_12Mar_soft= df_result.loc[(df_result["wheat_typelst"] == 'soft') & (df_result["fechal"] == '12:03:2021')]

df_12Mar_soft= df_result.loc[(df_result["wheat_typelst"] == 'soft') & (df_result["fechal"] == '12:03:2021')]
