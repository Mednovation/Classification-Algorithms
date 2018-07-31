import sys
import os

def find_images(path):
    for root, dirs, files in os.walk(path):
        for filename in files:
            if ".jpg" in filename:
                print(filename)
            elif ".png" in filename:
                print(filename)

if __name__ == '__main__':
    
    folder_name = sys.argv[1]

    folder_path = os.path.expanduser("~/Desktop/%s") %folder_name

    find_images(folder_path)
