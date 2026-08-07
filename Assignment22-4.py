from multiprocessing import Pool
import time
def SumPower5(N):
    Sum = 0
    for i in range(1,N + 1):
        Sum =Sum + (i **5)
    return Sum
def main():
    Data = [1000000,2000000,3000000,4000000]
    Start =time.time()
    p = Pool()
    Result =p.map(SumPower5,Data)
    p.close()
    p.join()
    End = time.time()
    print("Result :")
    print(Result)
    print("Execution Time : ",End - Start,"seconds")


if __name__ =="__main__":
    main()