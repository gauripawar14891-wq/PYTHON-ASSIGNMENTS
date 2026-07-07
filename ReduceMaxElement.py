from functools import reduce
Data = [45,87,59,63,28]

Result = reduce(lambda No1,No2 : No1 if No1>No2 else No2,Data)
print(Result)