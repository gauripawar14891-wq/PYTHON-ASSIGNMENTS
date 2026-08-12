import sys
def main():
    file1=open(sys.argv[1],"r")
    data1=file1.read()
    file1.close()


    file2=open(sys.argv[2],"r")
    data2=file2.read()
    file2.close()

    if data1==data2:
        print("Success")
    else:
        print("Failure")

if __name__ =="__main__":
    main()