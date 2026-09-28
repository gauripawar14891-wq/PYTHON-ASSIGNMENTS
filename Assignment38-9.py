import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("student_performance_ml.csv")
pass_students=df[df["FinalResult"]==1]
fail_students=df[df["FinalResult"]==0]
plt.scatter(pass_students["AssignmentsCompleted"],pass_students["FinalResult"],label="Pass")
plt.scatter(fail_students["AssignmentsCompleted"],fail_students["FinalResult"],label="Fail")
plt.xlabel("Assignments Completed")
plt.ylabel("Final Result")
plt.title("Assignments Completed vs Final Result")
plt.legend()
plt.show()