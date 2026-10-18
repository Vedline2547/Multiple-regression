# Import necessary libraries
import pandas as pd
import numpy as np
import plotly.express as px 
import plotly.graph_objects as go
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
# Creating data
X,y = make_regression(n_samples=100,n_features=2,n_informative=2,n_targets=1,noise=10)
df = pd.DataFrame({'feature1':X[:,0],'feature2':X[:,1],'target':y})
# print(df.shape)
fig = px.scatter_3d(df,x='feature1',y='feature2',z='target')
fig.show()
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)
lr = LinearRegression()
lr.fit(X_train,y_train)
y_pred = lr.predict(X_test)
print("MAE: ",mean_absolute_error(y_test,y_pred))
print("MSE: ",mean_squared_error(y_test,y_pred))
print("RMSE: ",np.sqrt(mean_squared_error(y_test,y_pred)))
print("R2-Score: ",r2_score(y_test,y_pred))