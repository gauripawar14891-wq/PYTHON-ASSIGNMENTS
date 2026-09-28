import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
#load dataset
df=pd.read_csv("Student_performance_ml.csv")
#seperate features and target
X=df.drop("FinalResult",axis=1)
y=df["FinalResult"]
#compare different random_state values
random_states=[0,10,42]
for rs in random_states:
    #split dataset
    X_train,X_test,y_train,y_test=train_test_split(
        X,y,test_size=0.2,random_state=rs
    )
    #create decision tree model
    model=DecisionTreeClassifier(
        random_state=rs
    )
    #train model
    model.fit(X_train,y_train)
    #predict test data
    y_pred=model.predict(X_test)
    #calculate testing accuracy
    accuracy=accuracy_score(
        y_test,y_pred
    )
    print("\nRandom State:",rs)
    print("Testing Accuracy:",accuracy)
    print("Testing Accuracy %:",accuracy * 100)