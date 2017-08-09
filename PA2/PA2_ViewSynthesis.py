import cv2
import numpy as np

left_img = cv2.imread('view1.png')#read it as a grayscale image
right_img = cv2.imread('view5.png')

groundTruth1 = cv2.imread('disp1.png',0)
groundTruth2 = cv2.imread('disp5.png',0)
groundTruth3 = cv2.imread('view3.png',0)

view3 = np.zeros((left_img.shape))
for i in range(0,left_img.shape[0]):
    for j in range(0,left_img.shape[1]):
        val = groundTruth1[i][j]
        finval = val/2
        minj = j-finval;
        if(minj<0):
            continue;
        view3[i][minj] = left_img[i][j]
        
cv2.imshow("Left Synthesis",view3 / view3.max())

rtview = np.zeros((right_img.shape))

for i in range(0,right_img.shape[0]):
    for j in range(0,right_img.shape[1]):
        val = groundTruth2[i][j]
        finval = val/2
        minj = j+finval;
        if(minj>right_img.shape[1]-1):
            continue;
       
        if(view3[i][minj].all() == 0):
            rtview[i][minj] = right_img[i][j]
            view3[i][minj] = right_img[i][j]

cv2.imshow("Right Synthesis",rtview / rtview.max())

cv2.imshow("VS1",view3 / view3.max())