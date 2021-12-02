import os
import glob as glob
from shutil import copyfile

dates=["04:02:2021", "04:03:2021", "12:03:2021", "17:02:2021"]
folder_path="/Users/juanmanuel/Documents/datasets/Lidar_3D/dataset/*/*/clips/*"
dst="/Users/juanmanuel/Documents/datasets/Lidar_3D/dataset_join/"
for file in glob.glob(folder_path):
    id=file.split("/")[-1].split("_")[0]
    mc=file.split("/")[-1].split("_")[2].split(".ply")[0]
    name= id+"_"+mc+"_mc.ply"
    copyfile(file, os.path.join(dst,name))
    print(os.path.join(dst,name))