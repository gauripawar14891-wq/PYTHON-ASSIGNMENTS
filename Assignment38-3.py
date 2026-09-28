import pandas as pd
df=pd.read_csv("student_performance_ml.csv")
print("average study hours:",df["StudyHours"].mean())
print("Average Attendance:",df["Attendance"].mean())
print("Maximum Previous Score:",df["PreviousScore"].max())
print("Minimum Sleep Hours:",df["SleepHours"].min())