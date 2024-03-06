from tkinter import *
from PIL import Image,ImageTk
from newuser import New_user_page1
import mysql.connector
from tkinter import messagebox
from Welcome import mydashboard
myroot=Tk()

myroot.geometry('1100x700+250+10')
myroot.title("The Covid Application ")
myroot.resizable(False,False)

user_email=Label(myroot,text='Email-id',font='rockwell 27 bold',fg='red')
user_email.place(x=100,y=300)

user_email_entry=Entry(myroot,font='italic 27 bold',bd=0)
user_email_entry.place(x=270,y=300)
user_email_entry.focus()