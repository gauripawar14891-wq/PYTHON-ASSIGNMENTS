import threading

def Maximum(Data):
   print("Maximum elelment is: ",max(Data))
def Minimum(Data):
   print("Minimum elelment is: ",min(Data))

def main():
    Data = list(map(int,input("Enter numbers : ").split()))
    T1 =threading.Thread(target=Maximum,args =(Data,))
    T2 = threading.Thread(target=Minimum,args=(Data,))
    T1.start()
    T2.start()
    T1.join()
    T2.join()

if __name__ =="__main__":
    main()