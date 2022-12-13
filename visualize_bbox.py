import cv2
import os
import xml.etree.ElementTree as ET
import numpy as np
import pdb

ROOT = os.path.dirname(os.path.abspath(__file__))  # root directory of this code

path = os.path.join(ROOT, './PKLot/PKLot/PUCPR/Cloudy/2012-09-12/')

def print_bbox(img, anns):
    '''draw bounding boxes on an image
    annotations are in xml format
    anns is path to xml file
    '''
    tree = ET.parse(anns)
    root = tree.getroot()
    bboxes = []
    for space in root:
        try:
            occupied = int(space.attrib['occupied'])
        except:
            occupied = -1
            print('WARNING: Occupied annotation missing!')
        # center coordinates
        for rect in space.findall('rotatedRect/center'):
            x = int(rect.get('x'))
            y = int(rect.get('y'))
        # width, height
        for rect in space.findall('rotatedRect/size'):
            w = int(rect.get('w'))
            h = int(rect.get('h'))
        for rect in space.findall('rotatedRect/angle'):
            d = int(rect.get('d'))
        bboxes.append([occupied, x, y, w, h, d])
    
        # only draw dots for now cause I'm too lazy to rotate rectangles
        cv2.circle(img, (x, y), 5, (0, 255, 0), 5)

if __name__ == '__main__':
    files = os.listdir(path)
    for i in range(len(files)):
        file = os.path.join(path, files[i])
        
        # check if it's jpg
        if file[-4:] == '.jpg':
            img = cv2.imread(file)
            anns = file[:-4] + '.xml'
            print_bbox(img, anns)
            cv2.imshow('image', img)
            if cv2.waitKey() == 27: # close on esc
                break
        else: continue