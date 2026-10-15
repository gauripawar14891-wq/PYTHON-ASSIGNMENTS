import math


#  Actual and Predicted values

actual = [1 , 0 , 1]

predicted = [0.9 , 0.2 , 0.8]

n = len(actual)

# Step 1: Calculate Mean Squared Error (MSE)

squared_error = 0

for i in range(n):

    squared_error += (actual[i] - predicted[i]) **2

mse = squared_error / n


#Step 2: Calculate Binary Cross Entropy (BCE)

epsilon = 1e-15

cross_entropy = 0

for i in range(n):
    p=max(epsilon,min(1 - epsilon,predicted[i]))

    cross_entropy += (actual[i] * math.log(p) + (1 - actual[i]) * math.log(1- p ))

    bce = -cross_entropy / n


#Step 3: Display results

print("Actual Values: ",actual)

print("Predicted Values: ",predicted)

print("Mean Squared Error: ",mse)

print("Binary Cross Entropy: ",bce)


# Step 4:Explain their Uses

print("MSE is commonly used for regression")

print("BCE is commonly used for classification")
