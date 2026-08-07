from functools import reduce
def CheckPrime(No):
    if No < 2:
        return False
    for i in range(2,No):
        if No % i ==0:
         return False
    return True

def main():
    Data = list(map(int,input("Enter the numbers: ").split()))
    FData = list(filter(CheckPrime,Data))
    print("Data after filter is: ",FData)
    MData =list(map(lambda No:No * 2,FData))
    print("Data after map: ",MData)
    RData= reduce(lambda No1,No2:No1 if No1>No2 else No2,MData)
    print("Data after reduce: ",RData)
if __name__ =="__main__":
    main()