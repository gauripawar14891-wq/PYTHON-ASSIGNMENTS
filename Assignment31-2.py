import schedule
import time

def display_message(message):
    print(message)














def main():

    message=input("Enter message")
    
    schedule.every(5).seconds.do(display_message,message)
    print(f"Message will be displayed every 5 seconds.")
    while True:
     schedule.run_pending()
     time.sleep(1)









if __name__ =="__main__":
    main()