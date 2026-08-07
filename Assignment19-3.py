from functools import reduce
def main():
    Data = list(map(int,input("Enter numbers : ").split()))
    FData =list(filter(lambda No : No >=70 and No <=90,Data))
    print("List after filter = ",FData)
    MData =list(map(lambda No : No + 10,FData))
    print("List after map = m",MData)
    RData = reduce(lambda No1,No2:No1 * No2,MData)
    print("List of reduce = ",RData)
if __name__ =="__main__":
    main()
