from functools import reduce
Data = [1,2,3,4,5]

Result = reduce(lambda No1,No2 : No1 + No2,Data)
print(Result)