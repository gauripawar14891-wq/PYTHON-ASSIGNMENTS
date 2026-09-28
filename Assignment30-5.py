import schedule
import time
from datetime import datetime

def write_datetime():
    current_time=datetime.now()
    with open("Marvellous.txt","a") as file:

    
     file.write("Task executed at: " + current_time.strftime("%d-%m-%Y %I:%M:%S%p") + "\n")
    file.close()






def main():
    schedule.every(5).seconds.do(write_datetime)
    while True:
        schedule.run_pending()
        time.sleep(1)








if __name__ =="__main__":
    main()