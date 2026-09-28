import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
#load dataset
df=pd.read_csv("Student_performance_ml.csv")
#seperate features and target
X=df.drop("FinalResult",axis=1)
y=df["FinalResult"]
#split dataset
X_train,X_test,y_train,y_test=train_test_split(
    X,y,test_size=0.2,random_state=42
)
#create and train decision tree model
model=DecisionTreeClassifier(random_state=42)
model.fit(X_train,y_train)
#predict test data
y_pred=model.predict(X_test)
correct_predictions=0
for actual,predicted in zip(y_test,y_pred):
    if actual==predicted:
        correct_predictions +=1
total_predictions=len(y_test)
#calculate accuracy manually
manual_accuracy=correct_predictions / total_predictions
print("Correct Predictions:",correct_predictions)
print("Total_predictions:",total_predictions)
print("Manual Accuracy:",manual_accuracy)
print("Manual Accuracy %: ",manual_accuracy * 100)
