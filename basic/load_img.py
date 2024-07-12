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
import image_ops 
import os

path = "D:\\intchains\\opencv\\pic\\1.png"
if not os.path.exists(path):
    print(f"File not found: {path}")
    sys.exit(1)

img = image_ops.imageOps.loadImage(path)
image_ops.imageOps.getPixelValue(img, 100, 100)
image_ops.imageOps.getPixelRGBValue(img, 100, 100)
image_ops.imageOps.getImageShape(img)
image_ops.imageOps.getImageDataType(img)
image_ops.imageOps.showImage(img)

