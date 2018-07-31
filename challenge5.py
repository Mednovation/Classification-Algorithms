import sys
import os
from PIL import Image
from PIL.ExifTags import GPSTAGS
import cv2
import numpy as np
from matplotlib import pyplot as plt

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
    return image.size

def get_date(image_name):
    image = Image.open(image_name)
    return datetime.datetime.fromtimestamp(os.stat(image_name).st_ctime)

def get_info(image_name):
    image = Image.open(image_name)
    info = image._getexif()
    for tag, value in info.items():
        key = TAGS.get(tag, tag)
        print(key + " " + str(value))

def main():
    
    f = open("labels.txt","w+")
    
    folder_name = sys.argv[1]
    
    folder_path = os.path.expanduser("~/Desktop/%s") %folder_name
    
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if ".jpg" in filename:
                f.write("image name: " + filename + "\n" + "label: " + os.path.basename(folder_path) + "\n" + "size: " + get_size("/"+os.path.basename(folder_path)+"/"+filename) + "\n" + "date: " + get_date("/"+os.path.basename(folder_path)+"/"+filename) + "\n" + "~~~" + "\n")
            elif ".png" in filename:
                f.write("image name: " + filename + "\n" + "label: " + os.path.basename(folder_path) + "\n" + "size: " + get_size("/"+os.path.basename(folder_path)+"/"+filename) + "\n" + "date: " + get_date("/"+os.path.basename(folder_path)+"/"+filename) + "\n" + "~~~" + "\n")

    f.close()


if __name__ == '__main__':
    main()
