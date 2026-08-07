from functools import reduce
def main():
    Data = list(map(int,input("Enter the numbers: ").split()))
    FData= list(filter(lambda No : No % 2 == 0,Data))
    print("Data after filter is : ",FData)
    MData = list(map(lambda No : No * No,FData))
    print("Data after map= ",MData)
    RData = reduce(lambda No1,No2: No1 + No2,MData)
    print("Data after reduce: ",RData)
if __name__ =="__main__":
    main()