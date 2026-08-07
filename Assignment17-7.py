







def Display(No):
    for i in range(No):
        for j in range(1,No + 1):
            print(j,end= "\t")
        print()



def main():
 No =int(input("Enter the number: "))

 Display(No)




if __name__ =="__main__":
    main()
