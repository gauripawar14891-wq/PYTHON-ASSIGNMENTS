import time
def read_file(file_path):
    try:
        with open(file_path,"r") as file:

            content=file.read()
            if content=="":
                print("File is empty")
            else:
                print("\nFile Contents")
                print(content)
    except FileNotFoundError:
        print("Error:File does not exist")
    except PermissionError:
        print("Error:permission denied")
    except OSError:
        print("Error:File cannot be opened")
    except Exception as e:
        print("Error:",e)
def main():
    file_path=input("Enter text file path:")
    while True:
        read_file(file_path)
        time.sleep(60)

if __name__ =="__main__":
    main()


