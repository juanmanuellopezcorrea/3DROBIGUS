import funtions
import glob
import pandas as pd


df_gt=pd.read_csv("/Users/juanmanuel/PycharmProjects/L3/results/GT.csv", header=[0]).sort_values('id')
df=pd.read_csv("/Users/juanmanuel/PycharmProjects/L3/results/2021-12-03 11:59:14.240385_features_ph_10pv_20_pp_30.csv", header=[0]).sort_values('index')

df_join = pd.concat([df_gt, df], axis=1)
df_join=df_gt+df






