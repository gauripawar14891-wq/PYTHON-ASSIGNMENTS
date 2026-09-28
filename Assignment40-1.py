import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix,ConfusionMatrixDisplay
from sklearn.metrics import accuracy_score
#load dataset
df=pd.read_csv("student_performance_ml.csv")
#seperate input and output
X=df.drop("FinalResult",axis=1)
y=df["FinalResult"]
#train-test split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
#train Decision Tree Model
model=DecisionTreeClassifier(random_state=42)
model.fit(X_train,y_train)
#prediction
y_pred=model.predict(X_test)
accuracy=accuracy_score(y_test,y_pred)
importance=model.feature_importances_
for feature,score in zip(X.columns,importance):
    print(feature,":",score)
#question 1-feature importance
print("\n===========================")
print("Question 1:Feature importance")
print("=============================")
importance=pd.DataFrame({
    "Feature":X.columns,
    "Importance":model.feature_importances_
})
print(importance)
#most important feature
most_important=importance.loc[importance["Importance"].idmax()
                              ]
#least important feature
least_important=importance.loc[
    importance["Importance"].idxmin()
]
print("\nMost important feature:")
print(most_important)
print("\nLeast important feature:")
print(least_important)
#question 2-remove sleephours
print("\n=============================")
print("question 2:remove sleephours")
print("===============================")
X_without_sleep =df.drop(
    ["FinalResult","Sleephours"],axis=1
)
X_train2,X_test2,y_train2,y_test2=train_test_split(
    X_without_sleep,
    y,
    test_size=0.2,
    random_state=42
)
model2=DecisionTreeClassifier(random_state=42)
model2.fit(X_train2,y_train2)
y_pred2=model2.predict(X_test2)
accuracy2=accuracy_score(y_test2,y_pred2)
print("Previous Accuracy:",accuracy)
print("New Accuracy:",accuracy2)
print("Previous Accuracy %",accuracy * 100)
print("New Accuracy %:",accuracy2 * 100)
if accuracy2==accuracy:
    print("Removing SleepHours did NOT affect accuracy")
elif accuracy2 < accuracy:
    print("Removing SleepHours decreased perforance")
else:
    print("Removing SleepHours improved performance")
#question 3:only studyhours and attendance
print("\n===================================")
print("Question 3:STUDYHOURS + ATTENDANCE")
print("=====================================")
X_two_features=df["FinalResult"["StudyHours","Attendance"]
                  ]
X_train3,X_test3,y_train3,y_test3=train_test_split(
    X_two_features,
    y,test_size=0.2,
    random_state=42
)
model3=DecisionTreeClassifier(random_state=42)
model3.fit(X_train3,y_train3)
y_pred3=model3.predict(X_test3)
accuracy3=accuracy_score(y_test3,y_pred3)
print("Full Feature Model Accuracy:",accuracy)
print("StudyHours + Attendance Accuracy:",accuracy3)
print("Full Feature Accuracy %:",accuracy * 100)
print("two feature accuracy %:",accuracy3 * 100)
if accuracy3==accuracy:
    print("The model is still performing well")
else:
    print("The performance has changed")