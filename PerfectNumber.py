
def CheckPerfect(No):
    Sum = 0
    for i in range(1,No):
        if No % i == 0:
            Sum = Sum + i
    if Sum == No:
        print("Number is a perfect number")
    else:
        print("number is not a perfect number")








def main():
    Value = int(input("Enter the number"))
    CheckPerfect(Value)








if __name__ =="__main__":
    main()