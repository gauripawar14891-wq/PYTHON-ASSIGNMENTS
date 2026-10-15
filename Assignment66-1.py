import math


# Input Values

x1=2

x2=3

# Weights and bias

w1=0.4

w2=0.6

bias=0.5

# Step 1 : Calculate weighted sum


weighted_sum= (x1 * w1) + (x2 * w2) + bias


# step 2 : Apply sigmoid activation function

output = 1 / (1 + math.exp(-weighted_sum))

#step 3 :Display Results

print("Weighted Sum : ",weighted_sum)

print("Sigmoid Output: ",output)

# Step 4: Check whether output is close to 0 or 1

if output < 0.5:
    print("output is closer to 0")
else:
    print("Output is closer to 1")