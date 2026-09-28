import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("student_performance_ml.csv")
plt.hist(df["StudyHours"],bins=8)
plt.title("Histogram of StudyHours")
plt.xlabel("Study Hours")
plt.ylabel("Number of Students")
plt.show()