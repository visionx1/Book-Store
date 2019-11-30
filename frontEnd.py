from tkinter import *
import backEnd
import time


def get_selected_row(event):
	global selected_tuple
	index = list1.curselection()[0]
	selected_tuple = list1.get(index)
	e1.delete(0, END)
	e1.insert(END,selected_tuple[1])
	e2.delete(0,END)
	e2.insert(END,selected_tuple[2])
	e3.delete(0,END)
	e3.insert(END,selected_tuple[3])
	e4.delete(0,END)
	e4.insert(END,selected_tuple[4])


def view_command():
	list1.delete(0, END)
	for row in backEnd.view():
		list1.insert(END, row)

def search_command():
    list1.delete(0 , END)
    for row in backEnd.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list1.insert(END, row)


def add_command():
	backEnd.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
	list1.delete(0,END)
	list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))
	time.sleep(1)
	view_command()

def update_command():
	backEnd.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
	view_command()


def delete_command():
	backEnd.delete(selected_tuple[0])
	view_command()

window = Tk()
window.title('Book Shop')
window.resizable(0,0)
window.configure(background='#edeef5')
# window.iconbitmap(r'book.png')


font1 = (
    'verdana',
    10
)

font2 = (
	"verdana",
	8
)

l1 = Label(window, text = 'Book Title', font = ('verdana', 12), fg = "#2d0aa1", bg = '#edeef5')
l1.grid(row = 0, column = 0)

l2 = Label(window, text = 'Author', font = ('verdana', 12), fg = "#2d0aa1", bg = '#edeef5')
l2.grid(row = 0, column = 2)

l3 = Label(window, text = 'Year Publshed', font = ('verdana', 12), fg = "#2d0aa1", bg = '#edeef5')
l3.grid(row = 1, column = 0)

l4 = Label(window, text = 'ISBN', font = ('verdana', 12), fg = "#2d0aa1", bg = '#edeef5')
l4.grid(row = 1, column = 2)

title_text = StringVar()
e1 = Entry(window, textvariable = title_text, width = 40, selectbackground = "blue", bg = '#dfe3e6',font = font1, fg = 'blue')
e1.grid(row = 0, column = 1)

author_text = StringVar()
e2 = Entry(window, textvariable = author_text, width = 30, selectbackground = "blue", bg = '#dfe3e6', font = font2, fg = 'blue')
e2.grid(row = 0, column = 3)

year_text = StringVar()
e3 = Entry(window, textvariable = year_text, width = 40, selectbackground = "blue", bg = '#dfe3e6', font = font1, fg = 'blue')
e3.grid(row = 1, column = 1)

isbn_text = StringVar()
e4 = Entry(window, textvariable = isbn_text, width = 30, selectbackground = "blue", bg = '#dfe3e6', font = font2, fg = 'blue')
e4.grid(row = 1, column = 3)

list1 = Listbox(window, height = 20, width = 60, bd = 4, highlightcolor = 'gray', selectbackground = 'gray', border = 4, font = ('verdana', 9), relief = 'sunken', highlightthickness = 3, fg = "blue", bg = '#edefff')
list1.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)

sb1 = Scrollbar(window, orient = VERTICAL, width = 24, activebackground = '#2a273d')
sb1.grid(row = 2, column = 2, rowspan = 6)

list1.configure(yscrollcommand = sb1.set)
sb1.configure(command = list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

b1 = Button(window, text = 'view all', width = 12, command = view_command, bg = '#33b2f2', fg = 'black', activebackground = 'white', relief = 'raised', font =('verdana', 10) )
b1.grid(row = 2, column = 3)

b2 = Button(window, text = 'Search entry', width = 12, command = search_command, bg = '#33b2f2', fg = 'black', activebackground = 'white', relief = 'raised', font =('verdana', 10) )
b2.grid(row = 3, column = 3)

b3 = Button(window, text = 'Add entry', width = 12, command = add_command, bg = '#33b2f2', fg = 'black', activebackground = 'white', relief = 'raised', font =('verdana', 10) )
b3.grid(row = 4, column = 3)

b4 = Button(window, text = 'update', width = 12, command = update_command, bg = '#33b2f2', fg = 'black', activebackground = 'white', relief = 'raised', font =('verdana', 10) )
b4.grid(row = 5, column = 3)

b5 = Button(window, text = 'Delete', width = 12, command = delete_command, bg = '#33b2f2', fg = 'black', activebackground = 'white', relief = 'raised', font =('verdana', 10) )
b5.grid(row = 6, column = 3)

b6 = Button(window, text = 'Close', width = 12, command = backEnd.exit, bg = 'red', fg = 'black', activebackground = 'white', relief = 'raised', font =('verdana', 10) )
b6.grid(row = 7, column = 3)

window.mainloop()