import cv2
filename = input("File Name :")
img = cv2.imread(filename)
#half = img
x,y,_ = img.shape
temp = 1
if x>100:
    temp = x/100
    temp = 1/temp
else:
    temp = 1

half = cv2.resize(img, (0, 0), fx = temp, fy = temp)
#print(img.shape)
rows,cols,_ = half.shape

thresh_hold = 0
def on_change(value):
    global thresh_hold
    x,y,_ = img.shape
    temp = 1
    if x>100:
        temp = x/100
        temp = 1/temp
    else:
        temp = 1
    thresh_hold = value
    imageCopy = img.copy()
    imageCopy = cv2.resize(img, (0, 0), fx = temp, fy = temp)
    
    rows,cols,_ = imageCopy.shape
    for i in range(rows):
        for j in range(cols):
            try:
                k1 = imageCopy[i,j]
                k2 = imageCopy[i,j+1]
                if abs(k1[0]-k2[0])<thresh_hold and abs(k1[1]-k2[1])<thresh_hold and abs(k1[2]-k2[2])<thresh_hold:
                    imageCopy[i,j+1] = imageCopy[i,j]
                k3 = imageCopy[i+1,j+1]
                if abs(k1[0]-k3[0])<thresh_hold and abs(k1[1]-k3[1])<thresh_hold and abs(k1[2]-k3[2])<thresh_hold:
                    imageCopy[i+1,j+1] = imageCopy[i,j]
                k4 = imageCopy[i+1,j]
                if abs(k1[0]-k4[0])<thresh_hold and abs(k1[1]-k4[1])<thresh_hold and abs(k1[2]-k4[2])<thresh_hold:
                    imageCopy[i+1,j] = imageCopy[i,j]   
                 
            except Exception as e:

                continue
    temp = (img.shape[0]*temp)
    print(temp)
    halfCopy = cv2.resize(imageCopy, (0, 0), fx = 5, fy = 5)
    gray = cv2.cvtColor(halfCopy, cv2.COLOR_BGR2GRAY)
    edged = cv2.Canny(gray, 10, 200)
    contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    #cv2.imshow('Canny Edges After Contouring', edged)
    cv2.drawContours(halfCopy, contours, -1, (0, 0, 0), 3)
    cv2.imshow("Frame", halfCopy)
	


for i in range(rows):
    for j in range(cols):
        try:
            k1 = half[i,j]
            k2 = half[i,j+1]
            if abs(k1[0]-k2[0])<thresh_hold and abs(k1[1]-k2[1])<thresh_hold and abs(k1[2]-k2[2])<thresh_hold:
                half[i,j+1] = half[i,j]
            k3 = half[i+1,j+1]
            if abs(k1[0]-k3[0])<thresh_hold and abs(k1[1]-k3[1])<thresh_hold and abs(k1[2]-k3[2])<thresh_hold:
                half[i+1,j+1] = half[i,j]
            k4 = half[i+1,j]
            if abs(k1[0]-k4[0])<thresh_hold and abs(k1[1]-k4[1])<thresh_hold and abs(k1[2]-k4[2])<thresh_hold:
                half[i+1,j] = half[i,j]   
             
        except Exception as e:

            continue
      
temp = (img.shape[0]*temp)
print(temp)
halfCopy = cv2.resize(half, (0, 0), fx = 5, fy = 5)
print(half.shape)
cv2.imshow("Frame",halfCopy)
cv2.createTrackbar('Threshold', "Frame", 0, 100, on_change)
cv2.waitKey(0)