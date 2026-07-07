from functools import reduce
Data = [2,4,5,6,14,54]
Result = reduce(lambda No1,No2: No1 * No2,Data)
print(Result)