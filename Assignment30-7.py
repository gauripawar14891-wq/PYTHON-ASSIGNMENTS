import shutil
import os
from datetime import datetime
def backup_folder():
    source_file=r"C:\Users\Umesh bhosale\Desktop\python asgnmnt\Demo.txt"
    backup_folder=r"C:\Users\Umesh bhosale\Desktop\PYTHON ASGNMNT\backup"
#create backup folder if it does not exist
if not os.path.exists(backup_folder):
    os.makedirs(backup_folder)
#create backup file name

current_time=datetime.now()

backup_file_name=("Demo_Backup_" + current_time.strftime("%d_%m_%Y_%H_%M_%S") + ".txt")

backup_path=os.path.join(backup_folder,backup_file_name)

#copy Demo.txt to backup folder

shutil.copy2(source_file,backup_path)

print("Backup completed successfully")
print("Backup file:",backup_path)






def main():
    backup_file()









if __name__ == "__main__":
    main()