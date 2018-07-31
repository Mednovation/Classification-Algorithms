import sys
import os
import argparse

def find_images(path):
    for root, dirs, files in os.walk(path):
        for filename in files:
            if ".jpg" in filename:
                print(filename)
            elif ".png" in filename:
                print(filename)

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
        
    parser.add_argument(
        'folder_name',
        type = 'str',
        default = ''
    )

    args = parser.parse_args()
