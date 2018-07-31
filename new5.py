import sys
import os
from PIL import Image
from PIL.ExifTags import GPSTAGS
import cv2
import numpy as np
from matplotlib import pyplot as plt
import datetime

def get_histogram(image_name):
    img = cv2.imread(image_name)
    color = ('b','g','r')
    plt.figure()
    for i,col in enumerate(color):
        histr = cv2.calcHist([img],[i],None,[256],[0,256])
        plt.plot(histr,color = col)
        plt.xlim([0,256])
    plt.show()

def get_size(image_name):
    image = Image.open(image_name)
    return str(image.size)

def get_date(image_name):
    image = Image.open(image_name)
    return str(datetime.datetime.fromtimestamp(os.stat(image_name).st_ctime))

def get_info(image_name):
    image = Image.open(image_name)
    info = image._getexif()
    for tag, value in info.items():
        key = TAGS.get(tag, tag)
        print(key + " " + str(value))

def main():
    f = open("labels.txt", "w+")
    folder_name = sys.argv[1]
    folder_path = folder_path = os.path.expanduser("~/Desktop/%s") %folder_name

    for root, dirs, files in os.walk(folder_path):
        for dirname in dirs:
            new_path = folder_path + "/" + dirname
            for roo, dir, fil in os.walk(new_path):
                for filename in fil:
                    if ".jpg" or "JPG" in filename:
                        f.write("image name: " + filename + "\n" + "label: " + dirname + "\n" + "size: " + get_size(folder_path+"/"+dirname+"/"+filename) + "\n" + "date: " + get_date(folder_path+"/"+dirname+"/"+filename) + "\n" + "~~~" + "\n")
                    elif ".png" or "PNG" in filename:
                        f.write("image name: " + filename + "\n" + "label: " + dirname + "\n" + "size: " + get_size(folder_path+"/"+dirname+"/"+filename) + "\n" + "date: " + get_date(folder_path+"/"+dirname+"/"+filename) + "\n" + "~~~" + "\n")
    f.close()

if __name__ == '__main__':
    main()
