from tkinter import *
import mysql.connector as msc

def res_fun(value,w):
    if value == 2:
        write_w = Toplevel(w)
        
        name_lbl = Label(write_w,text = 'Enter your name ===>').grid(row = 0, column = 0, padx = 10, pady = 10)
        global name_entry
        name_entry = Entry(write_w)
        
        lastName_lbl = Label(write_w,text = 'Enter your last name ===>').grid(row = 1, column = 0, padx = 10, pady = 10)
        lastName_entry = Entry(write_w)
        
        age_lbl = Label(write_w,text = 'Enter your age ===>').grid(row = 2, column = 0, padx = 10, pady = 10)
        global age_entry
        age_entry = Entry(write_w)
        
        name_entry.grid(row = 0, column = 1, padx = 10, pady = 10)
        lastName_entry.grid(row = 1, column = 1, padx = 10, pady = 10)
        age_entry.grid(row = 2, column = 1, padx = 10, pady = 10)
        
        writeSubmit_btn = Button(write_w,text = 'Submit',width = 20,height = 3,command = lambda: write_fun(lastName_entry.get()))
        
        writeSubmit_btn.grid(row = 3, column = 0, padx = 10, pady = 10)
        
    elif value == 1:
        read_w = Toplevel(w)
        nameRead_lbl = Label(read_w,text = 'Enter the name you want to search for ===>').grid(row = 0, column = 0, padx = 10, pady = 10)
        global nameRead_entry
        nameRead_entry = Entry(read_w)
        lastNameRead_lbl = Label(read_w,text = 'Enter the last name you want to search for ===>').grid(row = 1, column = 0, padx = 10, pady = 10)
        global lastNameRead_entry
        lastNameRead_entry = Entry(read_w)
        ageRead_lbl = Label(read_w,text = 'Enter the age you want to search for ===>').grid(row = 2, column = 0, padx = 10, pady = 10)
        global ageRead_entry
        ageRead_entry = Entry(read_w)
        
        readSubmit_btn = Button(read_w,text = 'Submit',width = 20,height = 3,command = lambda: read_fun(nameRead_entry.get())).grid(row = 3, column = 0, padx = 10, pady = 10)
        
        nameRead_entry.grid(row = 0, column = 1, padx = 10, pady = 10)
        lastNameRead_entry.grid(row = 1, column = 1, padx = 10, pady = 10)
        ageRead_entry.grid(row = 2, column = 1, padx = 10, pady = 10)

    
mydb = msc.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'readingfromsql'
    )

mycursor = mydb.cursor()

def write_fun(lastName):
    
    if name_entry.get() == '' or lastName_entry.get() == '' or age_entry.get() == '':
        
        messagebox.showerror('Error','You have left one or more of the areas blank')
        
    else:    
        sqlCommand = 'INSERT INTO writtenres (name,lastName,age) VALUES (%s,%s,%s)'
        values = (name_entry.get(),lastName,age_entry.get())
        
        mycursor.execute(sqlCommand,values)
        mydb.commit()
        
def read_fun(nameRead):
    mycursor.execute('SELECT * FROM writtenres')

    result = mycursor.fetchall()
    
    if nameRead == '' or lastNameRead_entry.get() == '' or ageRead_entry.get() == '':
        messagebox.showerror('Error','You have left one or more of the areas blank')
        
    elif result[0] == nameRead and result[1] == lastNameRead_entry.get() and result[2] == ageRead_entry.get():
        messagebox.showinfo('Result','This row exists')
    
    else:
        messagebox.showinfo('Result','This row does not exist')