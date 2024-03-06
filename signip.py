from tkinter import *
from PIL import Image,ImageTk

def New_user_page():
    myroot_signup=Toplevel()
    myroot_signup.geometry('1100x700+200+10')
    myroot_signup.title('New user registration ')
    myroot_signup.resizable(False,False)

    myimage1 = Image.open("Images/R.jpg")
    myimage_resize1 = myimage1.resize((1080,720), Image.Resampling.LANCZOS)
    get_image1 = ImageTk.PhotoImage(myimage_resize1)
    my_root_label1 = Button(myroot_signup, image=get_image1,bd=0)
    my_root_label1.place(x=0,y=0)



    myroot_signup.mainloop()