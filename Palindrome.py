def CheckPalindrome(No):
    Temp = No
    Rev = 0

    while No!=0:
        Digit=No % 10
        Rev = (Rev * 10) + Digit
        No = No // 10

    if Temp == Rev:
        print("Number is Palindrome")
    else:
        print("Number is not Palindrome")





def main():
    Value = (int(input("Enter the number: ")))
    CheckPalindrome(Value)








if __name__ =="__main__":
    main()