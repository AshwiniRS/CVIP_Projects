import numpy as np
import cv2
from matplotlib import pyplot as plt
import matplotlib.image as img
from PIL import Image

#reading image using opencv
img = cv2.imread('lena_gray.jpg',0)
img1=np.copy(img)
cv2.imshow('original',img)
grey_scale_int=np.arange(256)
#cumulatives = histogram.cumsum()

#Step1 storing frequencies of intensities inH
H = np.zeros((256),dtype=int)
cumsum = np.zeros((256),dtype=int)
Tp = np.zeros((256),dtype=int)
H1 = np.zeros((256),dtype=int)

#Step2
for i in range(0,img.shape[0]):
    for j in range(0,img.shape[1]):
        H[img[i,j]]+=1

#Histogram 1 = Image histogram
plt.figure('Image Histogram')  
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency of intensity level')
plt.title('Image Histogram')
plt.plot(H)
plt.show()
    
#Step3 calculating cumulatives in H
cumsum = np.cumsum(H)
plt.figure('Cumulative Image Histogram')  
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency of intensity level')
plt.title('Cumulative Image Histogram')
plt.plot(cumsum)
plt.show()

#Step4  
multiplication_factor = (256.0 - 1.0)/(img.shape[0]*img.shape[1])
Tp =multiplication_factor * (cumsum)
#Histogram 3 = Transformed matrix histogram
plt.figure('Tranformed Image Histogram')  
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency of intensity level')
plt.title('Tranformed Image Histogram')
plt.plot(Tp)
plt.show()
#Step5
#img1 = np.zeros((img.shape[0],img.shape[1]))
for i in range(0,img.shape[0]):
    for j in range(0,img.shape[1]):
        img1[i][j] = Tp[img[i][j]]

#Histogram 4 = Final image 
H1 = np.zeros((256))
for i in range(img1.shape[0]):
    for j in range(img1.shape[1]):
        H1[img1[i,j]]+=1    
plt.figure('Final Image Histogram')  
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency of intensity level')
plt.title('Final Image Histogram')
plt.plot(grey_scale_int,H1)
plt.show()

cv2.imshow('result',img1)