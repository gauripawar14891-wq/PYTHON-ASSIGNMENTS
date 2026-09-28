import schedule
import time


def coding_kar():
    print("coding kar...!")






def main():
    schedule.every(3).minutes.do(coding_kar)

    while True:
        schedule.run_pending()
        time.sleep(1)







if __name__ =="__main__":
    main()