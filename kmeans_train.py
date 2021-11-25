import funtions
import pandas as pd
import glob
from sklearn.cluster import KMeans
import os
import pickle
import numpy as np
import sys

from sklearn.model_selection import train_test_split



def kfeatures(dataset,path_save):
    print("Start the prediction")
    #split dataset
    folder_df=os.path.join(dataset,"dataset/*/*/clips/*.ply")
    df= funtions.coordenates(os.path.join(dataset,"dataset/*/*/clips/*.ply"))
    df_arr=df.to_numpy()
    X_train=df_arr
    #X_train, X_test = train_test_split(df_arr, test_size=0.99, random_state=42)

    #Train k-means models
    lstk =[2,3,4,5,6,7,8,9,10]

    #a=funtions.kmeans_train(X_train[:,3:7],lstk,dataset)

    #kmeans predict

    folder_models= os.path.join(dataset,"models/*")
    print (folder_models)
    df_pred= funtions.kmeans_pred(df_arr[:, 3:7],folder_models)
    df_pred=[df,df_pred]
    df_pred=pd.concat(df_pred, axis=1)

    name= os.path.join(("kmin_"+ str(min(lstk))+"kmax_"+ str(max(lstk))+".csv"))
    df.to_csvpath_save(path_save+name)




