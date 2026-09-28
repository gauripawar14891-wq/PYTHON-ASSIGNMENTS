import schedule
import time
from datetime import datetime

def show_datetime():
    current_time=datetime.now()
    print("Current Date and Time:",current_time.strftime("%d-%m-%Y %I:%M:%S%p"))

def main():
    schedule.every(1).minutes.do(show_datetime)
    while True:
        schedule.run_pending()
        time.sleep(1)






if __name__ =="__main__":
    main()
