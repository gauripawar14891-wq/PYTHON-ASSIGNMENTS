
import os
import schedule
import time
from datetime import datetime

def scan_directory(directory):
    if not os.path.isdir(directory):
       print("Directory does not exist")
       return
    files=0
    subdirectories=0

    for item in os.listdir(directory):
       path=os.path.join(directory,item)
       if os.path.isfile(path):
          files+=1
       elif os.path.isdir(path):
          subdirectories +=1

    current_time=datetime.now()
    print("\nDirectory Scanned:",directory)
    print("Total files:",files)
    print("Total Subdirectories:",subdirectories)
    print("Scan time:",current_time.strftime("%d-%m-%Y %I:%M:%S%p"))
def main():
       directory=input("Enter directory path:")
       scan_directory(directory)
       schedule.every(1).minute.do(scan_directory,directory)
while True:
       schedule.run_pending()
       time.sleep(1)


if __name__ =="__main__":
    main()