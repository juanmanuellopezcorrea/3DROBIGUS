
import funtions
import pandas as pd
import glob as glob
import kmeans_train
import os
import datetime

def features(ph,pp,pv,folder,path_save):
    """

    :param ph: proporcion de puntos para calcular la altura
    :param pp:  corte del suelo
    :param pv:
    :param folder:
    :param path_save:
    :return:
    """


    df = funtions.coordenates(folder)  # Data frame con todos los puntos con todas plantas
    lstind = []
    lstmc=[]
    lstheight = []
    lstvolum = []
    lstproy = []
    lstprop_10=[]
    lstprop_20=[]
    lstprop_30=[]
    lstprop_40=[]
    lstprop_50=[]

    lstint_50 = []
    lstint_40 = []
    lstint_30 = []
    lstint_20 = []
    lstint_10 = []


    for file in glob.glob(folder):
        ind = file.split("/")[-1].split("id")[0]
        lstind.append(ind)

        np = file.split("/")[-1].split("_")[-2]
        lstmc.append(np)
        df_1 = df.loc[(df["id"] == str(ind) )]
        df_1=funtions.clipsoil(df_1,pp)
        print(df_1.head())
        height = funtions.height_point(df_1, ph)
        lstheight.append(height)
        volum = funtions.point_cloud_volume(df_1, pv, ph)
        lstvolum.append(volum[3])  #Obtener volumen
        lstproy.append(volum[4])  #Obtener proyección
        # n de puntos
        dp_10 = funtions.density_height_points(df_1, 10)
        dp_20 = funtions.density_height_points(df_1, 20)
        dp_30 = funtions.density_height_points(df_1, 30)
        dp_40 = funtions.density_height_points(df_1, 40)
        dp_50 = funtions.density_height_points(df_1, 50)
        lstprop_10.append(dp_10)
        lstprop_20.append(dp_20)
        lstprop_30.append(dp_30)
        lstprop_40.append(dp_40)
        lstprop_50.append(dp_50)


        # intensity
        dint_50 = funtions.intensity_heigtht_points(df_1,50)
        dint_40 = funtions.intensity_heigtht_points(df_1,40)
        dint_30 = funtions.intensity_heigtht_points(df_1,30)
        dint_20 = funtions.intensity_heigtht_points(df_1,20)
        dint_10 = funtions.intensity_heigtht_points(df_1,10)

        lstint_50.append(dint_50)
        lstint_40.append(dint_40)
        lstint_30.append(dint_30)
        lstint_20.append(dint_20)
        lstint_10.append(dint_10)

    df_features = pd.DataFrame(list(zip(lstind,
                                        lstmc,
                                        lstheight,
                                        lstvolum,
                                        lstproy,
                                        lstprop_10,
                                        lstprop_20,
                                        lstprop_30,
                                        lstprop_40,
                                        lstprop_50,
                                        lstint_50,
                                        lstint_40,
                                        lstint_30,
                                        lstint_20,
                                        lstint_10,)
                                    ),

                                  columns=['index',
                                           'maceta',
                                           'lstheight',
                                           'lstvolum',
                                           'lstproy',
                                           'lstprop_10',
                                           'lstprop_20',
                                           'lstprop_30',
                                           'lstprop_40',
                                           'lstprop_50',
                                           'lstint_50',
                                           'lstint_40',
                                           'lstint_30',
                                           'lstint_20',
                                           'lstint_10',]
                               )

    name= os.path.join(path_save,( str(datetime.datetime.now())+"_features_ph_"+ str(ph)+"pv_"+str(pv)+"_pp_"+str(pp)+".csv"))
    df_features.to_csv(name)
    return df_features









