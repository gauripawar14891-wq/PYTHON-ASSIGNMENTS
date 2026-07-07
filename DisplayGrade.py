def DisplayGrade(Marks):
    if Marks >= 75:
        print("Distinction")
    elif Marks >=60:
        print("First Class")
    elif (Marks <= 60) and (Marks >=30):
        print("Second Class")
    else:
        print("Fail")
    
    
def main():
    Value = int(input("Enter the marks: "))
    DisplayGrade(Value)




if __name__ =="__main__":
    main()