import time
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Function to show message box
def show_popup(title='Notice', context='Error Message'):
    messagebox.showinfo(title, context)

# subclass of book
class Book: # Attributes: Title, Author, ISBN, Genre, Quantity
    # Methods: AddBook(), RemoveBook(), UpdateQuantity(), SearchBook()
    def __init__(self):
        self.books = [['TiTle'], ['Author'], ['ISBN'], ['Genre'], ['Quantity']]

    def AddBook(self):
        for i in range(len(self.books[0])):
            if BookGUIData[0] == self.books[2][i]:
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

    def IssueBook(self, BorrowerID, BookISBN):
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
                self.Transaction[2].append(time.time())
                return True
    
    def ReturnBook(self, BorrowerID, BookISBN):
        for i in range(len(self.Transaction[0])):
            if BorrowerID == self.Transaction[0][i] and BookISBN == self.Transaction[1][i]:
                libraryBook.AddBook(ISBN=BookISBN, Quantity=1)
                self.Transaction[3].append(time.time())
                # per hour 5 dollars
                cost = (self.Transaction[3][i] - self.Transaction[2][i]) * 5
                return cost
        print('ERROR: Action Not Found')
        return False

def update_data_from_gui():
    BookGUIData[:] = [entry.get() for entry in book_entries]
    BorrowerGUIData[:] = [entry.get() for entry in borrower_entries]

# Function to update the GUI from the data lists
def update_gui_from_data():
    for entry, data in zip(book_entries, BookGUIData):
        entry.delete(0, tk.END)
        entry.insert(0, data)
    for entry, data in zip(borrower_entries, BorrowerGUIData):
        entry.delete(0, tk.END)
        entry.insert(0, data)

libraryBook = Book()
libraryBorrower = Borrower()
libraryTransaction = Transaction()
BookGUIData = ['', '', '', '', '']
BorrowerGUIData = ['', '', '', '']


# Main Menu
root = tk.Tk()
root.title("Library Manage System")
root.geometry("900x750") 

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Create labels and entries for book
book_labels = ['Title', 'Author', 'ISBN', 'Genre', 'Quantity']
book_entries = [tk.StringVar() for _ in book_labels]

# Use LabelFrame for book frame
book_frame = ttk.LabelFrame(frame, text="Book")
book_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), padx=10, pady=10)

# Function to validate if input is digit
def is_digit(s):
    return s.isdigit()

validate_command = root.register(is_digit)

for i, (label, entry) in enumerate(zip(book_labels, book_entries)):
    ttk.Label(book_frame, text=label).grid(row=0, column=i, padx=10, pady=10)
    if label in ['ISBN', 'Quantity']:
        ttk.Entry(book_frame, textvariable=entry, validate='key', validatecommand=(validate_command, '%P')).grid(row=1, column=i, padx=10, pady=10)
    else:
        ttk.Entry(book_frame, textvariable=entry).grid(row=1, column=i, padx=10, pady=10)

# Create labels and entries for borrower
borrower_labels = ['Name', 'ID', 'Address', 'Contact Info']
borrower_entries = [tk.StringVar() for _ in borrower_labels]

# Use LabelFrame for borrower frame
borrower_frame = ttk.LabelFrame(frame, text="Borrower")
borrower_frame.grid(row=1, column=0, sticky=(tk.W, tk.E), padx=10, pady=10)

for i, (label, entry) in enumerate(zip(borrower_labels, borrower_entries)):
    ttk.Label(borrower_frame, text=label).grid(row=0, column=i, padx=10, pady=10)
    if label == 'ID':
        ttk.Entry(borrower_frame, textvariable=entry, validate='key', validatecommand=(validate_command, '%P')).grid(row=1, column=i, padx=10, pady=10)
    elif label in ['Address', 'Contact Info']:
        ttk.Entry(borrower_frame, textvariable=entry, width=32).grid(row=1, column=i, padx=10, pady=10)
    else:
        ttk.Entry(borrower_frame, textvariable=entry).grid(row=1, column=i, padx=10, pady=10)

# Create LabelFrame and buttons for book actions
book_actions = ['AddBook', 'RemoveBook', 'UpdateQuantity', 'SearchBook']
book_action_frame = ttk.LabelFrame(frame, text="Book Actions")
book_action_frame.grid(row=2, column=0, sticky=(tk.W, tk.E), padx=10, pady=10)
for i, action in enumerate(book_actions):
    ttk.Button(book_action_frame, text=action, command=lambda action=action: (update_data_from_gui(), getattr(libraryBook, action)(*[entry.get() for entry in book_entries])), width=20).grid(row=0, column=i, padx=10, pady=10)

# Create LabelFrame and buttons for borrower actions
borrower_actions = ['Register', 'UpdateInfo', 'ViewBorrowedBooks']
borrower_action_frame = ttk.LabelFrame(frame, text="Borrower Actions")
borrower_action_frame.grid(row=3, column=0, sticky=(tk.W, tk.E), padx=10, pady=10)
for i, action in enumerate(borrower_actions):
    ttk.Button(borrower_action_frame, text=action, command=lambda action=action: (update_data_from_gui(), getattr(libraryTransaction, action)(*[entry.get() for entry in book_entries+borrower_entries])), width=20).grid(row=0, column=i, padx=10, pady=10)

# Create LabelFrame and buttons for transaction actions
transaction_actions = ['IssueBook', 'ReturnBook', 'CalculateFine']
transaction_action_frame = ttk.LabelFrame(frame, text="Transaction Actions")
transaction_action_frame.grid(row=4, column=0, sticky=(tk.W, tk.E), padx=10, pady=10)
for i, action in enumerate(transaction_actions):
    ttk.Button(transaction_action_frame, text=action, command=lambda action=action: getattr(libraryTransaction, action)(*[entry.get() for entry in book_entries+borrower_entries]), width=20).grid(row=0, column=i, padx=10, pady=10)

root.mainloop()




