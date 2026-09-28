

import schedule
import time
from datetime import datetime

def create_log():
    current_time=datetime.now()
    filename=current_time.strftime("MarvellousLog_%d_%m_%Y_%H_%M_%S.txt")
    with open(filename,"w") as file:
       file.write("Log file created successfully\n")
       file.write(
           "Creation Time:"
           +
           current_time.strftime("%d-%m-%Y %I:%M:%S%p")
       )
       print("Log file created:",filename)
    
def main():
       
   schedule.every(10).minutes.do(create_log)
   print("Log creation scheduled every 10 minutes...")
while True:
             schedule.run_pending()
             time.sleep(1)


if __name__ =="__main__":
    main()