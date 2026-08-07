import threading
Sum = 0
Product = 1

def SumElements(Data):
    global Sum
    Sum =sum(Data)

def ProductElements(Data):
    global Product 
    for No in Data:
        Product *= No
def main():
    Data = list(map(int,input("Enter numbers: ").split()))
    T1 = threading.Thread(target=SumElements,args=(Data,))
    T2 = threading.Thread(target=ProductElements,args=(Data,))


    T1.start()
    T2.start()
    T1.join()
    T2.join()

    print("Sum is : ",Sum)
    print("Product is : ",Product)


if __name__ =="__main__":
    main()