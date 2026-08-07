class Demo:
    Value =100
    def __init__(self,no1,no2):
        self.no1=no1
        self.no2=no2
    def Fun(self):
        print("Inside Fun()")
        print("No1=",self.no1)
        print("No2=",self.no2)
    def Gun(self):
        print("Inside Gun()")
        print("No1 =",self.no1)
        print("No2=",self.no2)

def main():
        obj1=Demo(11,21)
        obj2 =Demo(51,101)
        obj1.Fun()
        obj2.Fun()
        obj1.Gun()
        obj2.Gun()
if __name__ =="__main__":
         main()

















if __name__ =="__main__":
    main()