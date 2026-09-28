import pandas as pd
df=pd.read_csv("student_performance_ml.csv")
print("first 5 records:")
print(df.head())
print("\n Last 5 records:")
print(df.tail())
print("\n total number of rows and columns:")
print(df.shape)

print("\n column names:")
print(df.columns.tolist())
print("\n Data Types:")
print(df.dtypes)