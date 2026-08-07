
def SumDigits(No):
     Sum = 0
     while No > 0:
          Digit = No % 10
          Sum = Sum + Digit
          No = No // 10
     print("Sum of the digitsis : ",Sum)



def main():
     No =int(input("Enter the number"))
     SumDigits(No)


if __name__ == "__main__":
     main()