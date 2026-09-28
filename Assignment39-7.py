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
#generate confusion matrix
cm=confusion_matrix(y_test,y_pred)
print("Confusion Matrix:")
print(cm)
#display confusion matrix
disp=ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["Fail","Pass"]

)
disp.plot()
plt.title("Confusion Matrix")
plt.show()
#training predictions
train_pred=model.predict(X_train)
#testing predictions
test_pred=model.predict(X_test)
#calculate accuracy
training_accuracy=accuracy_score(y_train,train_pred)
testing_accuracy=accuracy_score(y_test,test_pred)
print("Training Accuracy:",training_accuracy)
print("Testing Accuracy:",testing_accuracy)
#convert into percentage
print("Training accuracy:",training_accuracy * 100,"%")
print("Testing Accuracy:",testing_accuracy * 100,"%")
#compare
if training_accuracy > testing_accuracy +0.10:
    print("the model may be overfitting")
elif testing_accuracy < 0.70:
    print("the model may be underfitting")
else:
    print("the model does not show significant overfitting or underfitting")
#model 1 : max_depth=1
model1=DecisionTreeClassifier(max_depth=1,random_state=42)
model1.fit(X_train,y_train)
#prediction
pred1=model1.predict(X_test)
#accuracy
acc1=accuracy_score(y_test,pred1)
#model 2:max_depth=3
model2=DecisionTreeClassifier(max_depth=3,random_state=42)
model2.fit(X_train,y_train)
#prediction
pred2=model2.predict(X_test)
#accuracy
acc2=accuracy_score(y_test,pred2)
#model3:max_depth =none
model3=DecisionTreeClassifier(max_depth=None,random_state=42)
model3.fit(X_train,y_train)
#prediction
pred3=model3.predict(X_test)
#accuracy
acc3=accuracy_score(y_test,pred3)
#display results
print("Testing Accuracy:")
print("max_depth=1:",acc1 * 100,"%")
print("max_depth=3:",acc2 * 100)
print("max_depth=none:",acc3 * 100,"%")

#create newnstudent data
new_student=pd.DataFrame({
    "StudyHours":[6],
    "Attendance":[85],
    "PreviousScore":[66],
    "AssignmentsCompleted":[7],
    "SleepHours":[7]
})
#predict using trained model
prediction=model1.predict(new_student)
#display result
if prediction[0]==1:
    print("Prediction :Pass")
else:
    print("Prediction :Fail")