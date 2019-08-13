
import cv2
import numpy as np
import matplotlib.pyplot as plt

fCascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

names={0:'sush',1:'prathi'}
person1=np.load('sush.npy').reshape(21,50*50*3)
person2=np.load('p.npy').reshape(21,50*50*3)

data=np.concatenate([person1,person2])
labels=np.zeros((42,1))
labels[21:,:]=1

from sklearn.neighbors import KNeighborsClassifier
clf=KNeighborsClassifier(n_neighbors=5)
clf.fit(data,labels)

cap=cv2.VideoCapture(0)
while True:
    ret,image=cap.read()
    imGray=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    faces=fCascade.detectMultiScale(imGray,1.3,5)
    for (x,y,w,h) in faces:
        cropedface=image[y:y+h,x:x+w,:]
        resizedface=cv2.resize(cropedface,(50,50))
        reshapedface=resizedface.reshape(1,50*50*3)
        pred=clf.predict(reshapedface)
        name=names[int(pred)]
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(image,name,(x,y),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,255,255),2)
    cv2.imshow("output",image)
    if cv2.waitKey(1)==27:
        cap.release()
        cv2.destroyAllWindows()
        break
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        