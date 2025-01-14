#! /usr/bin/env python3

from asyncio import subprocess
from curses.ascii import NUL
import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np
import glob
import cv2
from torch import zero_

global is_scrolling
is_scrolling = False

def scrolling(val):
    global is_scrolling
    if not is_scrolling:
        is_scrolling = True
        print(is_scrolling)

def main():    
    global is_scrolling
    # i = 0
    # for filename in glob.glob("Ensimag-SlicesPneumothorax/Test/imgs/*[0-9].npy"):
    #     f=plt.figure()
    #     if (20*int(argv[1])-1 <= i < 20*int(argv[1])):
    #         img_array = np.load(filename)
    #         ground_truth = np.load(filename.replace("imgs", "masks").replace(".npy", "_mask.npy"))
    #         predic = np.load(filename.replace("Test/imgs", "Pred").replace(".npy", "_OUT.npy"))

    #         # plt.rcParams['figure.figsize'] = [200, 200] 
            
    #         # f.text(0.5, 0.2, filename)

    #         ax = f.add_subplot(20,3, (i%20+1, 1))
    #         ax.set_axis_off()
            
    #         plt.imshow(img_array)

    #         ax = f.add_subplot(20,3, (i%20+1, 2))
    #         ax.set_axis_off()
    #         plt.imshow(ground_truth)

    #         ax = f.add_subplot(20,3, (i%20+1, 3))
    #         ax.set_axis_off()
    #         plt.imshow(predic)
    #     i += 1
    # plt.show()
    files = glob.glob("Ensimag-SlicesPneumothorax/Test/imgs/*[0-9].npy")
    lines=[]

    for file in files:
        img_array = np.load(file)
        ground_truth = 255*np.load(file.replace("imgs", "masks").replace(".npy", "_mask.npy"))
        predic = np.load(file.replace("Test/imgs", "Pred").replace(".npy", "_OUT.npy"))

        lines.append(np.concatenate((img_array, ground_truth, predic), axis=1))
        # print(len(lines[0][0]))
        lines.append(np.zeros([100, len(lines[0][0])]))
    img = np.concatenate(lines, axis=0)

    H_max = np.shape(img)[0]
    img = np.array(img, dtype=np.uint8)
    hpos = 0

    # cv2.imshow("titre", img)
      
    cv2.namedWindow("winImage",cv2.WINDOW_NORMAL)

    cv2.createTrackbar("Hscroll", "winImage", 0, H_max-1000, scrolling)
    while 1:
        # if is_scrolling:
        #     hpos = cv2.getTrackbarPos("Hscroll", "winImage")
        #     is_scrolling = False
        hpos = cv2.getTrackbarPos("Hscroll", "winImage")
        cut_img = img[:][hpos:hpos+1000]
        # print(np.shape(cut_img))
        cv2.imshow("winImage", cut_img)

        k = cv2.waitKey(1) & 0xFF 
        if k == ord('q'):
            break
        elif k == 84:
            if (hpos < H_max-1000):
                cv2.setTrackbarPos("Hscroll", "winImage", hpos+50)
        elif k == 82:
            if (hpos > 0):
                cv2.setTrackbarPos("Hscroll", "winImage", hpos-50)
        print(hpos)            

    cv2.waitKey(0) 
    cv2.destroyAllWindows() 


    
if __name__ == "__main__":
    main()
