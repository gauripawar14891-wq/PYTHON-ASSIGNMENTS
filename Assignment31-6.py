import schedule
import time


def show_message(message):
    print(message)

def main():
    schedule.every().monday.at("09:00").do(show_message,"start your weekly goals")
    schedule.every().wednesday.at("17:00").do(show_message,"review your weekly progress")
    schedule.every().friday.at("18:00").do(show_message,"weekly work completed")
    print("Weekly messages scheduled....")
    while True:
        schedule.run_pending()
        time.sleep()

if __name__ =="__main__":
    main()
        
        