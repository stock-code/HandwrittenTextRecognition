import numpy as np
import random
from PIL import Image, ImageChops

Name_List=['CapA','CapB','CapC','CapD','CapE','CapF','CapG','CapH','CapI','CapJ','CapK','CapL','CapM','CapN','CapO','CapP','CapQ','CapR','CapS','CapT','CapU','CapV','CapW','CapX','CapY','CapZ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','tilt','exclaim','at','hash','dollor','perc','power','and','star','roundopen','roundclose','hiphen','plus','underscore','equal','curlyopen','curlyclose','squareopen','squareclose','bslash','pipe','fslash','que','colon','semicolon','lt','gt','comma','dot','singlequote','doublequote','blanck']
Original_List=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','~','!','@','#','$','%','^','&','*','(',')','-','+','_','=','{','}','[',']','\\','|','/','?',':',';','<','>',',','.','\'','\"'," "]
def trim(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0, 0)))
    diff = ImageChops.difference(im, bg)
    size1=diff.getbbox()
    diff = ImageChops.add(diff, diff,2,-100)
    bbox = diff.getbbox()
    if bbox:
        x=(bbox[0],size1[1],bbox[2],size1[3])
        return im.crop(x)

imgs=[]
thought = input("Enter your thoughts:")
rand0=str(random.randint(0,9))
# rand0=str('8')
cropped_Image_Location = "C:/Users/Stock_Code/PycharmProjects/Infosys.CharacterRecognition/CroppedImages/Character/" + rand0 + '_style/'
Output_Image_Location = "C:/Users/Stock_Code/PycharmProjects/Infosys.CharacterRecognition/Output/"
images_list = []
for i in range(0, len(thought)):
    if thought[i].isspace():
        images_list.append(cropped_Image_Location + 'blanck_handwriting.jpg')
        continue
    for j in range(93):
        if thought[i]==Original_List[j]:
            name=cropped_Image_Location + Name_List[j]+'_handwriting.jpg'
            images_list.append(name)
            continue

imgs = [trim(Image.open(i)) if i!=cropped_Image_Location + 'blanck_handwriting.jpg' else Image.open(i) for i in images_list ]

max_img_shape = sorted([(np.max(i.size), i.size) for i in imgs])[0][1]
img_merge = np.hstack((np.asarray(i.resize(max_img_shape, Image.ANTIALIAS)) for i in imgs))

img_merge = Image.fromarray(img_merge)
img_merge.save(Output_Image_Location + 'output.jpg')
