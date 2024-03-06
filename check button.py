from tkinter import *
root=Tk()
root.geometry('400x400')


def fxn():
    print(var1.get())
    print(var2.get())
    print(var3.get())
    print(var4.get())
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()

r1=Checkbutton(root,text='option1',onvalue=1,offvalue=0,variable=var1)
r1.place(x=20,y=20)
r2=Checkbutton(root,text='option2',onvalue=1,offvalue=0,variable=var2)
r2.place(x=20,y=70)
r3=Checkbutton(root,text='option3',onvalue=1,offvalue=0,variable=var3)
r3.place(x=20,y=100)
r4=Checkbutton(root,text='option4',onvalue=1,offvalue=0,variable=var4)
r4.place(x=20,y=150)
btn=Button(root,text='Press',command=fxn)
btn.place(x=60,y=180)

root.mainloop()
