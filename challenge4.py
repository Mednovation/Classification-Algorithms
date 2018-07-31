import sys
import os
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS


def main():
    image = Image.open("Samoyed.jpg")
    info = image._getexif()
    #image.size or image.whatever check on the manual
    for tag, value in info.items():
        key = TAGS.get(tag, tag)
        print(key + " " + str(value))
    print(image.size)
    w, h = image.size
    print(image.getcolors(w*h))
    print(datetime.datetime.fromtimestamp(os.stat("Samoyed.jpg").st_ctime))


if __name__ == '__main__':
    main()

