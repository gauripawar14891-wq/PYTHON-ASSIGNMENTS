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
#Misclassified student
#create result Dataframe
results=X_test.copy()
results["Actual"]=y_test
results["Predicted"]=y_pred#find misclassified students
misclassified=results[
    results["Actual"] !=results["Predicted"]
]
#display misclassified students
print("\nMisclassified Students:")
print("misclassified")
#count misclassified students
print("\nNumber of misclassified Students:",len(misclassified)
      )
#observe comman pattern
if len(misclassified)==0:
    print("\nNo students were misclassified")
    print("Therefore,there is no misclassification pattern")
    print("\nCommon pattern can be observed from the above rows")