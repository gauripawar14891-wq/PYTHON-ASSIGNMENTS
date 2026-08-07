

def CountWords(FileName):
    fobj=open(FileName,"r")
    Count = 0
    for line in fobj:
        Words=line.split()
        Count=Count+len(Words)
    fobj.close()
    print("Total number of words:",Count)



def main():
    Name=input("Enter file name:")
    CountWords(Name)





if __name__ =="__main__":
    main()