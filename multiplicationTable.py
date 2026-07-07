def Table(No):
    for i in range(1,11):
       Mult = No * i

       print("Multiplication Table is: ",Mult)





def main():
    Value = int(input("Enter the number: "))
    Table(Value)





if __name__ =="__main__":
    main()