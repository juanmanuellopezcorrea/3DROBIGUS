# This is a sample Python script.

import sys
import  features
import kmeans_train
import os
# Press ⌥⇧R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌃' to toggle the breakpoint.



# features
path_save="/Users/juanmanuel/PycharmProjects/lidar3D-master/result/"
dataset="/Users/juanmanuel/Documents/Projects/3Dphenotiping"
#dataset= "/Users/juanmanuel/Desktop" # path donde esta la carpeta dataset/clips
ph = 3
pp = 20
pv = 2

folder=os.path.join(dataset,"dataset/*/*/clips/*.ply")

features.features(ph,pp,pv,folder,path_save)


#kmeans_train.kfeatures(dataset,path_save)








# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')





"""
poner si lo queremos correr desde el terminal


if __name__ == "__main__":
    path_to_originals = sys.argv[1]
    path_to_masks = sys.argv[2]
    main_function(path_to_originals, path_to_masks)
"""



# See PyCharm help at https://www.jetbrains.com/help/pycharm/



import kmeans_train # entrena a kmeans



