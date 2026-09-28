#student performance prediction using decision tree
#import libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import(
    accuracy_score,confusion_matrix,ConfusionMatrixDisplay
)
#Dataset Loading
#read CSV file
df=pd.read_csv("Student_performance_ml.csv")
print("Dataset loaded successfully")
print()
#Data Analysis
print("First 5 records:")
print(df.head())
print("\nDataset Information:")
print(df.info())
print("\nStatistical Summary:")
print(df.describe())
print("\nMissing Values:")
print(df.isnull().sum())
#seperate input and output
#X contains input features
X=df.drop("FinalResult",axis=1)
#y contains target variable
y=df["FinalResult"]
#train-test split
X_train,X_test,y_train,y_test=train_test_split(
    X,y,test_size=0.2,random_state=42
)
print("\nTraining Records:",len(X_train))
print("Testing records:",len(X_test))
#model training
#create Decision Tree Classifier
model=DecisionTreeClassifier(random_state=42)
#train the model
model.fit(X_train,y_train)
print("\nDecision Tree Model trained successfully")
#prediction
#predict the test data
y_pred=model.predict(X_test)
print("\nPredicted Results:")
print(y_pred)
#Accuracy calculation
#training prediction
train_pred=model.predict(X_train)
#calculate training accuracy
training_accuracy=accuracy_score(y_train,train_pred)
#calculate testing accuracy
testing_accuracy=accuracy_score(y_test,y_pred)
print("\nTraining Accuracy:",training_accuracy * 100,"%")
print("Testing Accuracy:",testing_accuracy * 100,"%")
#confusion matrix generation
cm=confusion_matrix(y_test,y_pred)
print("\nConfusion Matrix:")
print(cm)
#display confusion matrix
disp=ConfusionMatrixDisplay(
    confusion_matrix=cm,display_labels=["Fail","Pass"]
)
disp.plot()
plt.title("Student performance - Confusion Matrix")
plt.show()
#predict new student
#new student details
new_student=pd.DataFrame({
    "StudyHours":[6],
    "Attendance":[85],
    "PreviousScore":[66],
    "AssignmentsCompleted":[7],
    "SleepHours":[7]
})
#make predictions
new_prediction=model.predict(new_student)
#display predictions
if new_prediction[0]==1:
    print("\nNew Student Prediction:PASS")
else:
    print("\nNew Student Prediction:FAIL")
    #Final Conclusion
    print("\n-------------------------FINAL CONCLUSION-----------")
    print("Training Accuracy:",training_accuracy * 100,"%")
    print("Testing accuracy:",testing_accuracy * 100,"%")
    if training_accuracy > testing_accuracy + 0.10:
        print("Conclusion:the model may be overfitting")
    elif testing_accuracy < 0.70:
        print("Conclusion:the model may be underfitting")
    else:
        print("Conclusion:No significant overfitting or underfitting is observed for this train_test_split")
    if new_prediction[0]==1:
        print("The new student is predicted to PASS")
    else:
        print("The new student is predicted to FAIL")
