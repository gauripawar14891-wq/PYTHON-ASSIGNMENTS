import threading
def Small(Str):
    Count = 0
    for ch in Str:
        if ch.islower():
            Count =Count + 1
    print("Small Letters : ",Count)
    print("Thread ID: ",threading.get_ident())
    print("Thread Name:",threading.current_thread().name)

def Capital(Str):
    Count=0
    for ch in Str:
        if ch.isupper():
            Count =Count + 1
    print("Capital Letters :",Count)
    print("Thread ID:",threading.get_ident())
    print("Thread Name:",threading.current_thread().name)
def Digits(Str):
    Count = 0
    for ch in Str:
        if ch.isdigit():
            Count =Count + 1
            print("Digits:",Count)
            print("Thread ID :",threading.get_ident())
            print("Thread Name:",threading.current_thread().name)
def main():
    Str =input("Enter String:")
    T1 =threading.Thread(target=Small,args=(Str,),name="Small")
    T2 =threading.Thread(target=Capital,args=(Str,),name="Capital")
    T3 =threading.Thread(target=Digits,args=(Str,),name="Digits")

    T1.start()
    T2.start()
    T3.start()

    T1.join()
    T2.join()
    T3.join()

if __name__ =="__main__":
    main()