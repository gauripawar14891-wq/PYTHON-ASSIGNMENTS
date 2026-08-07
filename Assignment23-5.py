from multiprocessing import Pool
import os
def Factorial (No):
    Fact = 1
    for i in range(1,No +1):
        Fact = Fact * i
    print("Process ID : ",os.getpid())
    print("Input number :",No)
    print("Factorial : ",Fact)
    print("-------------")
    return Fact
def main():
    Data =[10,15,20,25]
    p=Pool()
    Result = p.map(Factorial,Data)
    p.close()
    p.join()
if __name__ =="__main__":
    main()
