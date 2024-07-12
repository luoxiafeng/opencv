'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2024-07-11 16:35:50
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2024-07-12 08:39:03
FilePath: \opencv\basic\load_img.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import cv2
import sys
import numpy as np

#print current pwd
path = "D:\\opencv\\pic\\1.png"


def getPixelValue(img, x, y):
    print(img[x, y])
    
def getPixelRGBValue(img, x, y):
    print("B: ", img[x, y, 0])
    print("G: ", img[x, y, 1])
    print("R: ", img[x, y, 2])

def getImageShape(img):
    print(img.shape)  
    
def getImageDataType(img):
    print(img.dtype)  
    
def loadImage(path):
    try:
        img = cv2.imread(path)
        return img
    except:
        print("Error loading image")
        sys.exit(1)

def showImage(img):
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img = loadImage(path)
getPixelValue(img, 100, 100)
getPixelRGBValue(img, 100, 100)
getImageShape(img)
getImageDataType(img)
showImage(img)