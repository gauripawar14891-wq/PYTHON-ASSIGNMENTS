#  Fraudulent Transaction Detection

#Step 1: Import Required Libraries

import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns 

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import (
    BaggingClassifier,
    RandomForestClassifier,
    AdaBoostClassifier,
    VotingClassifier
)

from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report

)

#     Step 2: Load the Dataset
df = pd.read_csv("Fraudulent_Transaction_Detection.csv")

print("First Five Rows :")
print(df.head())

print("\nDataset shape: ")
print(df.shape)

#  Step 3: Check Missing Values

print("\nMissing Values: ")
print(df.isnull().sum())

#  Step 4:  Seperate input and output Variables

target="Fraud"

if target not in df.columns:
    raise ValueError("Target column 'Fraud' not found.")

X=df.drop(columns=[target])
y=df[target]


#  Remove an ID column if it is  present

id_columns= [
    col for col in X.columns
    if col.lower() in ["id","transactionid","transaction_id"]
]

X=X.drop(columns=id_columns)

#  Convert target to numeric if necessary

if y.dtype =="object":

 y=y.astype(str).str.strip().str.lower().map({
        "0":0,
        "1":1,
        "normal":0,
        "normal transaction":0,
        "legitimate":0,
        "not fraud":0,
        "fraud":1,
        "fraudulent":1,
        "fraudulent transaction":1
    })
if y.isnull().any():
        raise ValueError(
            "Target column must contain only 0/1 or recognized"
            "normal/fraud labels.check the Fraud column."
        )

y=y.astype(int)

if set(y.unique()) !={0,1}:
       raise ValueError("Fraud target must contain both classes 0 and 1.")
       
       
print("\n Target distribution:")
print(y.value_counts())

#  Step 5:  Identify numerical and categorical columns

numerical_columns=X.select_dtypes(
      include=["int64","float64","int32","float32"]
).columns.tolist()

categorical_columns = X.select_dtypes(
      include=["object","category","bool"]
).columns.tolist()


# Step 6: Preprocess Data

numerical_pipeline=Pipeline([
    ("imputer",
     SimpleImputer(strategy="median")) ,
     ("scaler",StandardScaler()) 
])

categorical_pipeline = Pipeline([
      ("imputer",
       SimpleImputer(strategy="most_frequent")),
       ("encoder",
        OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer([
      ("num",numerical_pipeline,numerical_columns),
      ("cat",categorical_pipeline,categorical_columns)
])

#Step 7:split into training and testing datasets

X_train,X_test,y_train,y_test=train_test_split(
      X,
      y,
      test_size=0.2,
      random_state=42,
      stratify=y
)

print("\n Training size:",X_train.shape)
print("\n Testing size:",X_test.shape)


# Step 8: Define the five algorithms

models={
      "Decision Tree":DecisionTreeClassifier(
            random_state=42,
            class_weight="balanced"
      ),

      "Bagging":BaggingClassifier(
            estimator=DecisionTreeClassifier(
                  random_state=42,
                  class_weight="balanced"
            ),
            n_estimators=100,
            random_state=42,
            n_jobs=-1
      ),

      "Random Forest":RandomForestClassifier(
          n_estimators=100,
          random_state=42,
          class_weight="balanced",
          n_jobs=-1
      ),
      "AdaBoost":AdaBoostClassifier(
            n_estimators=100,
            random_state=42
      )
}

# Step 9: Create Voting Classifier

voting_model=VotingClassifier(
      estimators=[
            (
                  "lr",
                  LogisticRegression(
                        max_iter=1000,
                        class_weight="balanced"
                  )
            ),
            (
                  "dt",
                  DecisionTreeClassifier(
                        max_depth=10,
                        random_state=42,
                        class_weight="balanced"
                  )
            ),
            (
                  "rf",
                  RandomForestClassifier(
                        n_estimators=100,
                        random_state=42,
                        class_weight="balanced",
                        n_jobs=-1
                  )
            )
      ],
      voting="soft"
)
models["Voting"] = voting_model

#  Step 10: Train models and evaluate performance

result=[]
confusion_matrices={}

for name,model in models.items():

    print("\nTraining:",name)

    # Preprocessing is fitted on training data only


    pipeline=Pipeline([
      ("preprocessing",preprocessor),
      ("model",model)
       ])

    pipeline.fit(X_train,y_train)

       #  predict test data

    y_pred = pipeline.predict(X_test)

       # Calculate evaluation metrics

    accuracy = accuracy_score(y_test,y_pred)

    precision = precision_score(
              y_test,y_pred,zero_division=0
        )

    recall=recall_score(
              y_test,y_pred,zero_division=0
        )

    f1=f1_score(
              y_test,y_pred,zero_division=0
        )
    cm = confusion_matrix(
        y_test,y_pred,labels=[0,1]
    )

    confusion_matrices[name]=cm

    result.append({
              "Algorithm":name,
              "Accuracy":accuracy,
              "Precision":precision,
              "Recall":recall,
              "F1 Score":f1
})
    print("\n",name,"Results")
    print("Accuracy:",round(accuracy,4))
    print("Precision:",round(precision,4))
    print("Recall:",round(recall,4))
    print("F1 Score:",round(f1,4))
    print("\nconfusion Matrix:")
    print(cm)
    print("\nClassification Report: ")
    print(classification_report(
              y_test,
              y_pred,
              labels=[0,1],
              target_names=[
                    "Normal Transaction",
                    "Fraudulent Transaction"
               ],
                zero_division=0
    ))

# Step 11:  Display final comparison table

comparison=pd.DataFrame(result)

print("\nFinal Comparison of All Models")
print(comparison.round(4).to_string(index=False))

#  Step 12: Plot Model Comparison

comparison_plot=comparison.set_index("Algorithm")[
      ["Accuracy","Precision","Recall","F1 Score"]
]

comparison_plot.plot(
      kind="bar",
      figsize=(12,6)
)

plt.title("Fraud Detection Model Performance comparison")

plt.ylabel("Score")
plt.ylim(0,1)
plt.xticks(rotation=30,ha="right")
plt.legend(loc="lower right")
plt.tight_layout()
plt.show()

# Step 13:  plot confusion matrices

fig,axes=plt.subplots(2,3,figsize=(14,8))

axes=axes.flatten()

for i,(name,cm) in enumerate(confusion_matrices.items()):
    sns.heatmap(
      cm,
      annot=True,
      fmt="d",
      cmap="Blues",
      xticklabels=["Normal","Fraud"],
      yticklabels=["Normal","Fraud"],
      ax=axes[i]

    )
    axes[i].set_title(name)
    axes[i].set_xlabel("Predicted Label")
    axes[i].set_ylabel("Actal Label")

    # Hide unused Subplot

    for j in range(len(confusion_matrices),len(axes)):

       axes[j].axis("off")

    plt.tight_layout()
    plt.show()



    #Step 14:Recommend the best model
    #F1 score is prioritized because fraud datasets are often imbalanced


    best_model=comparison.loc[
        comparison["F1 Score"].idxmax()
]


print("\nRecommended Model:",best_model["Algorithm"])
print("Accuracy:",round(best_model["Accuracy"],4))
print("Precision:",round(best_model["Precision"],4))
print("Recall:",round(best_model["Recall"],4))
print("F1 Score:",round(best_model["F1 Score"],4))






      

    