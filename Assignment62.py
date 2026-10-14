#  Employee Attrition Prediction System using MLPClassifier

import pandas as pd

import matplotlib.pyplot as plt

import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.metrics import classification_report,ConfusionMatrixDisplay


# 1 . Load the dataset using Pandas

df=pd.read_csv("Employee_Attrition.csv")
print("Dataset loaded successfully!")

# 2.  Display shape,columns and first five records

print("\nDataset Shape: ")
print(df.shape)


print("\nDataset Columns: ")
print(df.columns.tolist())

print("\nFirst Five Records: ")
print(df.head())


# 3. Check for missing values:

print("\nMissing Values: ")
print(df.isnull().sum())


#Handle missing Values if any

for column in df.columns:
    if df[column].isnull().any():
        if df[column].dtype=="object":
            df[column]=df[column].fillna(df[column].mode()[0])
        else:
            df[column]=df[column].fillna(df[column].median())

# 4 .Identify numerical and categorical features:

categorical_features=df.select_dtypes(include=["object","category"]).columns.tolist()

numerical_features=df.select_dtypes(include=["number"]).columns.tolist()

print("\nNumerical Features: ")

print(numerical_features)

print("\nCategorical Features: ")

print(categorical_features)

# 5. Convert categorical features into numerical form

df["OverTime"] =df["OverTime"].map({"Yes":1,"No":0})


#6. Convert target Attrition into 0 and 1

# 0:Employee stays
#1.Employee leaves


df["Attrition"]=df["Attrition"].map({"Yes":1,"No":0})

#check for invalid or unmapped values

if df[["OverTime","Attrition"]].isnull().any().any():
    raise ValueError("check OverTime and Attrition values in the csv")

print("\nDataset after encoding: ")

print(df.head())

# 7.Seperate independent and dependent variables


X=df.drop("Attrition",axis=1)
y=df["Attrition"]

print("\nIndependent variables Shape:",X.shape)
print("Depenedent Variables Shape:",y.shape)

# 8.split dateset into training and testing data

X_train,X_test,y_train,y_test=train_test_split(
      X,
      y,
      test_size=0.25,
      random_state=42,
      stratify=y
)

print("\nTraining Data Shape:",X_train.shape)
print("Testing Data Shape:",X_test.shape)

# 9 . Apply Feature Scaling

scaler=StandardScaler()

X_train_scaled=scaler.fit_transform(X_train)

X_test_scaled=scaler.transform(X_test)

print("\nFeature scaling completed")

# 10.create MLP with two hidden layers

model=MLPClassifier(
    hidden_layer_sizes=(16,8),
    activation="relu",
    solver="adam",
    learning_rate_init=0.001,
    max_iter=1000,
    random_state=42
)

print("\nMLP model created successfully")


# 11. Train the neural network

model.fit(X_train_scaled,y_train)

print("Model training completed")

#12. Display numner of training iterations

print("\nNumber of iterations Required: ")
print(model.n_iter_)

print("\n Final Training Loss: ")
print(model.loss_)

# 13. calculate training accuracy:

y_train_pred=model.predict(X_train_scaled)

train_accuracy=accuracy_score(y_train,y_train_pred)

print("\nTraining Accuracy:",round(train_accuracy * 100,2), "%")

#  14.Calculate testing accuracy

y_test_pred=model.predict(X_test_scaled)

test_accuracy=accuracy_score(y_test,y_test_pred)

print("Testing Accuracy:",round(test_accuracy * 100,2), "%")

#15.Generate confusion Matrix

cm=confusion_matrix(y_test,y_test_pred,labels=[0,1])

print("\nConfusion Marix: ")
print(cm)

ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=["Stay","Leave"]).plot()

plt.title("Employees Attrition Confusion Matrix")
plt.tight_layout()

plt.show()

print("Classification Report: ")
print(classification_report(y_test,y_test_pred,labels=[0,1],target_name=["Stay","Leave"],zero_division=0))

#16. Plot the Loss Curve

plt.figure(figsize=(8,5))
plt.plot(range(1,len(model.loss_curve_) + 1),model.loss_curve)

plt.xlabel("Iterations")
plt.ylabel("Loss")
plt.title("MLP Training Loss Curve")
plt.grid(True)
plt.tight_layout()
plt.show()

# 17. Create PredictAttriction(employee_data)  function

def PredictAttrition(employee_data):

    employee_df=pd.DataFrame([employee_data],columns=X.columns)

    employee_df["OverTime"]= employee_df["OverTime"].map({"Yes":1,"No":0})

    employee_df=employee_df.astype(float)

    employee_scaled=scaler.transform(employee_df)
    prediction=model.predict(employee_scaled)[0]

    probability=model.predict_proba(employee_scaled)[0][1]


    if prediction ==1:
        result="Employee is likely to leave"
    else:
        result="Employee is likely to Stay"
        return result,probability

    
# 18. Test using five new employee records

new_employee=[
    {
        "Age":26,
        "MonthlyIncome":3200,
        "YearsAtCompany":1,
        "TotalWorkingYears":3,
        "DistanceFromHome":15,
        "JobSatisfaction":2,
        "WorkLifeBalance":2,
        "OverTime":"Yes",
        "NumCompaniesWorked":4,
        "TrainingTimesLastYear":1
    },
    {
        "Age":45,
        "MonthlyIncome":8500,
        "YearsAtCompany":12,
        "TotalWorkingYears":22,
        "DistanceFromHome":4,
        "JobSatisfaction":4,
        "WorkLifeBalance":3,
        "OverTime":"No",
        "NumCompaniesWorked":2,
        "TrainingTimesLastYear":3
    },
    {
        "Age":30,
        "MonthlyIncome":4000,
        "YearsAtCompany":2,
        "TotalWorkingYears":5,
        "DistanceFromHome":18,
        "JobSatisfaction":1,
        "WorkLifeBalance":2,
        "OverTime":"Yes",
        "NumCompaniesWorked":5,
        "TrainingTimesLastYear":2
    },
    {
        "Age":40,
        "MonthlyIncome":7200,
        "YearsAtCompany":8,
        "TotalWorkingYears":16,
        "DistanceFromHome":5,
        "JobSatisfaction":4,
        "WorkLifeBalance":4,
        "OverTime":"No",
        "NumCompaniesWorked":2,
        "TrainingTimesLastYear":3
    },
    {
        "Age":34,
                
        "MonthlyIncome":5000,
        "YearsAtCompany":4,
        "TotalWorkingYears":9,
        "DistanceFromHome":10,
        "JobSatisfaction":3,
        "WorkLifeBalance":2,
        "OverTime":"Yes",
        "NumCompaniesWorked":3,
        "TrainingTimesLastYear":2
    },
    
    
]

print("\nPredictions for Five New Employees:")

for i,employee in enumerate(new_employees,start=1):

    result,probability=PredictAttrition(employee)

    print(f"\nEmployee {i}:")
    print("Prediction:",result)
    print("Probability of leaving:",round(probability * 100,2),"%")

# 19. Check for overfitting or underfitting

print("\nModel Evaluation: ")

difference=train_accuracy - test_accuracy
if train_accuracy < 0.60 and test_accuracy < 0.60:

    print("Possible underfitting : both accuracies are low ")

elif difference > 0.15 and train_accuracy > 0.70:

    print("Possible overfitting:training accuracy is: ")

    print("Significantly hogher than testing accuracy")

else:
    print("No strong evidence of overfitting based")

    print("On the Accuracy comparison alone")
    


                                   

