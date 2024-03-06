from tkinter import *
from PIL import Image,ImageTk
from signip import New_user_page
myroot=Tk()

myroot.geometry('1100x700+250+10')
myroot.title("The Avenger's ")
myroot.resizable(False,False)

myimage=Image.open("images/elizabeth-olsen-as-scarlet-witch-in-wanda-vision-4k-of-1920x1080.jpg")
myimage_resize=myimage.resize((1100,700), not Image.Resampling.LANCZOS)
get_image=ImageTk.PhotoImage(myimage_resize)
my_root_label=Label(myroot,image=get_image,bd=0)
my_root_label.place(x=0,y=0)



#user_email=Label(myroot,text="Email-id",font="lucida 30 bold",fg="blue")
#user_email.place(x=300,y=200)
#----------------------------email start---------------------------------------
user_email=Label(myroot,text='Email-id',font='lucida 30 bold',fg='red')
user_email.place(x=100,y=300)

user_email_entry=Entry(myroot,font='lucida 30 bold',bd=0)
user_email_entry.place(x=270,y=300)
user_email_entry.focus()
#-----------------------------email end-----------------------------------------

user_password=Label(myroot,text="Password",font="lucida 30 bold",fg='red')
user_password.place(x=100,y=400)

user_password_entry=Entry(myroot,show="^",font="ludica 30 bold",bd=0)
user_password_entry.place(x=305,y=400)


myimage=Image.open("Images/Login.png")
myimage_resize=myimage.resize((300,75),Image.Resampling.LANCZOS)
get_image_button=ImageTk.PhotoImage(myimage_resize)
login_button=Button(myroot,image=get_image_button,cursor="hand1")
login_button.place(x=400,y=450,width=200)


myimage_newuser=Image.open("Images/create new user.png")
myimage_resize_newuser=myimage_newuser.resize((200,100),Image.Resampling.LANCZOS)
get_image_newuser=ImageTk.PhotoImage(myimage_resize_newuser)
button_newuser=Button(myroot,image=get_image_newuser,cursor="hand2",command=New_user_page)
button_newuser.place(x=400,y=550,width=200)



my_title=Label(myroot, text=" WELCOME TO MARVEL CLUB ", fg= "red", bg="yellow", font="lucida 20 bold underline")
my_title.place(x=375,y=0)



myroot.mainloop()


