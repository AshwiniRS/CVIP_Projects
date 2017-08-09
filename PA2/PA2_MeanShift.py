import cv2
import numpy as np

bf_img = cv2.imread('Butterfly.jpg')
mean_shiftImg = np.zeros((bf_img.shape))
zeros = np.zeros((1,5))
noOfRows = bf_img.shape[0] * bf_img.shape[1] + 1
noOfCols = 5
lookupArr = np.zeros((noOfRows,noOfCols))

delIndex = []

k=0
for i in range(bf_img.shape[0]):
    for j in range(bf_img.shape[1]):
        lookupArr[k][0] = bf_img[i][j][0]
        lookupArr[k][1] = bf_img[i][j][1]
        lookupArr[k][2] = bf_img[i][j][2]
        lookupArr[k][3] = i
        lookupArr[k][4] = j
        k=k+1
 
noOfiterations = 0       
h = 160 
iter1 = 40
#randomF = int(noOfRows/2)
while(lookupArr.shape[0] >1):
    noOfiterations = noOfiterations + 1
    print noOfiterations

    randomF = np.random.randint(lookupArr.shape[0]-1)
    meanCal = np.zeros((0,5))
    list1 = []
    tempInd = []
    for i in range(lookupArr.shape[0]-1):
        #print i
        #if i not in delIndex:    
        temp = lookupArr[i,].reshape(1,5)
        dist = np.sqrt(np.sum((lookupArr[randomF]-lookupArr[i])**2)) 
        if(dist<=h):
            list1.append(i)
            meanCal = np.concatenate((meanCal,temp),axis=0)
    if(len(list1)>0):
        meanRow = np.mean(meanCal,axis=0).reshape(1,5)  
       # print meanRow
        #sumR = 0
        #sumG = 0
        #sumB = 0
        #sumX = 0
        #sumY = 0
        #for y in list1:
        #    sumR += lookupArr[y][0] 
        #    sumG += lookupArr[y][1]
        #    sumB += lookupArr[y][2]
        #    sumX += lookupArr[y][3]
        #    sumY += lookupArr[y][4]
        #
        #meanRow = np.zeros((1,5))
        #
        #meanRow[0][0] = sumR/len(list1)
        #meanRow[0][1] = sumG/len(list1)
        #meanRow[0][2] = sumB/len(list1)
        #meanRow[0][3] = sumX/len(list1)
        #meanRow[0][4] = sumY/len(list1)
        
        
        dist1 = np.sqrt(np.sum((lookupArr[randomF]-meanRow)**2))
       # print dist1
        if(dist1<=iter1):
            for x in list1:
                delIndex.append(x)
                tempInd.append(x)
                y = int(lookupArr[x][3])
                z = int(lookupArr[x][4])
                mean_shiftImg[y][z][0] = meanRow[0][0]
                mean_shiftImg[y][z][1] = meanRow[0][1]
                mean_shiftImg[y][z][2] = meanRow[0][2]
                #lookupArr = np.delete(lookupArr,x,0)
        #for ind in list1: 
            lookupArr = np.delete(lookupArr,tempInd,0)
        #    delIndex.append(i)
            #lookupArr[ind,] = [0,0,0,0,0]
    else:
        delIndex.append(randomF)
        y = int(lookupArr[randomF][3])
        z = int(lookupArr[randomF][4])
        mean_shiftImg[y][z][0] = lookupArr[randomF][0]
        mean_shiftImg[y][z][1] = lookupArr[randomF][1]
        mean_shiftImg[y][z][2] = lookupArr[randomF][2]
        #lookupArr[randomF,] = [0,0,0,0,0]

        lookupArr = np.delete(lookupArr,randomF,0)
cv2.imshow("MS",mean_shiftImg / mean_shiftImg.max())