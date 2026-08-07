def Minimum(Data):
    Min = Data[0]
    for No in Data:
          if No < Min:
               Min= No
    return Min
          
def main():
    Size = int(input("Enter the number of elements: "))
    Data = []
    print("Enter elements: ")
    for i in range(Size):
        No =int(input())
        Data.append(No)
    Result = Minimum(Data)
    print("Output is: ",Result)

if __name__ =="__main__":
     main()
      