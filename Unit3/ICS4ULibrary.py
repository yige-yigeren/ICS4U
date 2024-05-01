import time
import pygame as pg
# subclass of book
class Book: # Attributes: Title, Author, ISBN, Genre, Quantity
    # Methods: AddBook(), RemoveBook(), UpdateQuantity(), SearchBook()
    def __init__(self):
        self.books = [['TiTle'], ['Author'], ['ISBN'], ['Genre'], ['Quantity']]

    def AddBook(self, Title='', Author='', ISBN='', Genre='', Quantity=''):
        for i in range(len(self.books[0])):
            if ISBN == self.books[2][i]:
                self.books[4][i] += Quantity
            else:
                self.books[0].append(Title)
                self.books[1].append(Author)
                self.books[2].append(ISBN)
                self.books[3].append(Genre)
                self.books[4].append(Quantity)

    def RemoveBook(self, ISBN='', Quantity=''):
        for i in range(len(self.books[0])):
            if ISBN == self.books[2][i]:
                if Quantity > self.books[4][i]:
                    print(f'WARNING: Not enough books, action cancelled. {self.books[4][i]} books left.')
                    return False
                else:
                    self.books[4][i] -= Quantity
    
    def UpdateQuantity(self, ISBN, Quantity):
        for i in range(len(self.books[0])):
            if ISBN == self.books[2][i]:
                self.books[4][i] = Quantity

    def SearchBook(self, ISBN=''):
        for i in range(len(self.books[0])):
            if ISBN == self.books[2][i]:
                return self.books[0][i], self.books[1][i], self.books[2][i], self.books[3][i], self.books[4][i]
        print('ERROR: ISBN not found')
        return False
    
class Borrower: # Attributes: Name, ID, Address, Contact Info
    # Methods: Register(), UpdateInfo(), ViewBorrowedBooks()
    def __init__(self):
        self.Borrower = [['Name'], ['ID'], ['Address'], ['Contact Info']]
    
    def Register(self, Name, ID, Address, Contact_Info):
        if ID in self.Borrower[1] or Name in self.Borrower[0]:
            print('ERROR: ID already exists')
            return False
        else:
            self.Borrower[0].append(Name)
            self.Borrower[1].append(ID)
            self.Borrower[2].append(Address)
            self.Borrower[3].append(Contact_Info)
        
    def UpdateInfo(self, Name='', ID='', Address='', Contact_Info=''):
        if ID in self.Borrower[1]:
            for i in range(len(self.Borrower[0])):
                if ID == self.Borrower[1][i]:
                    if Name != '':
                        self.Borrower[0][i] = Name
                    if Address != '':
                        self.Borrower[2][i] = Address
                    if Contact_Info != '':
                        self.Borrower[3][i] = Contact_Info
        elif ID not in self.Borrower[1]:
            print('ERROR: ID not found')
            return False
        else:
            print('ERROR: ID is force required')
            return False
        
    def ViewBorrowedBooks(self, ID):
        Books = []
        for i in range(len(libraryTransaction.Transaction[0])):
            if ID == libraryTransaction.Transaction[0][i]:
                Books.append(libraryTransaction.Transaction[1][i])
        return Books
        

class Transaction: # Attributes: BorrowerID, BookISBN, BorrowDate, ReturnDate
    # IssueBook(), ReturnBook(), CalculateFine()
    def __init__(self):
        self.Transaction = [['BorrowerID'], ['BookISBN'], ['BorrowDate'], ['ReturnDate']]

    def IssueBook(self, BorrowerID, BookISBN, ReturnDate):
        bookinfo = libraryBook.SearchBook(BookISBN)
        if bookinfo == False:
            print('ERROR: Book not found')
            return False
        else:
            if bookinfo[4] == 0:
                print('ERROR: No more books left')
                return False
            else:
                libraryBook.RemoveBook(BookISBN, 1)
                self.Transaction[0].append(BorrowerID)
                self.Transaction[1].append(BookISBN)
                self.Transaction[2].append(time.strftime('%Y-%m-%d', time.localtime()))
                self.Transaction[3].append(ReturnDate)
                return True
    
    def ReturnBook(self, BorrowerID, BookISBN):
        for i in range(len(self.Transaction[0])):
            if BorrowerID == self.Transaction[0][i] and BookISBN == self.Transaction[1][i]:
                libraryBook.AddBook(ISBN=BookISBN, Quantity=1)
                self.Transaction[0].pop(i)
                self.Transaction[1].pop(i)
                self.Transaction[2].pop(i)
                self.Transaction[3].pop(i)
                return True

# 
libraryBook = Book()
libraryBorrower = Borrower()
libraryTransaction = Transaction()