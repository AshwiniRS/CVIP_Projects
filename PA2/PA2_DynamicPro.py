import cv2
import numpy as np

left_img = cv2.imread('view1.png', 0)  #read it as a grayscale image
right_img = cv2.imread('view5.png', 0)

#Disparity Computation for Left Image

OcclusionCost = 20 #(You can adjust this, depending on how much threshold you want to give for noise)

#For Dynamic Programming you have build a cost matrix. Its dimension will be numcols x numcols
numcols = left_img.shape[1]
CostMatrix = np.zeros((left_img.shape[1],left_img.shape[1]))
DirectionMatrix = np.zeros((numcols,numcols))  #(This is important in Dynamic Programming. You need to know which direction you need traverse)
DisparityMatrixLeft = np.zeros(left_img.shape)
DisparityMatrixRight = np.zeros(left_img.shape)

#We first populate the first row and column values of Cost Matrix

for i in range(numcols):
      CostMatrix[i,0] = i*OcclusionCost
      CostMatrix[0,i] = i*OcclusionCost

for row in range(left_img.shape[0]):
    print row
    for i in range(numcols):
        for j in range(numcols):
            min1 = CostMatrix[i-1,j-1] + np.abs((left_img[row,i]-right_img[row,j]))
            min2 = CostMatrix[i-1,j] + OcclusionCost
            min3 = CostMatrix[i,j-1] + OcclusionCost
            CostMatrix[i,j] = cmin = np.min((min1,min2,min3))
            if(min1==cmin):
                DirectionMatrix[i,j] = 1
            if(min2==cmin):
                DirectionMatrix[i,j] = 2
            if(min3==cmin):
                DirectionMatrix[i,j] = 3
    # Now, its time to populate the whole Cost Matrix and DirectionMatrix
    
    # Use the pseudocode from "A Maximum likelihood Stereo Algorithm" paper given as reference
#for row in range(left_img.shape[0]):    
    p=numcols-1
    q=numcols-1
    i=0;j=0;
    while(p!=0 and q!=0):
        if (DirectionMatrix[p,q]==1):
            DisparityMatrixLeft[row,p]=p-q
            DisparityMatrixRight[row,q]=p-q
            p=p-1
            q=q-1
            #break
        elif (DirectionMatrix[p,q]==2):
            p=p-1
           # break
        elif (DirectionMatrix[p,q]==3):
            q=q-1
            #break

cv2.imshow("DisparityImgLeft",DisparityMatrixLeft / DisparityMatrixLeft.max())
cv2.imshow("DisparityImgRight",DisparityMatrixRight / DisparityMatrixRight.max())