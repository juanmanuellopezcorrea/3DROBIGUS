import funtions
import pandas as pd
import glob as glob
import kmeans_train
import os
import glob as glob

#split dataset
dataset= "/Users/juanmanuel/Documents/Projects/3Dphenotiping" # path donde esta la carpeta dataset/clips
ph = 3
pp = 20
pv = 2


df= funtions.coordenates(os.path.join(dataset,"dataset/*/*/clips/*.ply"))




df.to_csv("./result/datapoints.csv")






    n = file.split("_")[-3].split("_")[0]
    print(n)


nplant = []
fechal = []
wheat_typelst = []
lstheight = []
lstvolum = []
lstproy = []
lstprop_10 = []
lstprop_20 = []
lstprop_30 = []
lstprop_40 = []
lstprop_50 = []
lstprop_60 = []

lstint_60 = []
lstint_50 = []
lstint_40 = []
lstint_30 = []
lstint_20 = []
lstint_10 = []

for file in glob.glob(dataset+"/dataset/*/*/clips/*.ply")[1]:
    np = file.split("/")[-1].split("_")[1].split(".")[0]
    nplant.append(np)
    f = file.split("/")[-4].split("_rob")[0]
    fechal.append(f)
    twl = file.split("/")[-3]
    wheat_typelst.append(twl)
    df_1 = df.loc[(df.n_plant == str(np))]
    print(df_1.head())




    height = funtions.height_point(df_1, ph)
    lstheight.append(height)
    volum = funtions.point_cloud_volume(df_1, pp, pv)
    lstvolum.append(volum[3])  # Obtener volumen
    lstproy.append(volum[4])  # Obtener proyección
    # n de puntos
    dp_10 = funtions.density_height_points(df_1, 10)
    dp_20 = funtions.density_height_points(df_1, 20)
    dp_30 = funtions.density_height_points(df_1, 30)
    dp_40 = funtions.density_height_points(df_1, 40)
    dp_50 = funtions.density_height_points(df_1, 50)
    dp_60 = funtions.density_height_points(df_1, 60)
    lstprop_10.append(dp_10)
    lstprop_20.append(dp_20)
    lstprop_30.append(dp_30)
    lstprop_40.append(dp_40)
    lstprop_50.append(dp_50)
    lstprop_60.append(dp_60)

    # intensity
    dint_50 = funtions.density_height_points(df_1, 50)
    dint_40 = funtions.density_height_points(df_1, 40)
    dint_30 = funtions.density_height_points(df_1, 30)
    dint_20 = funtions.density_height_points(df_1, 20)
    dint_10 = funtions.density_height_points(df_1, 10)

    lstint_50.append(dint_50)
    lstint_40.append(dint_40)
    lstint_30.append(dint_30)
    lstint_20.append(dint_20)
    lstint_10.append(dint_10)


df_features = pd.DataFrame(list(zip(nplant,
                                    fechal,
                                    lstheight,
                                    wheat_typelst,
                                    lstvolum,
                                    lstproy,
                                    lstint_50,
                                    lstprop_10,
                                    lstprop_20,
                                    lstprop_30,
                                    lstprop_40,
                                    lstprop_50,
                                    lstprop_60)
                                ),

                           columns=['nplant',
                                    'fechal',
                                    'lstheight',
                                    'wheat_typelst',
                                    'lstvolum',
                                    'lstproy',
                                    'lstint_50',
                                    'lstprop_10',
                                    'lstprop_20',
                                    'lstprop_30',
                                    'lstprop_40',
                                    'lstprop_50',
                                    'lstprop_60']
                           )

name = os.path.join(path_save, ("features_ph_" + str(ph) + "pv_" + str(pv) + "_pp_" + str(pp) + ".csv"))
df_features.to_csv(name)


