




def CountLines(FileName):
    fobj=open(FileName,"r")
    count = 0
    for line in fobj:
        count=count+ 1
    fobj.close()
    print("Total number of lines:",count)




def main():
    Name=input("Enter file name:")
    CountLines(Name)





if __name__ =="__main__":
    main()