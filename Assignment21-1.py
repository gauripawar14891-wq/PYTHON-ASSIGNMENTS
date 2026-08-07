import threading
def CheckPrime(No):
    if No <=1:
        return False
    for i in range(2,No):
        if No % i ==0:
            return False
    return True
def Prime(Data):
    print("Prime numbers: ")
    for i in Data:
        if CheckPrime(i):
            print(i)

def NonPrime(Data):
    print("Non prime Numbers: ")
    for i in Data:
        if not CheckPrime(i):
            print(i)

def main():
    Data = list(map(int,input("Enter Numbers: ").split()))
    T1=threading.Thread(target=Prime,args=(Data,),name= "Prime")
    T2=threading.Thread(target=NonPrime,args=(Data,),name= "NonPrime")
    T1.start()
    T2.start()
    T1.join()
    T2.join()

if __name__ =="__main__":
    main()
    