import time
import tkinter as tk
from tkinter import messagebox


# subclass of book
class Book: # Attributes: Title, Author, ISBN, Genre, Quantity
    # Methods: AddBook(), RemoveBook(), UpdateQuantity(), SearchBook()
    def __init__(self):
        self.books = [['TiTle'], ['Author'], ['ISBN'], ['Genre'], ['Quantity']]

    def AddBook(self, GUIData, Notify=False):
        for i in range(len(self.books[0])):
            if GUIData[0][2] == self.books[2][i]:
                self.books[4][i] += GUIData[0][4]
                if Notify:
                    post_notice('Notice', 'Book added successfully')
                GUIData[0][4] = self.books[4][i] # update
                sync_list_to_gui()
                return True
        self.books[0].append(GUIData[0][0])
        self.books[1].append(GUIData[0][1])
        self.books[2].append(GUIData[0][2])
        self.books[3].append(GUIData[0][3])
        self.books[4].append(GUIData[0][4])
        if Notify:
            post_notice('Notice', 'New Book added successfully')
        return True

    def RemoveBook(self, GUIData, Notify=False):
        for i in range(len(self.books[0])):
            if GUIData[0][2] == self.books[2][i]:
                if GUIData[0][4] > self.books[4][i]:
                    if Notify:
                        post_notice('Notice', 'Not enough books to remove')
                    return False
                else:
                    self.books[4][i] -= GUIData[0][4]
                    if Notify:
                        post_notice('Notice', 'Book removed successfully')
                    GUIData[0][4] = self.books[4][i] # update
                    sync_list_to_gui()
                    return True
    
    def UpdateQuantity(self, GUIData, Notify=False):
        for i in range(len(self.books[0])):
            if GUIData[0][2] == self.books[2][i]:
                self.books[4][i] = GUIData[0][4]
                if Notify:
                    post_notice('Notice', 'Quantity updated successfully')
                return True

    def SearchBook(self, GUIData):
        for i in range(len(self.books[0])):
            if GUIData[0][2] == self.books[2][i]:
                GUIData[0][0] = self.books[0][i]
                GUIData[0][1] = self.books[1][i]
                GUIData[0][2] = self.books[2][i]
                GUIData[0][3] = self.books[3][i]
                GUIData[0][4] = self.books[4][i]
                return True
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
                self.Transaction[2].append(time())
                return True
    
    def ReturnBook(self, BorrowerID, BookISBN):
        for i in range(len(self.Transaction[0])):
            if BorrowerID == self.Transaction[0][i] and BookISBN == self.Transaction[1][i]:
                libraryBook.AddBook(ISBN=BookISBN, Quantity=1)
                self.Transaction[3].append(time())
                # per hour 5 
                fine = 5 * (self.Transaction[3][i] - self.Transaction[2][i])
                if fine > 120:
                    fine = 120
                return fine

libraryBook = Book()
libraryBorrower = Borrower()
libraryTransaction = Transaction()

# GUI
root = tk.Tk()
root.title("Library Management System")

# GUI Data
GUIData = [['N/A','N/A',0,'N/A',0], ['N/A',0,'N/A','N/A','']]

def sync_gui_to_list():
    GUIData[0][0] = book_entry_dict['Title'].get()
    GUIData[0][1] = book_entry_dict['Author'].get()
    GUIData[0][2] = book_entry_dict['ISBN'].get()
    GUIData[0][3] = book_entry_dict['Genre'].get()
    GUIData[0][4] = book_entry_dict['Quantity'].get()
    GUIData[1][0] = borrower_entry_dict['Name'].get()
    GUIData[1][1] = borrower_entry_dict['ID'].get()
    GUIData[1][2] = borrower_entry_dict['Address'].get()
    GUIData[1][3] = borrower_entry_dict['Contact Info'].get()
    GUIData[1][4] = ''

def sync_list_to_gui():
    for i, entry in enumerate(book_entry_dict.values()):
        entry.delete(0, tk.END)
        entry.insert(0, GUIData[0][i])
    for i, entry in enumerate(borrower_entry_dict.values()):
        entry.delete(0, tk.END)
        entry.insert(0, GUIData[1][i])

def post_notice(title = 'Notice', text = 'Error'):
    messagebox.showinfo(title, text)

def is_digit(s):
    if s.isdigit():
        return True
    else:
        return False

# Book Frame
book_frame = tk.LabelFrame(root, text="Book", padx=5, pady=5)
book_frame.pack(padx=10, pady=10)
book_attributes = ['Title', 'Author', 'ISBN', 'Genre', 'Quantity']
book_entry_dict = {}
for attribute in book_attributes:
    label = tk.Label(book_frame, text=attribute)
    label.pack(side="left")
    if attribute in ['ISBN', 'Quantity']:
        validate_command = root.register(is_digit)
        entry = tk.Entry(book_frame, validate="key", validatecommand=(validate_command, '%P'))
    else:
        entry = tk.Entry(book_frame)
    entry.pack(side="left")
    book_entry_dict[attribute] = entry

# Borrower Frame
borrower_frame = tk.LabelFrame(root, text="Borrower", padx=5, pady=5)
borrower_frame.pack(padx=10, pady=10)
borrower_attributes = ['Name', 'ID', 'Address', 'Contact Info']
borrower_entry_dict = {}
for attribute in borrower_attributes:
    label = tk.Label(borrower_frame, text=attribute)
    label.pack(side="left")
    if attribute == 'ID':
        validate_command = root.register(is_digit)
        entry = tk.Entry(borrower_frame, validate="key", validatecommand=(validate_command, '%P'))
    elif attribute in ['Address', 'Contact Info']:
        entry = tk.Entry(borrower_frame, width=31)
    else:
        entry = tk.Entry(borrower_frame)
    entry.pack(side="left")
    borrower_entry_dict[attribute] = entry

# Book Button
book_operations_frame = tk.LabelFrame(root, text="Book Operations", padx=5, pady=5)
book_operations_frame.pack(padx=10, pady=10)

add_book_button = tk.Button(book_operations_frame, text="Add Book", command=lambda: (sync_gui_to_list(), libraryBook.AddBook(GUIData, True)))
remove_book_button = tk.Button(book_operations_frame, text="Remove Book", command=lambda: (sync_gui_to_list(), libraryBook.RemoveBook(GUIData, True)))
update_quantity_button = tk.Button(book_operations_frame, text="Update Quantity", command=lambda: (sync_gui_to_list(), libraryBook.UpdateQuantity(GUIData, True)))
search_book_button = tk.Button(book_operations_frame, text="Search Book", command=lambda: (sync_gui_to_list(), libraryBook.SearchBook(GUIData)))
add_book_button.pack(side="left")
remove_book_button.pack(side="left")
update_quantity_button.pack(side="left")
search_book_button.pack(side="left")

root.mainloop()