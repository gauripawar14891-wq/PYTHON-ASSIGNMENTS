import pandas as pd
df=pd.read_csv("student_performance_ml.csv")
result_count=df["FinalResult"].value_counts()
print(result_count)
pass_percent= (result_count[1] / len(df)) *100
fail_percent= (result_count[0] / len(df)) *100
print("Pass Percentage =",round(pass_percent,2),"%")
print("Fail Percentage =",round(fail_percent,2),"%")
if abs(pass_percent - fail_percent)<=10:
    print("Dataset is Balanced")
else:
    print("Dataset is Imbalanced")