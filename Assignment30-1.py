import schedule
import time

def print_ganesh():
   print("Jay Ganesh....")


def main():
 schedule.every(2).seconds.do(print_ganesh)

 while True:
    schedule.run_pending()
    time.sleep(1)






if __name__ =="__main__":
    main()