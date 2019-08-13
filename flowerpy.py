

from sklearn.datasets import load_iris
iris=load_iris()
#accesing from dictionary
x=iris["data"]
y=iris.target
target_names=iris.target_names

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)

from sklearn.linear_model import LogisticRegression
clf=LogisticRegression()
clf.fit(x_train,y_train)

#this for flask using this file used to load
from sklearn.externals import joblib
joblib.dump(clf,'irisPred.sav')



from sklearn.externals import joblib
model=joblib.load('irisPred.sav')
model.predict([[5.8,2.8,5.1,2.4]])
#this below code for iris pred
"""
y_pred=clf.predict(x_test)

score=clf.score(x_test,y_test)

a=eval(input("enter the data "))
#1,a=a.split(',')
a=list(a)
pred=clf.predict([a])
        

print("the flower is",target_names[pred])
"""