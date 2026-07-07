def SumNatural(No):

    Sum = 0

    for i in range(1, No + 1):
        Sum = Sum + i
        print("Sum of first n Natural Numbers is: ",Sum)


def main():
    Value = int(input("Enter number: "))
    SumNatural(Value)


if __name__ =="__main__":
    main()