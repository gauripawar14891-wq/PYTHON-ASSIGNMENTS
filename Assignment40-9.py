import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
#load dataset
df=pd.read_csv("student_performance_ml.csv")
#original model
X=df.drop("FinalResult",axis=1)
y=df["FinalResult"]
X_train,X_test,y_train,y_test=train_test_split(
    X,y,test_size=0.2,random_state=42
)
