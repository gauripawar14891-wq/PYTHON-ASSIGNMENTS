def CheckPrime(No):
    Count = 0
    for i in range(1,No + 1):
      if No % i == 0:
        Count=Count + 1
     
    if Count == 2:
       print("it is prime number")
    else:
       print("it is not a prime number")






def main():
    No =int(input("Enter the number"))
    CheckPrime(No)





if __name__ =="__main__":
    main()