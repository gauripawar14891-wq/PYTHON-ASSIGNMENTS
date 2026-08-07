from multiprocessing import Pool

def SumSquares(N):
    Sum = 0

    for i in range (1,N + 1):
        Sum = Sum + (i* i)

    return Sum

def main():
    Data =[1000000,2000000,3000000,4000000]

    p =Pool()
    Result = p.map(SumSquares,Data)

    p.close()
    p.join()

    print("Result : ")
    print(Result)

if __name__ =="__main__":
    main()
