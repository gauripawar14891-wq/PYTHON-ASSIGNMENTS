def FactNo(Value):
    Fact = 1
    for i in range(1,Value + 1):
        Fact = Fact * i
        print("Factorial of a number is: ",Fact)






def main():
    Value = int(input("Enter the number: "))
    FactNo(Value)







if __name__ =="__main__":
    main()