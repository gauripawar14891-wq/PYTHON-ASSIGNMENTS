Data = [56,45,15,54,78,90]
Value =list(filter(lambda No:No % 3 == 0 and No % 5 == 0,Data))
print(Value)