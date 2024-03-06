import joblib
import pandas as pd
import numpy as np
from tkinter import *
import tkinter.ttk
from PIL import Image, ImageTk

myroot = Tk()

myroot.geometry('1100x900')
myroot.title("Insurance Prediction")
myroot.resizable(False, False)
myimage = Image.open("insurance.jpg")
myimage_resize = myimage.resize((1100, 780), Image.Resampling.LANCZOS)
get_image = ImageTk.PhotoImage(myimage_resize)
my_root_label = Label(myroot, image=get_image, bd=10)
my_root_label.place(x=0, y=0)

#----------------Age label-----------------
agel=Label(myroot,text='Enter Age',fg='black',font='lucida 20 bold')
agel.place(x=10,y=120)
age_entry = Entry(myroot, fg="blue", font="rockwell 20 bold")
age_entry.focus()
age_entry.place(x=175, y=120, width=200, height=35)

#----------------Gender label---------------
genl=Label(myroot,text='Select Gender',fg='black',font='lucida 20 bold')
genl.place(x=10,y=270)
n = StringVar()
gender_choose = tkinter.ttk.Combobox(myroot, width=25, height=400, textvariable=n)
gender_choose['value'] = ('Select Gender', 'Male', 'Female')
gender_choose.current(0)
gender_choose.place(x=220, y=270)

#---------------BMI label--------------
bmil=Label(myroot,text='BMI',fg='black',font='lucida 20 bold')
bmil.place(x=10,y=170)
bmi_entry= Entry(myroot, fg="blue", font="rockwell 20 bold")
bmi_entry.place(x=150, y=170, width=200, height=35)

#---------------Child label------------
childl=Label(myroot,text='Child',fg='black',font='lucida 20 bold')
childl.place(x=10,y=220)
child_entry = Entry(myroot, fg="blue", font="rockwell 20 bold")
child_entry.place(x=150, y=220, width=200, height=35)

#--------------Smoker label------------
smokerl=Label(myroot,text='Smoker',fg='black',font='lucida 20 bold')
smokerl.place(x=10,y=320)

m = StringVar()
smoker_choose = tkinter.ttk.Combobox(myroot, width=20, height=400, textvariable=m)
smoker_choose['value'] = ('Select Smoker', 'no', 'yes')
smoker_choose.current(0)
smoker_choose.place(x=155, y=320)

#------------Region label--------------
regionl=Label(myroot,text='Region',fg='black',font='lucida 20 bold')
regionl.place(x=10,y=370)

o = StringVar()
region_choose = tkinter.ttk.Combobox(myroot, width=20, height=400, textvariable=0)
region_choose['value'] = ('Select Region', 'northeast', 'northwest','southeast','southwest')
region_choose.current(0)
region_choose.place(x=155, y=370)

#------------load joblib files ---------
lo = joblib.load('gender.joblib')
le = joblib.load('smoker.joblib')
ct = joblib.load('onehot.joblib')
sc = joblib.load('scaler.joblib')
regressor = joblib.load('regressor.joblib')

def value():
 age = age_entry.get()
 gen = gender_choose.get()
 bmi = bmi_entry.get()
 child = child_entry.get()
 smoker= smoker_choose.get()
 region = region_choose.get()
 data = pd.DataFrame(
        {'age': [age], 'gender': [gen], 'bmi': [bmi], 'children': [child], 'smoker': [smoker], 'region': [region]})
 data['gender'] = lo.transform(data['gender'])
 data['smoker'] = le.transform(data['smoker'])
 data = ct.transform(data)
 data = sc.transform(data)
 label = Label(myroot, text=regressor.predict(data),bg="silver",font="lucida 20 bold")
 label.place(x=430,y=300)
 my_value = Label(myroot, text="Your Health Insurance will be  ", fg="black", bg="silver", font="lucida 20 bold ")
 my_value.place(x=420, y=250)

#---------Predict Image-------------
myimage3 = Image.open("Login.png")
myimage_resize_newuser2 = myimage3.resize((160, 70), Image.Resampling.LANCZOS)
get_image_newuser2 = ImageTk.PhotoImage(myimage_resize_newuser2)
button_newuser2 = Button(myroot, image=get_image_newuser2, cursor="hand2", command=value, borderwidth=0)
button_newuser2.place(x=150, y=420)

#---------------Title label-----------
my_title = Label(myroot, text="Insurance prediction ", fg="black", bg="silver", font="lucida 20 bold ")
my_title.place(x=380, y=50)
myroot.mainloop()