Maximum = lambda No1,No2,No3:No1 if No1>No2 and No1 > No3 else No2 if No2 > No3 else No3
No1 =int(input("Enter first number"))
No2 =int(input("Enter second number"))
No3 = int(input("Enter third number"))
Ret = Maximum(No1,No2,No3)
print("Maximum number is: ",Ret)