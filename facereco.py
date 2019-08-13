# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 15:31:10 2019

@author: SUSHMITHA
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt


image=cv2.imread('image.jpg')
fCascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
facedata=[]
facecount=0
cap=cv2.VideoCapture(0)

while True:
    ret,image=cap.read()
    facegray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces=fCascade.detectMultiScale(facegray,1.3,5)
   # edges=cv2.Canny(facegray,300,200)
    for face in faces:
        x,y,h,w=face
        cropedface=image[y:y+h,x:x+w,:]
        resizedface=cv2.resize(cropedface,(50,50))
        if facecount%10==0 and len(facedata)<= 20:
            facedata.append(resizedface)
    facecount+=1
    cv2.putText(image,str(len(facedata)),(50,50),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,255,0),2)
    cv2.imshow('original',image)
    if cv2.waitKey(1)==27:
        cap.release()
        cv2.destroyAllWindows()
        break

cap.release()
cv2.destroyAllWindows()

facedata=np.array(facedata)
np.save('yyy',facedata)
