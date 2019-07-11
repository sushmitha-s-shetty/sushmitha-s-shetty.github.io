import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv('50_Startups.csv')

data.columns
x = np.array(data.iloc[:,0:4].values)
y = np.array(data.iloc[:,0:4].values)

from sklearn.preprocessing import LabelEncoder

lEncoder = LabelEncoder()
x[:,3] = lEncoder.fit_transform(x[:,3])

#assigning dummi values is called one hot encoder
from sklearn.preprocessing import OneHotEncoder

ohEncoder = OneHotEncoder(categorical_features=[3])
 
x = ohEncoder.fit_transform(x).toarray()

x = x[:,1:]

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()

regressor.fit(x_train,y_train)
y_pred = regressor.predict(x_test)

score = regressor.score(x_test,y_test)


from sklearn.metrics import mean_squared_error
mse = mean_squared_erroe(y_test,y_pred)**(1/2) 