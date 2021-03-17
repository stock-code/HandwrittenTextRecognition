import cv2
import numpy as np
import os
def get_contour_precedence(contour, cols):

    origin = cv2.boundingRect(contour)
    return (origin[1] ) * cols + origin[0]


cropped_Image_Location = "C:/Users/Stock_Code/PycharmProjects/Infosys.CharacterRecognition/"

input="DateInputs/1_Handwriting.jpg"
image = cv2.imread(cropped_Image_Location+"Input_Handwriting/"+input)
gray= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
(thresh, im_bw) = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
v = np.median(im_bw)
sigma=0.33
lower = int(max(0, (1.0 - sigma) * v))
upper = int(min(255, (1.0 + sigma) * v))
edges = cv2.Canny(gray, lower, upper)
cv2.imwrite(cropped_Image_Location + 'CroppedImages/edges-50-150.jpg', edges)
minLineLength = 0
lines = cv2.HoughLinesP(image=edges, rho=1, theta=np.pi / 180, threshold=100, lines=np.array([]),minLineLength=minLineLength, maxLineGap=200000)

try:
    a, b, c = lines.shape
    print(a,b,c)

    for i in range(a):
        cv2.line(im_bw, (lines[i][0][0], lines[i][0][1]), (lines[i][0][2], lines[i][0][3]), (255, 255, 255), 5, cv2.LINE_AA)
except:
    pass
#cv2.imshow("gray",gray)



_,thresh = cv2.threshold(im_bw,70,255,cv2.THRESH_BINARY_INV)
# kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
# dilated = cv2.dilate(thresh,kernel,iterations = 0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
ctr_sorted=sorted(contours, key=lambda ctr: cv2.boundingRect(ctr)[0] + cv2.boundingRect(ctr)[1]* image.shape[0])
#max_width = np.sum(contours[::, (0, 2)], axis=1).max()
# max_height = np.max(thresh[::, 3])
# nearest = max_height * 1.4
# print(nearest)
# contours.sort(key=lambda r: round( float(r[1] / nearest)))

i=0
k=1
j=i
for contour in ctr_sorted:

    [x,y,w,h] = cv2.boundingRect(contour)
    print(x,y,w,h)
    #print(x,y,w,h)
    if w>2 and h>1:
        #print(x, y, w, h,"........")
        cv2.rectangle(im_bw, (x-3, y-3), (x + w+3, y + h+3), (0, 0, 0), 1)#image,left-upper,right-lowwer,color,width
        if i==10:
            j='oslash'
        elif i==11:
            j='bslash'
        elif i==12:
            j='hiphen'
        else:
            j=i
        dir=cropped_Image_Location+"CroppedImages/"+str(input[0])+"_style"
        if not os.path.exists(dir):
            os.mkdir(dir)
        cv2.imwrite(cropped_Image_Location+"CroppedImages/"+str(input[0])+"_style/"+str(j)+"_handwriting.jpg",image[y-2:y+h+2,x-2:x+w+2])

        i=i+1
cv2.imwrite(cropped_Image_Location+"CroppedImages/"+str(input[0])+'_style/lectureAll.jpg', im_bw)
# cv2.imshow("gray",im_bw)
cv2.waitKey(0)
cv2.destroyAllWindows()
