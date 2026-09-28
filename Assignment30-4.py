import schedule
import time

def say_namaskar():
    print("Namaskar....")






def main():
    schedule.every().day.at("09:00").do(say_namaskar)

    while True:
        schedule.run_pending()
        time.sleep(1)




if __name__ =="__main__":
    main()