import os
import shutil


import time
from datetime import datetime

def copy_files(source,destination):
    if not os.path.isdir(source):
        print("Error:Source directory does not exist")
        return
    if not os.path.isdir(destination):
        print("Error:Destination directory does not exist")
        return
    files=os.listdir(source)
    for filename in files:
        if filename.lower().endswith(".txt"):
            source_file=os.path.join(source,filename)
            destination_file=os.path.join(destination,filename)
            try:
                shutil.copy2(source_file,destination_file)
                with open("CopyLog.txt","a")as log_file:
                    log_file.write(
                        datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                        +"-copied:"
                        +filename
                        +"\n"
                    )
                print("Copied:",filename)
            except Exception as e:
             print("Could not copy",filename,";",e)
def main():
    source=input("Enter source directory path:")
    destination=input("Enter destination directory path:")
    while True:
        copy_files(source,destination)
        print("Waiting for 10 minutes...")
        time.sleep(600)
if __name__ =="__main__":
    main()