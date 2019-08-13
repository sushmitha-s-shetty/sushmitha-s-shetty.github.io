#face recognition
import cv2
import numpy as np
import matplotlib.pyplot as plt

image=cv2.imread('image.jpg')
#plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
"""
fCascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

imGray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
plt.subplot(1,2,1)
plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
plt.subplot(1,2,2)
#plt.imshow(cv2.cvtColor(imGray,cv2.COLOR_BGR2RGB))
#plt.imshow(imGray,cmap="gray")#gray
"""
"""

face=fCascade.detectMultiScale(imGray,1.3,5)

x,y,h,w=face[0]
newface=image[y:y+h,x:x+w,:]
newgray=cv2.cvtColor(newface,cv2.COLOR_BGR2RGB)
newedge=cv2.Canny(newgray,50,200)
#plt.imshow(cv2.cvtColor(newface,cv2.COLOR_BGR2RGB)) here we can giveinstead newface differenylike newegde different image appear
#plt.imshow(newface,cmap="gray")
"""
"""
#plt.imshow(image)

image=cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,255),2)#make rectangle to perticular person
image=cv2.putText(image,'lena',(x,y),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,255,0),2)#font displayed

#plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))#dispaly

#multiple person detect
image=cv2.imread('image.jpg')
imgray=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
faces=fCascade.detectMultiScale(imGray,1.15,5)
for face in faces:
    x,y,h,w=face
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,255),2)
plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
  """  












cap=cv2.VideoCapture(0)

while True:
    ret,image=cap.read()
    facegray=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    faces=fCascade.detectMultiScale(facegray,1.3,5)
    edges=cv2.Canny(facegray,300,200)
    for face in faces:
        x,y,h,w=face
        #cv2.rectangle(edges,(x,y),(x+w,y+h),(0,255,255),2)#for color
        cv2.rectangle(edges,(x,y),(x+w,y+h),(255,0,255),2)#foredges
    cv2.imshow('video',edges)
    if cv2.waitKey(1)==27:
        cap.release()
        cv2.destroyAllWindows()
        break








