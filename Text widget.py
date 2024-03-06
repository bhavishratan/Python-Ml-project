from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
def fxn():
    ans=filedialog.askopenfile(title='open')
    print(ans)

    #messagebox.showwarning('Title','Warning')
    '''
    print(t.get('1.0','2.4'))
    t.delete('1.0','end')'''

root=Tk()
root.geometry('600x600')

t=Text(root,height=15,width=15)
t.place(x=50,y=50)
btn=Button(root,text="submit",command=fxn)
btn.place(x=250,y=250)
root.mainloop()




