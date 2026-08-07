class Circle:
    PI= 3.14
    def __init__(self):
        self.Radius =0.0
        self.Area =0.0
        self.Circumference =0.0
    def Accept(self):
        self.Radius=float(input("Enter Radius:"))
    def CalculateArea(self):
            self.Area =Circle.PI * self.Radius * self.Radius
    def CalculateCircumference(self):
            self.Circumference =2 * Circle.PI *self.Radius
    def Display(self):
            print("Radius:",self.Radius)
            print("Area:",self.Area)
            print("Circumference:",self.Circumference)
print("----------------------------------------")

def main():
    No=int(input("Enter number of circles : "))

    for i in range(No):
        print("\nCircle",i + 1)
        obj = Circle()
        obj.Accept()
        obj.CalculateArea()
        obj.CalculateCircumference()
        obj.Display()

if __name__ =="__main__":
    main()