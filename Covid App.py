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

myimage=Image.open("Images/covid 19.jpg")
myimage_resize=myimage.resize((1100,700), not Image.Resampling.LANCZOS)
get_image=ImageTk.PhotoImage(myimage_resize)
my_root_label=Label(myroot,image=get_image,bd=0)
my_root_label.place(x=0,y=0)



#user_email=Label(myroot,text="Email-id",font="lucida 30 bold",fg="blue")
#user_email.place(x=300,y=200)
#----------------------------email start---------------------------------------
user_email=Label(myroot,text='Email-id',font='rockwell 27 bold',fg='red')
user_email.place(x=100,y=300)

user_email_entry=Entry(myroot,font='italic 27 bold',bd=0)
user_email_entry.place(x=270,y=300)
user_email_entry.focus()
#-----------------------------email end-----------------------------------------

user_password=Label(myroot,text="Password",font="rockwell 27 bold",fg='red')
user_password.place(x=100,y=400)

user_password_entry=Entry(myroot,show="⭐",font="rockwell 27 bold",bd=0)
user_password_entry.place(x=285,y=400)

#_______________________________login______________________________________________
def Login_check():
    email=user_email_entry.get()
    user_password=user_password_entry.get()
    mydb= mysql.connector.connect(
        host="Localhost",
        user="root",
        password="",
        database="Covid"
    )
    mycursor=mydb.cursor()
    q="Select * from user where email ='"+email+"' and password ='"+user_password+"'"
    mycursor.execute(q)
    myrecord=mycursor.fetchall()
    if len(myrecord)>0:
        myroot.withdraw()
        mydashboard()

    else:
        messagebox.showwarning('Invalid','Incorrect login Details')

myimage=Image.open("Images/Login 1.png")
myimage_resize=myimage.resize((200,55),Image.Resampling.LANCZOS)
get_image_button=ImageTk.PhotoImage(myimage_resize)
login_button=Button(myroot,image=get_image_button,cursor="hand1",command=Login_check)
login_button.place(x=350,y=470,width=200)


myimage_newuser=Image.open("Images/create new user 1.png")
myimage_resize_newuser=myimage_newuser.resize((200,50),Image.Resampling.LANCZOS)
get_image_newuser=ImageTk.PhotoImage(myimage_resize_newuser)
button_newuser=Button(myroot,image=get_image_newuser,cursor="hand2",command=New_user_page1)
button_newuser.place(x=350,y=550,width=200)



my_title=Label(myroot, text="THE COVID APPLICATION ", fg= "White", bg="red", font=" italic 27")
my_title.place(x=1,y=0)






myroot.mainloop()


