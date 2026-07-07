def DisplayFactor(No):
    for i in range(1,No + 1):
        if No % i == 0:
            print(i,end = " ")









def main():
    Value = int(input("Enter a Number"))
    DisplayFactor(Value)






if __name__ =="__main__":
    main()