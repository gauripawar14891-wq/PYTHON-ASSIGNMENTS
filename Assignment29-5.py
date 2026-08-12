def SearchWord(Name,Word):

    fobj=open(Name,"r")

    data=fobj.read()
    fobj.close()

    count=data.count(Word)


    print("Frequency of",Word,"is",count)


def main():

    Name=input("Enter name of file: ")
    Word=input("Enter the word to search: ")


    SearchWord(Name,Word)


if __name__ =="__main__":
    main()