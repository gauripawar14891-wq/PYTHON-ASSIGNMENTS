import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix,ConfusionMatrixDisplay
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