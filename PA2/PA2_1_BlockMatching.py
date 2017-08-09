import cv2
import numpy as np

left_img = cv2.imread('view1.png', 0)#read it as a grayscale image
right_img = cv2.imread('view5.png', 0)
def padwithzeroes(image,pad_width,iaxis, kwargs):
    image[:pad_width[0]] = 0
    image[-pad_width[1]:] = 0
    return image

leftimg_pad = np.lib.pad(left_img,1,padwithzeroes)
rightimg_pad = np.lib.pad(right_img,1,padwithzeroes)

displeft = np.zeros((leftimg_pad.shape))
dispright = np.zeros((rightimg_pad.shape))

groundTruth1 = cv2.imread('disp1.png',0)
groundTruth2 = cv2.imread('disp5.png',0)


#left_img loop
for i in range(1,leftimg_pad.shape[0]-1):
    for j in range(1,leftimg_pad.shape[1]-1):
        min1 = 9999999
        finalDiff = 0;
        left_mat = np.zeros((3,3))
        left_mat = leftimg_pad[i-1:i+2,j-1:j+2]
        mink=0
        minj=j-78 
        if(minj<=0):
            minj=1
        
            
#column loop on right_image
        for col in range(minj,j+1):
            right_mat = np.zeros((3,3))
            right_mat = rightimg_pad[i-1:i+2,col-1:col+2]
            diff = np.subtract(left_mat,right_mat)
            diff = np.square(diff)
            sumMat = np.sum(diff)
            
            if min1 > sumMat:
                min1=sumMat
                mink=col
        
        displeft[i][j] = np.abs(j-mink)

cv2.imshow("Left Disparity Matrix",displeft / displeft.max())
mse=np.sum(np.square(displeft[1:displeft.shape[0]-1,1:displeft.shape[1]-1]-groundTruth1))/groundTruth1.size
print mse

#right_img loop
for i in range(1,rightimg_pad.shape[0]-1):
    for j in range(1,rightimg_pad.shape[1]-1):
        min1 = 9999999
        finalDiff = 0;
        right_mat = np.zeros((3,3))
        right_mat = rightimg_pad[i-1:i+2,j-1:j+2]
        mink=0
        maxj=j+78 
        if(maxj>=rightimg_pad.shape[1]-1):
            maxj=rightimg_pad.shape[1]-1
        
            
#column loop on right_image
        for col in range(j,maxj):
            left_mat = np.zeros((3,3))
            left_mat = leftimg_pad[i-1:i+2,col-1:col+2]
            diff = np.subtract(right_mat,left_mat)
            diff = np.square(diff)
            sumMat = np.sum(diff)
            
            if min1 > sumMat:
                min1=sumMat
                mink=col
        
        dispright[i][j] = np.abs(j-mink)

cv2.imshow("Right Disparity Matrix",dispright / dispright.max())
mse=np.sum(np.square(dispright[1:dispright.shape[0]-1,1:dispright.shape[1]-1]-groundTruth2))/groundTruth2.size
print mse
      
leftimg_pad = np.lib.pad(left_img,4,padwithzeroes)
rightimg_pad = np.lib.pad(right_img,4,padwithzeroes)

displeft9 = np.zeros((leftimg_pad.shape))
dispright9 = np.zeros((rightimg_pad.shape))

#left_img loop
for i in range(4,leftimg_pad.shape[0]-4):
    for j in range(4,leftimg_pad.shape[1]-4):
        min1 = 9999999
        finalDiff = 0;
        left_mat = np.zeros((9,9))
        left_mat = leftimg_pad[i-4:i+5,j-4:j+5]
        mink=0
        minj=j-78 
        if(minj<=4):
            minj=4
        
            
#column loop on right_image
        for col in range(minj,j+1):
            right_mat = np.zeros((9,9))
            right_mat = rightimg_pad[i-4:i+5,col-4:col+5]
            diff = np.subtract(left_mat,right_mat)
            diff = np.square(diff)
            sumMat = np.sum(diff)
            
            if min1 > sumMat:
                min1=sumMat
                mink=col
        
        displeft9[i][j] = np.abs(j-mink)       

cv2.imshow("Left Disparity Matrix - 9X9 window",displeft9 / displeft9.max())
mse=np.sum(np.square(displeft9[4:displeft9.shape[0]-4,4:displeft9.shape[1]-4]-groundTruth1))/groundTruth1.size 
print mse


#right_img loop
for i in range(4,rightimg_pad.shape[0]-4):
    for j in range(4,rightimg_pad.shape[1]-4):
        min1 = 9999999
        finalDiff = 0;
        right_mat = np.zeros((9,9))
        right_mat = rightimg_pad[i-4:i+5,j-4:j+5]
        mink=0
        maxj=j+78 
        if(maxj>=rightimg_pad.shape[1]-4):
            maxj=rightimg_pad.shape[1]-4
        
            
