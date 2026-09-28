
import os
import schedule
import time
from datetime import datetime

def scan_directory(directory):
    if not os.path.isdir(directory):
       print("Directory does not exist")
       return
    count=0
    

    for item in os.listdir(directory):
       full_path=os.path.join(directory,item)
       if os.path.isfile(full_path):
          count+=1
       

    current_time=datetime.now()
    with open("DirectoryCountLog.txt","a") as file:
        file.write("Directory path:"+directory +"\n")
        file.write("Number of files:",+str(count)+"\n")
        file.write("Date and time:" + current_time.strftime("%d-%m-%Y %I:%M:%S%p"))
        + "\n"
        file.write("-"*40+"\n")
        print("Directory:",directory)
        print("Number of files:",count)
        print("Date and time:",current_time.strftime("%d-%m-%Y %I:%M:%S%p"))


def main():
       directory=input("Enter directory path:")
       
       schedule.every(5).minute.do(count_files,directory)
       print("File counting scheduled every 5 minutes...")
while True:
       schedule.run_pending()
       time.sleep(1)


if __name__ =="__main__":
    main()