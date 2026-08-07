def ChkNum(Value):
    if Value > 0:
        print("Number is positive")
    elif Value < 0:
        print("Number is negative")
    else:
        print("Zero")









def main():
    No = int(input("Enter the number: "))
    ChkNum(No)










if __name__ =="__main__":
    main()