def Factorial(No):
   Fact = 1
   for i in range(1,No + 1):
      Fact = Fact * i
      print("Factorial of a number is: ",Fact)
   



def main():

  Value = int(input("Enter the number: "))
  Factorial(Value)








if __name__ =="__main__":
    main()