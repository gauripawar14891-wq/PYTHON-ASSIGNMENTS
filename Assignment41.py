#Wine classification using achine learning

#step 1:Get Data

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
#load wine dataset
df=pd.read_csv("WinePredictor (2).csv")
print(df)
print("\n First 5 records:")
print(df.head())
#step 2:clean,prepare and manipulate Data
#check missing values
print("\nMissing Values:")
print(df.isnull().sum())
#remove duplicate records
df=df.drop_duplicates()
print("\n Dataset after removing duplicates")
print(df.head())
#seperate input features and target
X=df.drop("Class",axis=1)
y=df["Class"]
print("\nInput Features:")
print(X.head())
print("\n Target Classes:")
print(y.head())
#split data into training and testing data
X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
print("\nTraining Data Shape:")
print(X_train.shape)
print("\nTesting Data Shape:")
print(X_test.shape)
#feature scaling
scaler=StandardScaler()
X_train=scaler.fit_transform(X_train)
X_test=scaler.transform(X_test)
#step 3:Train Data
#create machine learning model
model=LogisticRegression(max_iter=1000)
#train the model
model.fit(X_train,y_train)
print("\n Model Trained Successfully")
#step 4:Test Data
#Predict classes using testing data
y_pred=model.predict(X_test)
print("\nActual Classes: ")
print(y_test.values)
print("\nPredicted Classes:")
print(y_pred)
#step 5:Calculate Accuracy
accuracy=accuracy_score(y_test,y_pred)
print("\nAccuracy:")
print(accuracy)
print("\nAccuracy Percentage:")
print(accuracy * 100,"%")
