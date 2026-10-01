#Machine Learning Assignment for classification using k_nearest neighbors


####################################
# Step 1:Get Data
####################################

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score

# Load Dataset

df=pd.read_csv("PlayPredictor (1).csv")
print("Dataset:")
print(df)
print("\nFirst 5 records: ")
print(df.head())


################################################
#Step 2:Clean,Prepare and Manipulate Data
################################################

#Create Label Encoders
WeatherEncoder = LabelEncoder()
TempratureEncoder=LabelEncoder()
PlayEncoder=LabelEncoder()

#convert weather into numeric values
df["Weather"]=WeatherEncoder.fit_transform(df["Weather"])

#convert Temprature into numeric Values
df=["Temprature"]=TempratureEncoder.fit_transform(df["Temprature"])
#convert play into numeric values
df["Play"]=PlayEncoder.fit_transfor9df["Teprature"]
#conert play into nueri alues
df["Play"]=PlayEncoder.fit_transfor(df["Play"])

print("\nEncoded Dataset:")
print(df)
#seperate features and target
X=df[["Weather","Temprature"]]
Y=df["Play"]
print("\nInput features:")
print(X)

print("\n Target: ")
print(Y)
##########################################################
# sTEP 3: Train Data
##########################################################
#create KNN Classifier
#K=3 

model=KNeighborsClassifier(n_neighbors=3)
#train model using whole dataset
model.fit(X,Y)
print("\nModel trained successfully")
##########################################################
# Step 4:Test Data
##########################################################


#Take weather and temprature values fro user

print("\nEnter Weather")
print("1.Sunny")
print("2.Overcast")
print("3.Rainy")
weather=input("Enter Weather:")
print("\nEnter Temprature:")
print("1.Hot")
print("2.cold/cool")
print("Mild")
temprature=input("Enter Temprature:")

#convert user input into encoded values

weather_value=WeatherEncoder.transform([weather])[0]
temprature_value=TempratureEncoder.transform([temprature])[0]


#create test data
test_data=[[weather_value,temprature_value]]

#predict result

prediction=model.predict(test_data)


#convert numeric prediction back to yes/no

result=PlayEncoder.inverse_transform(prediction)

print("/nPrediction Result: ")
print("Play: ",result[0])


####################################################
# Step 5: Calculate Accuracy
####################################################

def CheckAccuracy(K):


# Divide dataset into two equal parts

 X_train,X_test,Y_train,Y_test=train_test_split(
    X,
    Y,
    test_size=0.5,
    random_state=42

)

#create KNN MOdel

 model=KNeighborsClassifier(n_neighbors=K)


# Train Model

 model.fit(X_train,Y_train)

#predict test Data

 Y_pred=model.pedict(X_test)

#calculate accuracy
 accuracy=accuracy_score(Y_test,Y_pred)
 return accuracy


# calculate accuracy for different values of K

print("\nAccuracy for K=1:")
print(CheckAccuracy(1) * 100,"%")

print("\nAccuracy for K=3:")
print(CheckAccuracy(3) * 100,"%")

print("\nAccuracy for K=5:")
print(CheckAccuracy(5) * 100,"%")

print("\nAccuracy for K=7:")
print(CheckAccuracy(7) * 100,"%")