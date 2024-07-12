import cv2
import sys 

class imageOps:
    def self():
        pass
    def getPixelValue(img, x, y):
        print(img[x, y])
        print('[',img.item(x,y,0), img.item(x,y,1), img.item(x,y,2),']')
    
    def getPixelRGBValue(img, x, y):
        print("B: ", img[x, y, 0])
        print("G: ", img[x, y, 1])
        print("R: ", img[x, y, 2])
        print("B: ", img.item(x, y, 0))
        print("G: ", img.item(x, y, 1))
        print("R: ", img.item(x, y, 2))

    def getImageShape(img):
        print(img.shape)  
        
    def getImageDataType(img):
        print(img.dtype)  
    
    def getImageChannels(img):
        print(img.shape[2])
        
    
    def setImagePixelValue(img, x, y, value):
        img[x, y] = value
        return img
    
    def setImagePixelRGBValue(img, x, y, value):
        img[x, y, 0] = value[0]
        img[x, y, 1] = value[1]
        img[x, y, 2] = value[2]
        img.itemset((x, y, 0), value[0])
        img.itemset((x, y, 1), value[1])
        img.itemset((x, y, 2), value[2])
        return img 
    
    def loadImage(path):
        try:
            img = cv2.imread(path)
            return img
        except:
            print("Error loading image")
            sys.exit(1)
            
    def saveImage(img, path):
        cv2.imwrite(path, img)

    def showImage(img):
        cv2.imshow('image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()