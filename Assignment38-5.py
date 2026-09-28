import pandas as pd
df=pd.read_csv("student_performance_ml.csv")
print("Average Study Hours by Result:")
print(df.groupby("FinalResult")["StudyHours"].mean())
print("\nAverage Attendance by Result:")
print(df.groupby("FinalResult")["Attendance"].mean())