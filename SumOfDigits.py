def SumDigits(No):
    Sum = 0
    while No!=0:
        Digits = No % 10
        Sum = Sum + Digits
        No = No // 10
    print("Sum of Digits is: ",Sum)








def main():
    Value = int(input("Enyter the number: "))

    SumDigits(Value)







if __name__ =="__main__":
    main()