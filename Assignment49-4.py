import numpy as np

from sklearn.preprocessing import StandardScaler

from scipy.spatial.distance import euclidean


data=np.array([

    [25,20000],
    [30,40000]

])

#   distance before scaling

distance_before = euclidean(data[0],data[1])

#  Apply feature scaling

scaler = StandardScaler()

scaled_data=scaler.fit_transform(data)

#  Distance after scaling

distance_after = euclidean(scaled_data[0],scaled_data[1])


print("Euclidean Distance Before Scaling = ",distance_before)


print("Euclidean Distance After Scaling: ",distance_after)

print("\n Explanation: ")

print("Before scaling,the feature with larger numerical values has a greater influence ")

print("After scaling, both the features contribute more equally to the distance ")


