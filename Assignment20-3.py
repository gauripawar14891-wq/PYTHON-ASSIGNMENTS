import threading
def EvenList(Data):
    Sum = 0
    print("Even Elements: ")
    for i in Data:
        if i % 2 ==0:
            print(i)
            Sum =Sum + i
    print("Sum of Even elelments=:",Sum)
def OddList(Data):
    Sum =0
    print("Odd Elements:")
    for i in Data:
        if i % 2 !=0:
            print(i)
            Sum =Sum + i
    print("Sum of Odd Elements =",Sum)

def main():
    Data=list(map(int,input("Enter numbers: ").split()))
    T1=threading.Thread(target=EvenList,args=(Data,),name="EvenList")
    T2=threading.Thread(target=OddList,args=(Data,),name="OddList")
    T1.start()
    T2.start()
    T1.join()
    T2.join()
if __name__ =="__main__":
    main()