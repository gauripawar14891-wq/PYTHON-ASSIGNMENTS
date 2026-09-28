import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix,ConfusionMatrixDisplay
from sklearn.metrics import accuracy_score
new_students=pd.DataFrame({
    "StudyHours":[2,4,5,7,8],
    "Attendance":[60,70,80,90,95],
    "PreviousScore":[40,50,60,70,80],
    "AssignmentsCompleted":[2,4,6,8,9],
    "SleepHours":[5,6,7,8,8]
})
#predict using trained Model
df=pd.read_csv("Student_performance_ml.csv")
#input and target
X=df.drop("FinalResult",axis=1)
y=df["FinalResult"]
#split Data
X_train,X_test,y_train,y_test=train_test_split(
    X,y,
    test_size=0.2,
    random_state=42
)
#create and train the model
model=DecisionTreeClassifier(random_state=42)
model.fit(X_train,y_train)
predictions=model.predict(new_students)
#add predictions to DataFrame


new_students["PredictedResult"]=predictions
#convert 0 and 1 into Fail and Pass
new_students["PredictedResult"]=new_students["PredictedResult"].map({
    0:"Fail",
    1:"Pass"
})
#display result
print("\nDetails and predictions of 5 new students:")
print(new_students)