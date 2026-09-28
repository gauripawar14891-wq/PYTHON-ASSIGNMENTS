import schedule
import time
def lunch_time():
    print("Lunch_time!")

def wrap_up_work():
    print("Wrapup work")






def main():
    schedule.every().day.at("13:00").do(lunch_time)
    schedule.every().day.at("18:00").do(wrap_up_work)

    while True:
        schedule.run_pending()
        time.sleep(1)







if __name__ =="__main__":
    main()