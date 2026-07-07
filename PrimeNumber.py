def CheckPrime(No):
    Count = 0
    for i in range(2,No):
        if No % i == 0:
            Count = Count + 1
    if Count == 0 and No > 1:
        print("Prime number")
    else:
        print("Not Prime Number")







def main():
    Value = int(input("Enter the number: "))
    CheckPrime(Value)









if __name__ =="__main__":
    main()