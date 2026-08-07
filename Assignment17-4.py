
def SumFactor(No):
    Sum = 0
    for i in range(1,No):
        if No % i == 0:
            Sum = Sum + i

    print("Sum of the factors is: ",Sum)






def main():

 No = int(input("Enter the number: "))

 SumFactor(No)




if __name__ =="__main__":
    main()