import tkinter.ttk
from tkinter import *
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox
def New_user_page1():
    myroot_signup=Toplevel()
    myroot_signup.geometry('1100x700+200+10')
    myroot_signup.title('New user registration')
    myroot_signup.resizable(False,False)

    myimage3= Image.open("Images/corona dead.jpg")
    myimage_resize3= myimage3.resize((1080,720), Image.Resampling.LANCZOS)
    get_image3= ImageTk.PhotoImage(myimage_resize3)
    my_root_label3 = Button(myroot_signup, image=get_image3,bd=0)
    my_root_label3.place(x=0,y=0)

    label_reg_tittle = Label(myroot_signup,text="Registration",bg='black',fg='white',font='rockwell 29 bold')
    label_reg_tittle.place(x=430,y=30)

    obj_frame=Frame(myroot_signup,bg='sky blue')
    obj_frame.place(x=290,y=100,width=500,height=560)
    #---------------------name code -----------------------------------------------


    name=Label(obj_frame,text="Name",fg='white',bg='blue',font='rockwell 25 bold')
    name.place(x=30,y=10)

    name_entry=Entry(obj_frame,fg='blue',font='rockwell 29 bold')
    name_entry.focus()
    name_entry.place(x=140,y=10,width=230,height=50)

#--------------------------------email code-------------------------------------------

    email=Label(obj_frame,text="Email",fg='white',bg="blue",font='rockwell 25 bold ')
    email.place(x=30,y=100)

    email_entry=Entry(obj_frame,fg='blue',font='rockwell 29 bold')
    email_entry.place(x=140,y=100,width=230,height=50)

#-----------------------------------password code---------------------------------------

    password=Label(obj_frame,text="Pass",fg='white',bg='blue',font='rockwell 29 bold')
    password.place(x=30,y=200)

    password_entry=Entry(obj_frame,show='$',fg='blue',bg='white',font='rockwell 25 bold')
    password_entry.place(x=140,y=200,width=230,height=50)

#-------------------------------------name code-------------------------------------------

    number=Label(obj_frame,text="Number",fg='white',bg="blue",font='rockwell 20 bold ')
    number.place(x=20,y=300)

    number_entry=Entry(obj_frame,fg='blue',font='rockwell 22 bold')
    number_entry.place(x=140,y=300,width=230,height=50)


#-------------------------------------gender code-----------------------------------------

    gender=Label(obj_frame,text='Gender',fg='white',bg='blue',font='rockwell 20 bold')
    gender.place(x=20,y=370)

    n=StringVar()

    Gender_choose=tkinter.ttk.Combobox(obj_frame,width=100,height=130,textvariable=n)
    Gender_choose['values']=('Select your Gender',"Male","Female","others")
    Gender_choose.current(0)
    Gender_choose.place(x=150,y=370,width=150,height=40)

    #_____________________________________mysql code---------------------------------------
    def signup_save():
        name = name_entry.get()
        email = email_entry.get()
        password = password_entry.get()
        number = number_entry.get()
        gender = Gender_choose.get()
        mydb=mysql.connector.connect(
            host="Localhost",
            user="root",
            password="",
            database="Covid"
        )
        mycursor=mydb.cursor()
        q="insert into user(name,email,password,number,gender)values('"+name+"','"+email+"','"+password+"','"+number+"','"+gender+"')"
        mycursor.execute(q)
        mydb.commit()
        messagebox.showinfo("signup status","New user Added successfully")

    # ---------------------------------data bases-----------------------------------------


    #----------------------------------------save image------------------------------------------

    myimage2 = Image.open("Images/save 1.png")
    myimage_resize2 = myimage2.resize((120,55), Image.Resampling.LANCZOS)
    get_image2 = ImageTk.PhotoImage(myimage_resize2)
    my_root_label2 = Button(myroot_signup,image=get_image2, bd=0,cursor='hand2',command=signup_save)
    my_root_label2.place(x=450,y=530)


    myroot_signup.mainloop()
