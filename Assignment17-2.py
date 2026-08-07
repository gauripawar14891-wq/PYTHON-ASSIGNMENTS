def Display(No):
    for i in range(5):
        for j in range(No):
            print("*",end = "\t")
        print()


def main():
    No = int(input("Enter the number: "))
    Display(No)





if __name__ =="__main__":
    main()