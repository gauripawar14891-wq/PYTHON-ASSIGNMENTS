def CountDigits(No):
    Count = 0
    while No > 0:
        No = No // 10
        Count = Count +1


    print("Number of digits:",Count)




def main():
    No =int(input("Enter the number: "))
    CountDigits(No)







if __name__ =="__main__":
    main()
