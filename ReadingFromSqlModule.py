from tkinter import *

def res_fun(value,w):
    if value == 1:
        write_w = Toplevel(w)
        
        name_lbl = Label(write_w,text = 'Enter your name ===>').grid(row = 0, column = 0, padx = 10, pady = 10)
        name_entry = Entry(write_w)
        
        lastName_lbl = Label(write_w,text = 'Enter your last name ===>').grid(row = 1, column = 0, padx = 10, pady = 10)
        lastName_entry = Entry(write_w)
        
        age_lbl = Label(write_w,text = 'Enter your age ===>').grid(row = 2, column = 0, padx = 10, pady = 10)
        age_entry = Entry(write_w)
        
        name_entry.grid(row = 0, column = 1, padx = 10, pady = 10)
        lastName_entry.grid(row = 1, column = 1, padx = 10, pady = 10)
        age_entry.grid(row = 2, column = 1, padx = 10, pady = 10)
        
    elif value == 2:
        read_w = Toplevel(w)
        nameRead_lbl = Label(read_w,text = 'Enter the name you want to search for ===>').grid(row = 0, column = 0, padx = 10, pady = 10)
        nameRead_entry = Entry(read_w)
        lastNameRead_lbl = Label(read_w,text = 'Enter the last name you want to search for ===>').grid(row = 1, column = 0, padx = 10, pady = 10)
        lastName_entry = Entry(read_w)
        ageRead_lbl = Label(read_w,text = 'Enter the age you want to search for ===>').grid(row = 2, column = 0, padx = 10, pady = 10)
        ageRead_entry = Entry(read_w)
        
        nameRead_entry.grid(row = 0, column = 1, padx = 10, pady = 10)
        lastNameRead_entry.grid(row = 1, column = 1, padx = 10, pady = 10)
        ageRead_entry.grid(row = 2, column = 1, padx = 10, pady = 10)