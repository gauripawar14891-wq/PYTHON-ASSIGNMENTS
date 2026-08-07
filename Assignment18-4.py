def Frequency(Arr,Value):
    Count = 0
    for No in Arr:
          if No == Value:
               Count = Count + 1
    return Count
          
def main():
    Size = int(input("Enter the number of elements: "))
    Data = []
    print("Enter elements: ")
    for i in range(Size):
        No =int(input())
        Data.append(No)
    Value = int(input("Element to search: "))
    Result = Frequency(Data,Value)
    print("Output is: ",Result)

if __name__ =="__main__":
     main()
      