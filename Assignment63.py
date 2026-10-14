# Loan Default Prediction Using MLPClassifier

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score,confusion_matrix

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    precision_score,
    recall_score,
    f1_score,ConfusionMatrixDisplay

)

#  1 . Load and understand the dataset


df=pd.read_csv("Loan_Default.csv")
print("Dataset loaded successfully!")
print("\nFirst Five Records: ")
print(df.head())


print("\nDataset Shape: ")
print(df.shape)

print("\nDataset Columns: ")
print(df.columns.tolist())

print("\nDataset information: ")
df.info()

print("\nStatistical Summary: ")
print(df.describe(include="all"))

# 2 . Perform exploratory data analysis

print("\nDefault value counts: ")
print(df["Default"].value_counts())

print("\nAverage values: ")
print(df.select_dtypes(include=np.number).mean())

df["Default"].value_counts().sort_index().plot(
    kind="bar",
    title="Loan Default Class Distribution",
    xlabel="Default (0 = Low Risk, 1 = High Risk)",ylabel="Number of Applicants")

plt.tight_layout()
plt.show()

# 3 . Find Missing Values

print("\nMissing Values before cleaning : ")
print(df.isnull().sum())

for column in df.columns:
    if df[column].isnull().any():
        if df[column].dtype=="object":
            df[column]=df[column].fillna(df[column].mode()[0])
        else:
            df[column]=df[column].fillna(df[column].median())

print("\nMissing values after cleaning: ")
print(df.isnull().sum())

# 4 . check whether target classes are balanced

class_counts = df["Default"].value_counts().sort_index()

print("\nClass Distribution : ")
print(class_counts)

print("\nClass Percentages: ")
print((df["Default"].value_counts(normalize=True) * 100))

if class_counts.min() / class_counts.sum() < 0.30:
    print("The Dataset maybe imbalanced")
else:
    print("The classes are balanced")


# 5 . Encode Categorical variables

print("\nCategorical columns:")
print(df.select_dtypes(include=["object","category"]).columns.tolist())

df["PreviousDefault"]=df["PreviousDefault"].map({
    "Yes":1,"No":0
})

df=pd.get_dummies(
    df,columns=["HomeOwnership"],dtype=int
)

print("\nDataset after encoding : ")
print(df.head())

# 6 . Seperate X and Y

X=df.drop("Default",axis=1)

y=df["Default"].astype(int)

print("\n Independent Variables shape: ",X.shape)
print("Target variables shape : ",y.shape)

# 7 . Split into training and testing data

X_train,X_test,y_train,y_test=train_test_split(
      X,
      y,
      test_size=0.25,
      random_state=42,
      stratify=y
)

print("\nTraining Data Shape: ",X_train.shape)
print("Testing data shape: ",X_test.shape)

# 8 . Explain Stratified splitting

print("\nStratified splitting is used to preserve")
print("\nApproximately the same target class proportions")
print("\n in the training and testing datasets")

# 9 . Scale the Features

scaler=MLPClassifier(
    hidden_layer_size=(32,16),
    activation="relu",
    solver="adam",
    learning_rate_init=0.001,
    max_iter=1000,
    random_state=42
    

)

print("\nMLPClassifier created successfully")

# 11 . Train the model

model.fit(X_train_scaled,y_train)
print("\nModel Training completed")

# 12 . Calculate Accuracy:

y_train_pred = model.predict(X_train_scaled)
y_test_pred=model.predict(X_test_scaled)

train_accuracy=accuracy_score(y_train,y_train_pred)
test_accuracy = accuracy_score(y_test,y_test_pred)

print("\nTraining Accuracy:",round(train_accuracy * 100,2),"%")
print("\nTesting Accuracy:",round(test_accuracy * 100,2),"%")

print("\nNumber of trainiing iterations: ",model.n_iter_)
print("Final training loss: ",model.loss_)

# 13 . Generate the confusion matrix

cm=confusion_matrix(y_test,y_test_pred,labels=[0,1])

print("\nConfusion Marix: ")
print(cm)

ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=["Low Risk","High Risk"]).plot()

plt.title("Loan Default Confusion Matrix")
plt.tight_layout()

plt.show()

# 14 . Generate Classification Report

print("Classification Report: ")
print(classification_report(y_test,y_test_pred,labels=[0,1],target_name=["Low Risk","High Risk"],zero_division=0))


# 15 . Calculate precision,recall and F1 score

