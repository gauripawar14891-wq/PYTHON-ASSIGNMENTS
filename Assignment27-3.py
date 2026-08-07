class Numbers:
    def __init__(self,Value):
        self.Value=Value
    def ChkPrime(self):
        if self.Value <=1:
            return False
        for i in range(2,self.Value):
            if self.Value % i ==0:
                return False
        return True
    def ChkPerfect(self):
        Sum = 0
        for i in range(1,self.Value):
            return True
        else:
            return False
    def Factors(self):
        print("Factors are: ")
        for i in range(1,self.Value + 1):
            if self.Value % i == 0:
                print(i,end=" ")
        print()
    def SumFactors(self):
        Sum =0
        for i in range(1,self.Value +1):
            if self.Value % i ==0:
                Sum =Sum + i
        return Sum

def main():
    No1= int(input("Enter first number : "))
    obj1 = Numbers(No1)
    print("Prime: ",obj1.ChkPrime())
    print("Perfect: ",obj1.ChkPerfect())
    obj1.Factors()
    print("Sum of Factors :",obj1.SumFactors())

    print("---------------------------------------")

    No2= int(input("Enter second number : "))
    obj2 = Numbers(No1)
    print("Prime: ",obj2.ChkPrime())
    print("Perfect: ",obj2.ChkPerfect())
    obj2.Factors()
    print("Sum of Factors :",obj2.SumFactors())

if __name__ =="__main__":
    main()
