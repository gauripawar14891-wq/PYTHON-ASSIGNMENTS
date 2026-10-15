import numpy as np
import matplotlib.pyplot as plt

# generate input values from -10 to 10

x=np.linspace(-10,10,200)

#Activation functions
sigmoid = 1 / ( 1 + np.exp(-x))
relu = np.maximum(0,x)
tanh = np.tanh(x)

#  Plot activation functions


plt.figure(figsize=(10,6))

plt.plot(x, sigmoid,label="Sigmoid")

plt.plot(x, relu,label="ReLU")

plt.plot(x, tanh,label="Tanh")

plt.title("Different Activation Functions")

plt.xlabel("Input")

plt.ylabel("Output")

plt.axhline(0,color="black",linewidth=0.5)

plt.axvline(0,color="black",linewidth=0.5)

plt.grid(True)

plt.legend()

plt.show()

# Display explanations

print("Sigmoid : Converts values into the range 0 and 1")

print("ReLU:Returns 0 for negative inputs and x for positive inputs")

print("Tanh:Converts values into the range -1 to 1")