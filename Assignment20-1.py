import threading
def Even():
    print("First 10 even numbers: ")
    for i in range(2,21,2):
        print(i)
def Odd():
    print("First 20 odd numbers: ")
    for i in range(1,20,2):
        print(i)
def main():
    T1 =threading.Thread(target=Even,name = "Even")
    T2 =threading.Thread(target=Odd,name = "Odd")

    T1.start()
    T2.start()

    T1.join()
    T2.join()

if __name__ =="__main__":
    main()