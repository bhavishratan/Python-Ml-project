import tkinter.ttk
from tkinter import *
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox
def mydashboard():
    myroot_welcome=Toplevel()
    myroot_welcome.geometry('1100x700+200+10')
    myroot_welcome.title('welcome user..............')
    myroot_welcome.resizable(False,False)

    myimage_welcome_bk= Image.open("Images/01 covid.jpg")
    myimage_resize_welcome= myimage_welcome_bk.resize((1100,700), Image.Resampling.LANCZOS)
    get_image_welcome= ImageTk.PhotoImage(myimage_resize_welcome)
    my_root_label_ = Button(myroot_welcome, image=get_image_welcome,bd=0)
    my_root_label_.place(x=0,y=0)

    myroot_welcome.mainloop()