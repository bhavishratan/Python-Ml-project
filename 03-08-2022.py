from tkinter import *
root=Tk()
root.geometry('400x400')


def fxn():
    print(var.get())
var=IntVar()

r1=Radiobutton(root,text='option1',value=1,variable=var)
r1.place(x=20,y=20)
r2=Radiobutton(root,text='option2',value=1,variable=var)
r2.place(x=20,y=70)
r3=Radiobutton(root,text='option3',value=1,variable=var)
r3.place(x=20,y=100)
r4=Radiobutton(root,text='option4',value=1,variable=var)
r4.place(x=20,y=150)
btn=Button(root,text='Press',command=fxn)
btn.place(x=60,y=180)
a = input("Enter the value of w")
print(a)
root.mainloop()
