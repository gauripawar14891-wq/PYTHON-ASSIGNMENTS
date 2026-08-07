class BankAccount:
    ROI=10.5   #CLASS VARIABLE
    def __init__(self,Name,Amount):    #constructor
        self.Name =Name
        self.Amount =Amount
    def Display(self):   #Display account details
            print("Account Holder : ",self.Name)
            print("Curretnt Balance: ",self.Amount)

    def Deposit(self,Money):         #deposit amount
            self.Amount = self.Amount + Money
            print("Deposited",Money)
            print("Updated Balance:",self.Amount)
    def Withdraw(self,Money):  #withdraw amount
            if Money <=self.Amount:
                self.Amount = self.Amount - Money
                print("Withdraw: ",Money)
                print("Updated Balance:",self.Amount)
            else:
                print("Insufficient Balance")
    def CalculateInterest(self):
          Interest=(self.Amount * BankAccount.ROI) /100
def main():
      obj1 = BankAccount("Gauri",50000)
      obj1.Display()
      obj1.Deposit(10000)
      obj1.Withdraw(15000)
      Interest =obj1.CalculateInterest()
      print("Interest= ",Interest)

if __name__ =="__main__":
      main()
    


