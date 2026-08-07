def Maximum(Data):
     Max = Data[0]
     for No in Data:
          if No > Max:
               Max = No
     return Max
          
def main():
    Size = int(input("Enter the number of elements: "))
    Data = []
    print("Enter elements: ")
    for i in range(Size):
        No =int(input())
        Data.append(No)
    Result = Maximum(Data)
    print("Output is: ",Result)

    if __name__ =="__main__":
            main()
      








if __name__ =="__main__":
    main()