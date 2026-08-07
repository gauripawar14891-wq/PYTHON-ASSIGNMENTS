class Arithmatic:
    def __init__(self):
        self.Value1 =0
        self.Value2 =0
    def Accept(self):
        self.Value1 = int(input("Enter first number:"))
        self.Value2 = int(input("Enter second number:"))
    def Addition(self):
        return self.Value1 + self.Value2
    def Subtraction(self):
        return self.Value1 - self.Value2
    def Multiplication(self):
        return self.Value1 * self.Value2
    def Division(self):
        return self.Value1 /  self.Value2
    
def main():
        obj1 =Arithmatic()
        obj2 = Arithmatic()
        print("Enter values for object 1")
        obj1.Accept()
        print("Enter values for object 2")
        obj2.Accept()
        print("\nObject 1 Results")
        print("Addition = ",obj1.Addition())
        print("Subtraction = ",obj1.Subtraction())
        print("Multiplication = ",obj1.Multiplication())
        print("Division = ",obj1.Division())
        print("\nObject 2 Results")
        print("Addition = ",obj2.Addition())
        print("Subtraction = ",obj2.Subtraction())
        print("Multiplication = ",obj2.Multiplication())
        print("Division = ",obj2.Division())

if __name__ =="__main__":
   main()
        






















if __name__ =="__main__":
    main()