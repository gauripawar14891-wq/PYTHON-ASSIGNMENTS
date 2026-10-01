  #Step 1:Import required libraries 
import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression

#Get Data

#Load Dataset

data=pd.read_csv("Advertising.csv")

print("Dataset:")
print(data)

print("First 5 records:")
print(data.head())

#Step 2:Clean ,prepare and manipulate data

#display column name

print("\n Column Names:")
print(data.columns)

#check for missing values
print("\n Missing Values:")
print(data.isnull().sum())
#seperate input features and output
#tv,radio,newspaper=independent variables
#sales=dependent variables

X=data[["TV","radio","newspaper"]]
Y=data["sales"]

print("\nInput Features")
print(X.head())
print("\nOutput / sales:")
print(Y.head())

#step 3:Train Data
#divide dataset into training and testing data
#50% training and 50% testing

X_train,X_test,Y_train,Y_test=train_test_split(
    X,
    Y,
    test_size=0.50,
    random_state=42
)
print("\nTraining Data:")
print(X_train)
print("\nTesting Data:")
print(X_test)


# create  linear regression object
model=LinearRegression()


#train the model

model.fit(X_train,Y_train)


#  step 4: Test the Data

#predict sales using testing data
Y_pred=model.predict(X_test)

#step 5:Display predicted and Expected Output

print("\nExpected Saes Values: ")
print(Y_test.values)

print("\nPredicted Sales Values")
print(Y_pred)

#Display expected and predicted Values together

result=pd.DataFrame({
    "Expected Sales":Y_test.values,
    "Predicted Sales":Y_pred
})

print("\nExpected VS Predicted Sales: ")
print(result)