import MarvellousNum
def ListPrime(Arr):
    Sum = 0
    for No in Arr:
          if MarvellousNum.ChkPrime(No):
               Sum = Sum + No
    return Sum
          
def main():
    Size = int(input("Enter the number of elements: "))
    Data = []
    print("Enter elements: ")
    for i in range(Size):
        No =int(input())
        Data.append(No)
    Result = ListPrime(Data)
    print("Output is: ",Result)

if __name__ =="__main__":
     main()
      