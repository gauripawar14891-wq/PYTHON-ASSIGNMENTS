from multiprocessing import Pool
def CountPrime(N):
    Count = 0
    for i in range(2,N + 1):
        Flag = True
        for j in range(2,int(i **0.5)+ 1):
            if i % j ==0:
                Flag = False
                break

        if Flag:
            Count = Count + 1
    return Count
def main():
    Data = [10000,20000,30000,40000]
    p = Pool()
    Result =p.map(CountPrime,Data)
    p.close()
    p.join()
    for i in range(len(Data)):
        print("Prime count between 1 and ",Data[i],"=",Result[i])

if __name__ =="__main__":
    main()