

def DisplayFile(FileName):
    fobj=open(FileName,"r")
    
    for line in fobj:
        print(line,end =" ")
    fobj.close()
    



def main():
    Name=input("Enter file name:")
    DisplayFile(Name)





if __name__ =="__main__":
    main()