precision= precision_score(y_test,y_test_pred,zero_division=0)

recall = recall_score(y_test,y_test_pred,zero_division=0)

f1 = f1_score(y_test,y_test_pred,zero_division=0)

print("\nPrecision : ",round(precision,4))
print("\nRecall : ",round(recall,4))
print("\nF1 - score : ",round(f1,4))


# 16 . Plot the Training Loss

plt.figure(figsize=(8,5))

plt.plot(range(1,len(model.loss_curve_) +1),model.loss_curve_)

plt.xlabel("Iterations")
plt.ylabel("Loss")
plt.title("MLP Training Loss Curve")
plt.grid(True)
plt.tight_layout()
plt.show()

# 17 .  Test the model on new loan Applicants

def PredictDefault(applicant_data):

    applicant_df = pd,DataFrame([applicant_data])
    applicant_df["PreviousDefault"] = (applicant_df["PreviousDefault"].map({"Yes":1,"No":0}))
    applicant_df = pd.get_dummies(applicant_df,columns=["HomeOwnership"],dtype=int)

# Match the feature columns used during training

    applicant_df=applicant_df.reindex(columns=X.columns,fill_value=0)

    applicant_scaled=scaler.transform(applicant_df)

    prediction=model.predict(applicant_scaled)[0]

    probability=model.predict_proba(applicant_scaled)[0][1]

    if prediction == 1:
      result = "High default risk"
    else:
      result="Low default Risk"
    return result,probability

#sample new loan applicants

new_applicants = [
    {
               "Age":26,
               "Income":320000,
               "LoanAmount":180000,
               "CreditScore":590,
               "EmploymentYears":2,
               "ExsistingLoans":2,
               "MonthlyDebt":15000,
               "LoanTerm":36,
               "PreviousDefault":"Yes",
               "HomeOwnerShip":"Rent"
    },
    {
                "Age":45,
                "Income":950000,
                "LoanAmount":250000,
                "CreditScore":790,
                "EmploymentYears":15,
                "ExsistingLoans":1,
                "MonthlyDebt":9000,
                "LoanTerm":60,
                "PreviousDefault":"No",
                "HomeOwnerShip":"Own"
    },
    {
        
                "Age":32,
                "Income":520000,
                "LoanAmount":200000,
                "CreditScore":680,
                "EmploymentYears":6,
                "ExsistingLoans":1,
                "MonthlyDebt":12000,
                "LoanTerm":48,
                "PreviousDefault":"No",
                "HomeOwnerShip":"Mortgage"
    }
]

print("\nPredictions for new applicants: ")

for i,applicant in enumerate(new_applicants,start=1):

    result,probability = PredictDefault(applicant)

    print(f"\nApplication {i}:")
    print("Prediction: ",result)
    print("Estimated probability of default:",round(probability * 100,2),"%")

#   Hyperparameter experiments :

def run_experiment(parameter_name,values):

    print("\nExperiment:{parameter_name}")
    results = []

    for value in values:
        params = {
            "hidden_layer_sizes":(32,16),
            "activation":"relu",
            "solver":"adam",
            "learning_rate_init": 0.001,
            "max_iter": 1000,
            "random_state": 42

        }

        params[parameter_name]=value
        experiment_model=MLPClassifier(**params)
        experiment_model.fit(X_train_scaled,y_train)
        predictions=experiment_model.predict(X_test_scaled)
        accuracy = accuracy_score(y_test,predictions)
        results.append({"Parameter":parameter_name,"Value":str(value),"Test Accuracy":round(accuracy,4),"Iterations":experiment_model.n_iter_,"Final Loss":round(experiment_model.loss_,4)})

        print(f"{value}:Accuracy={accuracy:.4f},"f"Iterations={experiment_model.n_iter_}")
        return results

    # Experiment 1: Activation Functions

    activation_results = run_experiment("activation",["identity","logistic","tanh","relu"])

    #Experiment 2 :Hidden layer structures 
    layer_results =run_experiment(
        "hidden_layer_sizes",[(10,),(20,10),(50,25),(100,50,25)]
    )

    #Experiment 3:Learning Rates

    learning_rate_results = run_experiment("learning_rate_init",[0.0001,0.001,0.001])

    #Display all experiment results

    experiment_results = pd.DatFrame(activation_results + layer_results + learning_rate_results)

    print("\nHyperparameter Experiment Results:")

    print(experiment_results.to_string(index=False))

    