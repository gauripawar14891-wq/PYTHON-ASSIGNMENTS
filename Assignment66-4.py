# Take input Values from the User

x=float(input("Enter input value: "))

weight = float(input("Enter initial weight: "))

bias=float(input("Enter initial bias : "))

target = float(input("Enter target  output: "))

learning_rate = float(input("Enter learning rate: "))

# Step 1: Calculate Predictions

prediction = weight * x + bias


# Step 2 : Calculate Error

error = target - prediction


# Step 3: Calculate gradients for squared error loss:

dw = -2 * x * error
db = -2 * error

#Store old values :

old_weight = weight
old_bias = bias

# Step 4 : Update weight and bias using gradient descent

weight = weight - learning_rate * dw
bias = bias - learning_rate * db


# Step 5: Display Result

print("\n---Results---")

print("Prediction : ",prediction)

print("Target Output: ",target)

print("Error : ",error)

print("Old weight: ",old_weight)

print("Updated Weight: ",weight)

print("Old Bias: ",old_bias)

print("Updated Bias: ",bias)