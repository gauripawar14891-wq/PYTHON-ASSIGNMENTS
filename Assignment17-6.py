







def Display(No):
    for i in range(No):
        for j in range(No -i):
            print("*",end = "\t")
        print()



def main():
 No =int(input("Enter the number: "))

 Display(No)




if __name__ =="__main__":
    main()
