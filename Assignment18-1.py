def Addition(Data):
     Sum = 0 
     for No in Data:
          Sum =Sum + No
     return Sum
          
def main():
    Size = int(input("Enter the number of elements: "))
    Data = []
    print("Enter elements: ")
    for i in range(Size):
        No =int(input())
        Data.append(No)
    Result = Addition(Data)
    print("Addition is: ",Result)

if __name__ =="__main__":
            main()
      







