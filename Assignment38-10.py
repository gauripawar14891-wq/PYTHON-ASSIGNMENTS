import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("student_performance_ml.csv")
df.boxplot(column="SleepHours",by="FinalResult")
plt.xlabel("Final Result")
plt.ylabel("Sleep Hours")
plt.title("Sleep Hours vs Final Result")
plt.suptitle("")
plt.xticks([1,2],["Fail","Pass"])
plt.show()