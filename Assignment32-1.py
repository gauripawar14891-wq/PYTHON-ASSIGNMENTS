import time
from datetime import datetime

def create_file():
    current_time=datetime.now()
    filename=current_time=datetime.now()

    filename=current_time.strftime("File_%d_%m_%Y_%H_%M%S.txt")
    with open(filename,"w") as file:file.write("Filename:"+filename +"\n")
    file.write("Creation time:"+current_time.strftime("%H:%M:%S")+"\n")
    print("File created:",filename)
def main():
        while True:
            create_file()
            time.sleep(60)

if __name__=="__main__":
    main()