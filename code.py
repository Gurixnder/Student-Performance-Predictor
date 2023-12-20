#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# In[53]:


student_data = pd.read_csv("dataset/Student_Performance.csv", dtype = {'Performance Index':'int64'})
student_data.info()



# In[7]:


student_data["Performance Index"].value_counts()


# In[10]:


from sklearn.model_selection import train_test_split


# In[76]:


features = ["Hours Studied", "Previous Scores", "Sample Question Papers Practiced"]
X = student_data[features]
y = student_data["Performance Index"]

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2, random_state = 42)


# In[83]:


from sklearn.metrics import mean_squared_error, r2_score


# In[79]:


from sklearn.linear_model import LinearRegression
L = LinearRegression()
L.fit(X_train, y_train)


# In[80]:


y_pred = L.predict(X_test)


# In[84]:


mse = mean_squared_error(y_test, y_pred)
r2s = r2_score(y_test, y_pred)
print("R2 score: ", r2s)
print("Mean Squared Error: ", mse)


# In[82]:


plt.scatter(y_test, y_pred)
plt.xlabel("Actual values")
plt.ylabel("Predicted values")
plt.show()


# In[86]:


from sklearn.linear_model import Ridge
R=Ridge(alpha = 0.0001)


# In[88]:


R.fit(X_train, y_train)


# In[89]:


y_pred1 = R.predict(X_test)


# In[90]:


print("R2 score: ", r2_score(y_test, y_pred1))
print("Mean Squared Error: ", mean_squared_error(y_test, y_pred1))


# In[92]:


def getPrediction(hours_studied, prev_scores, sample_ques_practiced):
    data = np.column_stack((hours_studied, prev_scores, sample_ques_practiced))
    pred = L.predict(data)
    pred = int(pred)
    return pred


# In[97]:


print(getPrediction(4,93,1))


# In[101]:




