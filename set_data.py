#! /usr/local/bin python3

import glob
import numpy as np
from random import random

"""
Separate the data between test and train/validation
"""
def separate_data(test_ratio_Segmented = 0.1, ratio_NonSegmented = 0.2):
    
    destination_test = "./Ensimag-SlicesPneumothorax/Test/"
    destination_tv = "./Ensimag-SlicesPneumothorax/Train_Validation/"

    len_tv = len(glob.glob("./Ensimag-SlicesPneumothorax/Segmented/imgs/*.npy")) * (1-test_ratio_Segmented)
    print("len_tv =", len_tv)
    len_ns = len_tv * ratio_NonSegmented
    print("len_ns =", len_ns)
    n_ns = len(glob.glob("./Ensimag-SlicesPneumothorax/NonSegmented/*.npy"))
    print("n_ns =", n_ns)
    ratio = int(n_ns // len_ns)
    print(f"ratio = {ratio}")
    assert n_ns / len_ns > 1, "Il n'y a pas assez d'image non segmentée"

    for rep in ["imgs/", "masks/"]:
        i = 0
        for filename in sorted(glob.glob("./Ensimag-SlicesPneumothorax/Segmented/" + rep + "*.npy")):
            img_array = np.load(filename)
            if (i % (1//test_ratio_Segmented) == 0):
                np.save(filename.replace("./Ensimag-SlicesPneumothorax/Segmented/" + rep, destination_test + rep), img_array)
            else:
                if rep == "imgs/":
                    turn(filename, destination_tv, rep)
                    transpose(filename, destination_tv, rep)
                else:
                    turn_mask(filename, destination_tv, rep)
                    transpose_mask(filename, destination_tv, rep)
            i += 1

    j = 0
    for filename in glob.glob("./Ensimag-SlicesPneumothorax/NonSegmented/*.npy"):
        img_array = np.load(filename)
        mask_non_seg = np.zeros(np.shape(img_array))
        if (j % ratio) == 0:
            np.save(filename.replace("./Ensimag-SlicesPneumothorax/NonSegmented/", destination_tv + "imgs/").replace(".npy", "_ns.npy"), img_array)
            np.save(filename.replace("./Ensimag-SlicesPneumothorax/NonSegmented/", destination_tv + "masks/").replace(".npy", "_ns_mask.npy"), mask_non_seg)
        elif (j % ratio) == 1:
            np.save(filename.replace("./Ensimag-SlicesPneumothorax/NonSegmented/", destination_test + "imgs/").replace(".npy", "_ns.npy"), img_array)
            np.save(filename.replace("./Ensimag-SlicesPneumothorax/NonSegmented/", destination_test + "masks/").replace(".npy", "_ns_mask.npy"), mask_non_seg)
        j += 1

def turn(filename, destination, rep):
    img_array = np.load(filename)
    np.save(filename.replace("./Ensimag-SlicesPneumothorax/Segmented/" + rep, destination + rep), img_array)
    img_array_rot90 = np.rot90(img_array)
    np.save(filename.replace("./Ensimag-SlicesPneumothorax/Segmented/" + rep, destination + rep).replace(".npy", "_rot90.npy"), img_array_rot90)
    img_array_rot180 = np.rot90(img_array_rot90)
    np.save(filename.replace("./Ensimag-SlicesPneumothorax/Segmented/" + rep, destination + rep).replace(".npy", "_rot180.npy"), img_array_rot180)
    img_array_rot270 = np.rot90(img_array_rot180)
    np.save(filename.replace("./Ensimag-SlicesPneumothorax/Segmented/" + rep, destination + rep).replace(".npy", "_rot270.npy"), img_array_rot270)
    return

def turn_mask(filename, destination, rep):
    img_array = np.load(filename)
    np.save(filename.replace("./Ensimag-SlicesPneumothorax/Segmented/" + rep, destination + rep), img_array)
    img_array_rot90 = np.rot90(img_array)
    np.save(filename.replace("./Ensimag-SlicesPneumothorax/Segmented/" + rep, destination + rep).replace("_mask.npy", "_rot90_mask.npy"), img_array_rot90)
    img_array_rot180 = np.rot90(img_array_rot90)
    np.save(filename.replace("./Ensimag-SlicesPneumothorax/Segmented/" + rep, destination + rep).replace("_mask.npy", "_rot180_mask.npy"), img_array_rot180)
    img_array_rot270 = np.rot90(img_array_rot180)
    np.save(filename.replace("./Ensimag-SlicesPneumothorax/Segmented/" + rep, destination + rep).replace("_mask.npy", "_rot270_mask.npy"), img_array_rot270)
    return

def transpose(filename, destination, rep):
    img_array = np.load(filename)
    np.save(filename.replace("./Ensimag-SlicesPneumothorax/Segmented/" + rep, destination + rep).replace(".npy", "_T.npy"), img_array.T)
    return

def transpose_mask(filename, destination, rep):
    img_array = np.load(filename)
    np.save(filename.replace("./Ensimag-SlicesPneumothorax/Segmented/" + rep, destination + rep).replace("_mask.npy", "_T_mask.npy"), img_array.T)
    return

# def turn():
#     for filename in glob.glob("./Ensimag-SlicesPneumothorax/Segmented/*.npy"):
#         img_array = np.load(filename)
#         img_array_rot90 = np.rot90(img_array)
#         np.save(filename.replace(".npy", "_rot90.png"), img_array_rot90)
#         img_array_rot180 = np.rot90(img_array_rot90)
#         np.save(filename.replace(".npy", "_rot180.png"), img_array_rot180)
#         img_array_rot270 = np.rot90(img_array_rot180)
#         np.save(filename.replace(".npy", "_rot270.png"), img_array_rot270)
#     return

if __name__ == '__main__':
    separate_data()

# faire un programme, qui multiplie les données chez la machine de chacun.
# déterminer un bon jeu de test.
