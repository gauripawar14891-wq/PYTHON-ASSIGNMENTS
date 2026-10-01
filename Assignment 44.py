

# Question 1:


import pandas as pd

data={
    'Name':['Amit','Sagar','Pooja'],
    'Math':[85,90,78],
    'Science':[92,88,80],
    'English':[75,85,82]
}

df=pd.DataFrame(data)

print("Shape:",df.shape)
print("Columns:",df.columns)
print("Data Types:\n",df.dtypes)

# Question 2:

print(df.describe())


#  Question 3

df['Total'] =df['Math'] + df['Science'] + df['English']

print(df)

#  Question 4:

print(df [ df ['Science'] > 85 ] )

#  Question 5:

df['Name'] =df['Name'].replace('Charlie','Chris')

print(df)

#  Question 6:
df_sorted = df.sort_values(by='Total',ascending=False)

print(df_sorted)


#   Question 7:

import matplotlib.pyplot as plt

plt.bar(df['Name'],df['Total'])

plt.xlabel('Student Name')
plt.ylabel('Total Marks')
plt.title('Total Marks by Student')

plt.show()

#  Question 8:

alice_marks=df[df['Name'] == 'Alice'] [['Math','Science','English']].values.flatten()

subjects=['Math','Science','English']
plt.plot(subjects,alice_marks,marker='0')

plt.title("Allice's Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.grid(True)
plt.show()

#  Question 9:

import numpy as np

data2= {
    'Name':['Dan','Eve','Frank'],
        'Math':[np.nan,76,88],
        'Science':[91,np.nan,85],
        

}
df2=pd.DataFrame(data2)

df2.fillna(df2.mean(numeric_only=True),inplace=True)
print(df2)

#  Question 10:

df_dropped=df.drop(columns=['English'])

print(df_dropped)

#  Question 11 :

df['Math_Norm'] = (
    (df['Math'] - df['Math'].min())  /  (df['Math'].min())
)

print(df[['Name','Math','Math_Norm']])

#  Question 12 :

df['Gender'] =['F','M','M']
df_encoded=pd.get_dummies(df,columns=['Gender'])

print(df_encoded)


#  Question 13:

print(
    df.groupby('Gender')[['Math','Science','English']].mean()
)

#Question 14:

bob=df[df['Name'] == 'Bob'][['Math','Science','English']].values.flatten()

labels=['Math','Science','English']
plt.pie(
    bob,
    labels=labels,
    autopct='%1.1f%%'
)


plt.title("Bob's Subject Wise Distribution")
plt.show()

#  Question 15

df['Status'] = df['Total'].apply(
    lambda x:'Pass' if x >= 250 else 'Fail')

print(df[['Name','Total','Status']])

#  Question 16:

print("Total Passed: ",df[df['Status'] =='Pass'].shape[0])

# Question 17:

df.to_csv('student_result.csv',index=False)

print("DataFrame exported successfully")

#  Question 18:

plt.hist(
    df['Math'],
    bins=5,
    edgecolor='black'
)

plt.title("Distribution of Math Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.grid(True)

plt.show()

#  Question 19:

df.rename(
    columns={'Math':"Mathematics"},
    inplace=True
)
print(df.head())

#  Question 20:

plt.boxplot(df['English'])
plt.title("Boxplot of English Marks")
plt.ylabel("Marks")
plt.grid(True)

plt.show()
