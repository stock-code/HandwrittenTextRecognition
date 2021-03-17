import cv2
import os
Name_List=['CapA','CapB','CapC','CapD','CapE','CapF','CapG','CapH','CapI','CapJ','CapK','CapL','CapM','CapN','CapO','CapP','CapQ','CapR','CapS','CapT','CapU','CapV','CapW','CapX','CapY','CapZ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','tilt','exclaim','at','hash','dollor','perc','power','and','star','roundopen','roundclose','hiphen','plus','underscore','equal','curlyopen','curlyclose','squareopen','squareclose','bslash','pipe','fslash','que','colon','semicolon','lt','gt','comma','dot','singlequote','doublequote','blanck']
BLACK_THRESHOLD = 200
MIN_SIZE = 30
MAX_SIZE = 300
THIN_THRESHOLD = max(10, MIN_SIZE)
FILE_NAME = "8_Handwriting.jpg"
PADDING = 5

cropped_Image_Location = "E:/Projects/Handwritten_Text_Creation/Infosys.CharacterRecognition/Input_Handwriting/Character"

# Sort Contours on the basis of their x-axis coordinates in ascending order
def sort_contours(contours):
    # construct the list of bounding boxes and sort them from top to bottom
    boundingBoxes = [cv2.boundingRect(c) for c in contours]
    (contours, boundingBoxes) = zip(*sorted(zip(contours, boundingBoxes), key=lambda b: b[1][1], reverse=False))
    # return the list of sorted contours
    return contours



img = cv2.imread("Input_Handwriting/Character/"+FILE_NAME)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Don't use magic numbers
thresh = cv2.threshold(gray, thresh=BLACK_THRESHOLD, maxval=255, type=cv2.THRESH_BINARY_INV)[1]

# Find the contours
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

hierarchy = hierarchy[0]  # get the actual inner list of hierarchy descriptions

# Grab only the innermost child components
inner_contours = [c[0] for c in zip(contours, hierarchy) if c[1][3] > 0]

sorted_contours = sort_contours(inner_contours)
j=''
i = 0
# For each contour, find the bounding rectangle and extract it
dir=cropped_Image_Location+"CroppedImages/Character/"+str(FILE_NAME[0])+"_style"
if not os.path.exists(dir):
    os.mkdir(dir)
for contour in sorted_contours:
    x, y, w, h = cv2.boundingRect(contour)

    # Skip thin contours (vertical and horizontal lines)
    if (h < THIN_THRESHOLD) or (w < THIN_THRESHOLD):
        continue
    if (h > MAX_SIZE) and (w > MAX_SIZE):
        continue
    if i>93:

         continue
    roi = img[(y + PADDING):(y + h - PADDING), (x + PADDING):(x + w - PADDING)]
    j = Name_List[i]

    print(j)
    cv2.imwrite(cropped_Image_Location + "CroppedImages/Character/" + str(FILE_NAME[0]) + "_style/" + str(j) + "_handwriting.jpg",roi)
    i += 1