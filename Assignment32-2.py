import os
import time
from datetime import datetime

def monitor_file(file_path):
    try:
        file_size=os.path.getsize(file_path)
        current_time=datetime.now()
        with open("FileSizeLog.txt","a") as log_file:
            log_file.write("File path:"+file_path+"\n")
            log_file.write("File size:"+str(file_size)+"bytes\n")
            log_file.write("Date and time:"+current_time.strftime("%d-%m-%Y %H:%M:%S")+"\n")

            log_file.write("--------------------------------\n")       
            print("File size recorded:",file_size,"bytes")          

    except FileNotFoundError:
     print("Error:File does not exist")
    except PermissionError:
       print("Error:Permission denied")
    except Exception as e:
       print("Error:",e)
def main():
   file_path=input("Enter file path:")
   while True:
      monitor_file(file_path)
      time.sleep(30)

if __name__ =="__main__":
   main()
       
                           
                           
                           
                           
                           
                           

                           