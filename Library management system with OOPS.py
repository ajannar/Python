class Library:
    
    def __init__(self,listOfBooks):
        self.availableBooks = listOfBooks

    def displayAvailableBooks(self):
        print()
        print("Available books: ")
        for book in self.availableBooks:
            print(book)

    def addBook(self,returnedBook):
        print()
        if returnedBook in self.availableBooks:
            print("You can't return this book as you havn't borrowed any books")
        else:
            print("Thank you for returning the book")
            self.availableBooks.append(returnedBook)
        

    def removeBook(self,borrowedBook):
        print()
        if borrowedBook in self.availableBooks:
            print("You have borrowed a new book")
            self.availableBooks.remove(borrowedBook)
        else:
            print("This book is not available right now")
        

class Customer:
    def borrowBook(self):
        print()
        print("Enter book name to borrow: ")
        self.bookName=input()
        return self.bookName

    def returnBook(self):
        print()
        print("Enter book name to return: ")
        self.bookName=input()
        return self.bookName

library = Library(["Gita","Ramayana","Mahabharat"])
customer = Customer()

while(True):
    print()
    print("Press 1 to display available books")
    print("Press 2 to borrow book")
    print("Press 3 to return book")
    print("Press 4 to exit")
    print()

    optionChoice = int(input())

    if optionChoice == 1:
        library.displayAvailableBooks()

    if optionChoice == 2:
        borrowedBook = customer.borrowBook()
        library.removeBook(borrowedBook)

    if optionChoice == 3:
        returnedBook = customer.returnBook()
        library.addBook(returnedBook)

    if optionChoice == 4:
        quit()



