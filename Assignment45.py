#  Question 1:
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

# Load the csv file



df=pd.read_csv("student_performance_ml.csv")

# display the data
print(df)

#Question 1:

df["Math_Normalized"] = (
    (df["Math"] - df["Math"].min()) / (df["Math"].max()-df["Math"].min())
)

print(df[["Name","Math","Math_Normalized"]])

#Question 2:

# Create Gender Column
df["Gender"] = ["F","M","M"]

#  One-hot Encoding

df=pd.get_dummies(df,columns=["Gender"],dtype=int)

print(df)

#  Question 3:

df_gender=pd.read_csv("student_performance_ml.csv")

df_gender["Gender"] =["F","M","M"]

#  Calculate  average marks

gender_average=df_gender.groupby("Gender")[["Math","Science","English"]].mean()

print(gender_average)

#  Question 4:

#select sagar's marks

sagar=df[df["Name"]=="Sagar"].iloc[0]

subjects=["Math","Science","English"]

marks=[sagar["Math"],sagar["Science"],sagar["English"]]

#plot pie chart

plt.figure(figsize=(6,6))
plt.pie(marks,labels=subjects,autopct="%1.1f%%")
plt.title("Subject Marks of sagar")
plt.show()

# Question 5:
df["Total"]=df["Math"] + df["Science"] + df["English"]
#Add status column
df["Status"] = df["Total"].apply(
    lambda x:"Pass" if x >=250 else "Fail"
)
print(df[["Name","Total","Status"]])

#Question 6:

passed_students=(df["Status"]=="Pass").sum()
print("Number of students passed: ",passed_students)

#Question 7:

df.to_csv("final_student_performance.csv",index=False)
print("Final DataFrame exported successfully")

#  Question *:
 
plt.figure(figsize=(7,5)) 

plt.hist(df["Math"],bins=5,edgecolor="black")

plt.xlabel("Math Marks")
plt.ylabel("Number of students")
plt.title("Histogram of Math Marks")

plt.show()

#Question 9:

df.rename(columns={"Math":"Mathematics"},inplace=True)
print(df)

#Question 10:

plt.figure(figsize=(6,5))
plt.boxplot(df["English"])
plt.ylabel("English Marks")
plt.title("Boxplot of English Marks")
plt.show()