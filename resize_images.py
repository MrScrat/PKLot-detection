import cv2
import os
import xml.etree.ElementTree as ET
import numpy as np
import pdb

ROOT = os.path.dirname(os.path.abspath(__file__))  # root directory of this code

#path = os.path.join(ROOT, 'PKLot/PKLotSegmented/')

path = 'PKLot/PKLotSegmented/'

if __name__ == '__main__':
    files = []
    for folder in os.listdir(path):
        if folder[0] != '.':
            for weather in os.listdir(os.path.join(path, folder)):
                if weather[0] != '.':
                    for date in os.listdir(os.path.join(path, folder, weather)):
                        if date[0] != '.':
                            for occupied in os.listdir(os.path.join(path, folder, weather, date)):
                                if occupied[0] != '.':
                                    for img in os.listdir(os.path.join(path, folder, weather, date, occupied)):
                                        files.append(os.path.join(path, folder, weather, date, occupied, img))
    print('found all files')

dim = (90, 90)
for i in range(len(files)):
    # read and resize image
    img = cv2.imread(files[i])
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

    # define location
    location = files[i].split('/')
    location[1] = 'PKLotSegmented_resized'
    location = os.path.join(*location)

    # create directories
    directory = os.path.dirname(location)
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # write image
    cv2.imwrite(location, resized)

    print(str(i) + ' ' + location)

    # pdb.set_trace()