!pip install openCV 2

import cv2
import os
import re

def tryint(s):
    try:
        return int(s)
    except:
        return s

def alphanum_key(s):
    return [tryint(c) for c in re.split('([0-9]+)', s)]

def sort_nicely(l):
    l.sort(key=alphanum_key)
    return l


directory = "C:\\Users\\hilel\\Downloads\\Images\\Images\\38.27" #"Image/Directory"
fileNameKeys = ['2021-11-02-172459','.jpg']


dirList = sort_nicely([file for file in os.listdir(directory) if all(substring in file for substring in fileNameKeys)])
images = [cv2.imread(directory + '/' + imageFile) for imageFile in dirList if True]
print(dirList)


#################################
stitcher = cv2.Stitcher.create(cv2.STITCHER_PANORAMA) #(cv2.STITCHER_SCANS)
#################################


stitchOut = stitcher.stitch(images)
print("Stitcher exit status = " + str(stitchOut[0]))
print("Hit any Key to continue and save image")
#cv2.imshow('Stitched Image', stitchOut[1])
#cv2.waitKey(0)
cv2.imwrite(directory + "/" + "STITCH.png", stitchOut[1]) 