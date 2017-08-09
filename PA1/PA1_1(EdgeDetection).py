import numpy as np
import cv2
from matplotlib import pyplot as plt
import matplotlib.image as img
from PIL import Image

img1 = cv2.imread('lena_gray.jpg', cv2.IMREAD_GRAYSCALE).astype(float) / 255.0
cv2.imshow('image1',img1);

#sobel_filter_Gx = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
#Gx = cv2.filter2D(src=img1, kernel=sobel_filter_Gx,ddepth=-1)
#cv2.imshow('image2',Gx)
#
#sobel_filter_Gy = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
#Gy = cv2.filter2D(src=img1, kernel=sobel_filter_Gy,ddepth=-1)
#cv2.imshow('image3',Gy)
#
#G = np.sqrt(Gx**2+Gy**2)
#cv2.imshow('image4',G)

kernelX = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
kernelY = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
kernelXv = np.array([[1],[2],[1]])
kernelXh = np.array([[-1,0,1]])
kernelYv = np.array([[-1],[0],[1]])
kernelYh = np.array([[1,2,1]])

def padwithzeroes(image,pad_width,iaxis, kwargs):
    image[:pad_width[0]] = 0
    image[-pad_width[1]:] = 0
    return image

img2 = np.lib.pad(img1,1,padwithzeroes)

def conv2d(image,kernel):
    
    img3 =  np.zeros((image.shape[0]-2, image.shape[1]-2))
    for x in range(1,image.shape[0]-1):
        for y in range(1,image.shape[1]-1):
            img3[x-1,y-1] = (image[x - 1, y - 1] * kernel[0, 0] + 
                              image[x - 1, y] * kernel[0, 1] + 
                              image[x - 1, y + 1] * kernel[0, 2] +
                              image[x, y - 1] * kernel[1, 0] + 
                              image[x, y] * kernel[1, 1] + 
                              image[x, y + 1] * kernel[1, 2] +
                              image[x + 1, y - 1] * kernel[2, 0] + 
                              image[x + 1, y] * kernel[2, 1] + 
                              image[x + 1, y + 1] * kernel[2, 2])
    
    return img3

Gx = conv2d(img2,kernelX)
cv2.imshow('Gx',Gx)

Gy = conv2d(img2,kernelY)
cv2.imshow('Gy',Gy)

G = np.sqrt(Gx**2+Gy**2)
cv2.imshow('G',G)

def conv1d(image,kernelv,kernelh):
    img4 =  np.zeros((image.shape[0], image.shape[1]))
    img5 =  np.zeros((image.shape[0], image.shape[1]))

    for x in range(1,image.shape[0]-1):
     for y in range(1,image.shape[1]-1):
        img4[x,y] = (image[x - 1, y] * kernelv[0, 0] +
                    image[x, y] * kernelv[1,0] + 
                    image[x + 1, y] * kernelv[2, 0])
    for x in range(1,image.shape[0]-1):
     for y in range(1,image.shape[1]-1):    
        img5[x-1, y-1] = (img4[x, y-1] * kernelh[0,0] +
                         img4[x, y] * kernelh[0,1] +
                         img4[x, y+1] * kernelh[0,2])
    return img5

Gx1 = conv1d(img2,kernelXv,kernelXh)
cv2.imshow('Gx1',Gx1)

Gy1 = conv1d(img2,kernelYv,kernelYh)
cv2.imshow('Gy1',Gy1)

G1 = np.sqrt(Gx1**2+Gy1**2)
cv2.imshow('G1',G1)

