import threading
def Display1():
    print("Thread1 Started")
    for i in range(1,51):
        print(i)
    print("Thread1 completed")
def Display2():
    print("Thread2 Started")
    for i in range(50,0,-1):
        print(i)
    print("Thread2 completed")

def main():
    Thread1 = threading.Thread(target=Display1,name="Thread1")
    Thread2 = threading.Thread(target=Display2,name="Thread2")
    Thread1.start()
    Thread1.join()
    Thread2.start()
    Thread2.join()

    print("Exit from main")

if __name__ =="__main__":
    main()