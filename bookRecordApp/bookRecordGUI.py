"""
This is just a simple GUI that stores information about books in a .db file
and communicates with the help of the sqlite3 module
"""

from tkinter import *
import backend

#Returns a tuple for selected book
def getSelectedRow(event):
    #Accounts for empty Listbox widget
    try:
        global selectedBookTuple
        index = list.curselection()[0]
        selectedBookTuple = list.get(index)
        titleLabel.delete(0,END)
        titleLabel.insert(END, selectedBookTuple[1])
        authorLabel.delete(0,END)
        authorLabel.insert(END, selectedBookTuple[2])
        yearLabel.delete(0,END)
        yearLabel.insert(END, selectedBookTuple[3])
        isbnLabel.delete(0,END)
        isbnLabel.insert(END, selectedBookTuple[4])
    except IndexError:
        pass

#View all books in Listbox widget
def viewBooks():
    rows = backend.view()
    list.delete(0,END)
    for row in rows:
        list.insert(END, row)

#Finds books with any of the user-inputted attributes
def searchBooks():
    list.delete(0, END)
    for row in backend.search(titleText.get(), authorText.get(), yearText.get(), isbnText.get()):
        list.insert(END, row)

#Adds book to the Database
def addBook():
    t = titleText.get()
    a = authorText.get()
    y = yearText.get()
    i = isbnText.get()
    if (t == "") or (a == "") or (y == "") or (i == ""):
        pass
    else:
        if not backend.search(t, a, y, i):
            backend.insert(t, a, y, i)
            viewBooks()
    viewBooks()

#Updates entries in Database
def updateEntry():
    #Accounts for empty Listbox widget
    try:
        backend.update(selectedBookTuple[0], titleText.get(), authorText.get(), yearText.get(), isbnText.get())
        viewBooks()
    except NameError:
        pass

#Deletes entries from Database
def deleteEntry():
    #Accounts for empty Listbox widget
    try:
        backend.delete(selectedBookTuple[0])
        viewBooks()
    except NameError:
        pass

#Open window
window = Tk()
window.title('Book Database')

#Create Label widgets within window
title = Label(window, text='Title')
title.grid(row=0, column=0)
author = Label(window, text='Author')
author.grid(row=0, column=2)
year = Label(window, text='Year')
year.grid(row=1, column=0)
isbn = Label(window, text='ISBN')
isbn.grid(row=1, column=2)

#Create Entry widgets
titleText = StringVar()
titleLabel = Entry(window, textvariable=titleText)
titleLabel.grid(row=0, column=1)
authorText = StringVar()
authorLabel = Entry(window, textvariable=authorText)
authorLabel.grid(row=0, column=3)
yearText = StringVar()
yearLabel = Entry(window, textvariable=yearText)
yearLabel.grid(row=1, column=1)
isbnText = StringVar()
isbnLabel = Entry(window, textvariable=isbnText)
isbnLabel.grid(row=1, column=3)

#Create Listbox for book entry display
list = Listbox(window, height=6, width=35)
list.grid(row=2, column=0, rowspan=6, columnspan=2)
list.configure(background='grey')

#Bind Listbox event to function
list.bind('<<ListboxSelect>>', getSelectedRow)

#Create Scrollbar for interaction with the Listbox
scroll = Scrollbar(window)
scroll.grid(row=2, column=2, rowspan=6)
list.configure(yscrollcommand=scroll.set)
scroll.configure(command=list.yview)

#Create Buttons for interaction with Listbox
view = Button(window,text='View All', width=12, command=viewBooks)
view.grid(row=3, column=3)
search = Button(window,text='Search Entry', width=12, command=searchBooks)
search.grid(row=4, column=3)
add = Button(window,text='Add Entry', width=12, command=addBook)
add.grid(row=5, column=3)
update = Button(window,text='Update', width=12, command=updateEntry)
update.grid(row=6, column=3)
delete = Button(window,text='Delete', width=12, command=deleteEntry)
delete.grid(row=7, column=3)
close = Button(window,text='Close', width=12, command=window.destroy)
close.grid(row=8, column=3)

window.mainloop()