#column loop on left_img
        for col in range(j,maxj):
            left_mat = np.zeros((9,9))
            left_mat = leftimg_pad[i-4:i+5,col-4:col+5]
            diff = np.subtract(right_mat,left_mat)
            diff = np.square(diff)
            sumMat = np.sum(diff)
            
            if min1 > sumMat:
                min1=sumMat
                mink=col
        
        dispright9[i][j] = np.abs(j-mink)       

cv2.imshow("Right Disparity Matrix - 9X9 window",dispright9 / dispright9.max())
mse=np.sum(np.square(dispright9[4:dispright9.shape[0]-4,4:dispright9.shape[1]-4]-groundTruth2))/groundTruth2.size
print mse



#consistency check


def calMSE(matrix1,matrix2):
    sum_error = 0
    for i in range(matrix1.shape[0]):
        for j in range(matrix1.shape[1]):
            if(matrix1[i][j] != 0):
                error = abs(matrix1[i][j] - matrix2[i][j])
                error = error**2
                sum_error += error

    return sum_error/matrix2.size



leftimg_pad = np.lib.pad(left_img,1,padwithzeroes)
rightimg_pad = np.lib.pad(right_img,1,padwithzeroes)

backpleft = np.zeros((leftimg_pad.shape))

for i in range(1,leftimg_pad.shape[0]):
    for j in range(1,leftimg_pad.shape[1]):
        displ = displeft[i][j]
        index = int(np.abs(j - displ))
        if(index<1):
            continue
        dispr = dispright[i][index]
        if(displ == dispr):
            backpleft[i][j] = displ
        else:
            backpleft[i][j] = 0

cv2.imshow("Back Projection Left",backpleft / backpleft.max())
#mse=np.sum(np.square(backpleft[1:backpleft.shape[0]-1,1:backpleft.shape[1]-1]-groundTruth1))/groundTruth1.size
mse = calMSE(backpleft[1:backpleft.shape[0]-1,1:backpleft.shape[1]-1],groundTruth1)
print mse

backpright = np.zeros((rightimg_pad.shape))

for i in range(1,rightimg_pad.shape[0]):
    for j in range(1,rightimg_pad.shape[1]):
        dispr = dispright[i][j]
        index = int(np.abs(j + dispr))
        if(index>=rightimg_pad.shape[1]):
            continue
        displ = displeft[i][index]
        if(displ == dispr):
            backpright[i][j] = dispr
        else:
            backpright[i][j] = 0

cv2.imshow("Back Projection Right",backpright / backpright.max())
mse = calMSE(backpright[1:backpright.shape[0]-1,1:backpright.shape[1]-1],groundTruth2)

#mse=np.sum(np.square(backpright[1:backpright.shape[0]-1,1:backpright.shape[1]-1]-groundTruth2))/groundTruth2.size
print mse

leftimg_pad = np.lib.pad(left_img,4,padwithzeroes)
rightimg_pad = np.lib.pad(right_img,4,padwithzeroes)

backpleft9 = np.zeros((leftimg_pad.shape))

for i in range(4,leftimg_pad.shape[0]-4):
    for j in range(4,leftimg_pad.shape[1]-4):
        displ = displeft9[i][j]
        index = int(np.abs(j - displ))
        if(index<4):
            continue
        dispr = dispright9[i][index]
        if(displ == dispr):
            backpleft9[i][j] = displ
        else:
            backpleft9[i][j] = 0

cv2.imshow("Back Projection Left 9X9",backpleft9 / backpleft9.max())
mse = calMSE(backpleft9[4:backpleft9.shape[0]-4,4:backpleft9.shape[1]-4],groundTruth1)

#mse=np.sum(np.square(backpleft9[4:backpleft9.shape[0]-4,4:backpleft9.shape[1]-4]-groundTruth1))/groundTruth1.size
print mse

backpright9 = np.zeros((rightimg_pad.shape))

for i in range(4,rightimg_pad.shape[0]-4):
    for j in range(4,rightimg_pad.shape[1]-4):
        dispr = dispright9[i][j]
        index = int(np.abs(j + dispr))
        if(index>=rightimg_pad.shape[1]-4):
            continue
        displ = displeft9[i][index]
        if(displ == dispr):
            backpright9[i][j] = dispr
        else:
            backpright9[i][j] = 0

cv2.imshow("Back Projection Right 9X9",backpright9 / backpright9.max())
mse = calMSE(backpright9[4:backpright9.shape[0]-4,4:backpright9.shape[1]-4],groundTruth2)

#mse=np.sum(np.square(backpright9[4:backpright9.shape[0]-4,4:backpright9.shape[1]-4]-groundTruth2))/groundTruth2.size
print mse



















