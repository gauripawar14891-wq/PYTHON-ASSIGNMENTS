class BookStore:
    NoOfBooks = 0 # class variable
    def __init__(self,Name,Author):  # constructor
        self.Name =Name
        self.Author = Author
        BookStore.NoOfBooks += 1
    def Display(self): #Instance method
        print(f"{self.Name} by {self.Author}. No of books:{BookStore.NoOfBooks}")
def main():
    Book1=BookStore("Linux System Programming","Robert Love")
    Book1.Display()
    Book2 = BookStore("C Programming","Dennis Ritchie")
    Book2.Display()

if __name__ =="__main__":
    main()
