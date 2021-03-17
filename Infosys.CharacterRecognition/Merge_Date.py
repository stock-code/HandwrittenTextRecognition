import cv2
import numpy as np
import random
cropped_Image_Location = "C:/Users/Stock_Code/PycharmProjects/Infosys.CharacterRecognition/"
date=input("Enter Date:")
rand0=str(random.randint(1,9))
rand0=str('b')
images_list=[]

for i in range(0,len(date)):

    if date[i]=='/':
        images_list.append(cv2.imread(cropped_Image_Location+'CroppedImages/'+rand0+'_style/fslash_handwriting.jpg'))
    elif date[i]=='\\':
        images_list.append(cv2.imread(cropped_Image_Location+'CroppedImages/'+rand0+'_style/bslash_handwriting.jpg'))
    elif date[i]=='-':
        images_list.append(cv2.imread(cropped_Image_Location+'CroppedImages/'+rand0+'_style/hiphen_handwriting.jpg'))
    elif int(date[i]) in range(0,10):
        images_list.append(cv2.imread(cropped_Image_Location+'CroppedImages/'+rand0+'_style/'+date[i]+'_handwriting.jpg'))


class Merge(object):
    def __init__(self,initial_image):
        self.merge = initial_image
        self.x,self.y = self.merge.shape[:2]

    def append(self,image):
        image = image[:,:,:3]
        x,y = image.shape[0:2]
        new_image = cv2.resize(image,(int(y*float(self.x)/x),self.x))
        self.merge = np.hstack((self.merge,new_image))

    def generate(self):
        cv2.imwrite(cropped_Image_Location + 'Output/output.jpg', self.merge)
        # cv2.imshow('date', self.merge)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

Final_Image=Merge(images_list[0])

for i in range(1,len(date)):
    # print(i)
    Final_Image.append(images_list[i])

Final_Image.generate()