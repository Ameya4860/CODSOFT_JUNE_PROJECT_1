# In this file im going to code for my todo list app with the help of tkinter
from tkinter import *
from tkinter.font import Font
from tkinter import filedialog
import pickle 
root = Tk()
root.title("TODO-LIST")
root.geometry("570x750+100+200")
root.resizable(False , False)
root.configure(bg = "black")


my_frame= Frame(root)
my_frame.pack(pady = 10)

my_list = Listbox(my_frame , font = ("arial" , 30) , width =25 , height =5 , bg = "#E7222E",bd = "0", fg ="black" , highlightthickness="0" , selectbackground="green" , activestyle="none")
my_list.pack(side = LEFT)

#Create a dummy list
stuff = []
for item in stuff:
    my_list.insert(END , item)
 #Create Scroll Bar
my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side = RIGHT , fill = BOTH)     
# Add scroll bar
my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command = my_list.yview)

#Create a entry box for adding items
my_entry = Entry(root , font = ("arial" , 24)) 
my_entry.pack(pady =20)

#buttons
button_frame = Frame(root)
button_frame.pack(pady = 20)

#function
def delete_item():
    my_list.delete(ANCHOR)
def add_item():
    my_list.insert(END , my_entry.get())
    my_entry.delete(0 , END)
def cross_item():
    my_list.itemconfig(
        my_list.curselection(),
        fg ="grey")
    my_list.selection_clear(0 , END)
    
def uncross_item():
    my_list.itemconfig(
        my_list.curselection(),
        fg = "black"
    )
    my_list.selection_clear(0 ,END)
def delete_crossed_item():
    print(my_list.size())
    count = 0
    while count < my_list.size():
        if my_list.itemcget(count , "fg") == "grey":
            my_list.delete(my_list.index(count))
        else:
            count+=1
def save_list():
    root = Tk()
    root.withdraw()  # Hide the main tkinter window

    file_name = filedialog.asksaveasfilename(
        initialdir="C:/Users/ameya/OneDrive/Documents/save file",
        title="Save File",
        filetypes=(("Dat Files", "*.dat"), ("All Files", "*.*"))
    )
    if file_name:
        if file_name.endswith(".dat"):
            pass
        else:
            file_name=f'{file_name}.dat'
    count = 0

# Delete crossed off items before saving
    while count < my_list.size():
        if my_list.itemcget(count , "fg") == "grey":
            my_list.delete(my_list.index(count))
        else:
            count+=1        
    stuff = my_list.get(0, END)
    output_file = open(file_name , 'wb') 
    pickle.dump(stuff , output_file)       
def open_list():
    file_name= filedialog.askopenfilename(
        initialdir="C:/Users/ameya/OneDrive/Documents/save file",
        title="Open File",
        filetypes=(("Dat Files", "*.dat"), ("All Files", "*.*"))
    )
    if file_name:
        my_list.delete(0,END)
        input_file = open(file_name , 'rb')
        stuff = pickle.load(input_file)
        for item in stuff:
            my_list.insert(END , item)


#create a menu
my_menu = Menu(root)
root.config(menu = my_menu)

file = Menu(my_menu ,tearoff = False)
my_menu.add_cascade(label = "File" , menu = file)

file.add_command(label = "Save List" , command =save_list)
file.add_command(label = "Open List" , command =open_list)

# create a button
delete_button = Button(button_frame , text = "Delete Item" , command = delete_item)
add_button = Button(button_frame , text = "Add Item" , command = add_item)
cross_button = Button(button_frame , text = "Cross Item" , command = cross_item)
uncross_button = Button(button_frame , text = "Uncross Item" , command = uncross_item)
delete_crossed_button = Button(button_frame , text = "Delete Crossed Item" , command = delete_crossed_item)

# Button function and position 
delete_button.grid(row = 0 , column = 0)
add_button.grid(row = 0 , column = 1 , padx =20)
cross_button.grid(row = 0 , column = 2)
uncross_button.grid(row = 0 , column = 3 , padx =20)
delete_crossed_button.grid(row = 0 , column = 4)
root.mainloop()