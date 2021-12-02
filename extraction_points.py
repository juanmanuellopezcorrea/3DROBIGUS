import funtions
import glob
import pandas as pd

path_dataset= "/Users/juanmanuel/Documents/datasets/Lidar_3D/dataset_join/*"

df=funtions.coordenates(path_dataset)
df_1=df.loc[(df.id == "34")]

pv=20
pp=30

funtions.point_cloud_volume(df_1,pv,pp,)
#funtions.height_point(df_1,10)
#a=funtions.clipsoil(df_1,40)
#funtions.density_height_points(df_1,99)
#funtions.helloply("/Users/juanmanuel/Documents/hello.ply",a.Px,a.Py,a.Pz,a.intensity)
#funtions.helloply("/Users/juanmanuel/Documents/hello34.ply",df_1.Px,df_1.Py,df_1.Pz,df_1.intensity)
