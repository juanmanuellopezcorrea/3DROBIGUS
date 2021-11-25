import pandas as pd
import funtions
from collections import Counter
ph=3

df_gt=pd.read_csv("/Users/juanmanuel/PycharmProjects/lidar3D-master/result/kmin_2kmax_10.csv")
df_gt.sample(frac=0.5)
df_gt["wheat_type"] = df_gt["wheat_type"].str.replace('DurumWheat', 'durum')
df_gt["wheat_type"] = df_gt["wheat_type"].str.replace('Durum', 'durum')
df_gt["wheat_type"] = df_gt["wheat_type"].str.replace('SoftWheat', 'soft')
df_gt["wheat_type"] = df_gt["wheat_type"].str.replace('Soft', 'soft')

lst=df_gt.id.unique().tolist()

lstk=["kmeans_2","kmeans_3","kmeans_4","kmeans_5","kmeans_6","kmeans_7","kmeans_8","kmeans_9","kmeans_10"]

df=pd.DataFrame()
for pl in lst[:10]:
 print(df_gt.kmeans_2.unique())
 df_1= df_gt.loc[(df_gt["id"].astype(str) == str(pl))]
 print(df_1.kmeans_2.unique())

 columns = []
 values=[]
 for k in lstk:
  nk=k.split("_")[-1]
  dfk = df_1.loc[(df_1[str(k)].astype(str) == str(0))]
  for pt in range(0,int(nk)):
   dfk = df_1.loc[(df_1[str(k)].astype(str) == str(pt))]
   #if  len(dfk) >0:
   b=funtions.height_point(dfk,ph)
   name=str(k) + "_k_cl_" + str(pt)
   columns.append(name)
   values.append(b)
 dic=dict(zip(columns,values))




    lstpl["names"].append(k)
    lstpl["names"].append(k)

    print(b)
    df[str(k)+"_k_cl_"+str(pt)]=b
    print(df.head)

     #print(dfk.head())



  df_1 = df.loc[(df.n_plant == str(np))]

  lstk
  df_k= df_1.loc[(df_1.k.astype(str) == str(nk))]



 print(df_1.head())











d