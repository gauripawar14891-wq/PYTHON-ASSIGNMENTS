import pandas as pd
df=pd.read_csv("student_performance_ml.csv")
print("Total students:",len(df))
passed=(df["FinalResult"]==1).sum()
failed=(df["FinalResult"]==0).sum()
print("passed students:",passed)
print("failed students:",failed)