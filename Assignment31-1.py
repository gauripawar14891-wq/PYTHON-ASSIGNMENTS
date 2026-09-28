import schedule
import time

def display_message(message):
    print(message)














def main():

    message=input("Enter message")
    interval=int(input("Enter interval in seconds:"))
    schedule.every(interval).seconds.do(display_message,message)
    print(f"Message will be displayed every{interval}seconds.")
    while True:
     schedule.run_pending()
     time.sleep(1)









if __name__ =="__main__":
    main()