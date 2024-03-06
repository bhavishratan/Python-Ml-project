import joblib
import pandas as pd
import numpy as np
from tkinter import *
import tkinter.ttk
from PIL import Image, ImageTk

myroot = Tk()

myroot.geometry('1300x1000')
myroot.title(" Welcome to Loan Prediction Application ")
myroot.resizable(False, False)
myimage = Image.open("Image/yo.jpg")
myimage_resize = myimage.resize((1300, 800), Image.Resampling.LANCZOS)
get_image = ImageTk.PhotoImage(myimage_resize)
my_root_label = Label(myroot, image=get_image, bd=0)
my_root_label.place(x=0, y=0)



#----------------Married label-----------------
marriedl=Label(myroot,text='Married',fg='black',font='lucida 30 bold')
marriedl.place(x=10,y=80)
q = StringVar()
married_choose = tkinter.ttk.Combobox(myroot, width=20, height=400,font='lucida 15 ', textvariable=q)
married_choose['value'] = ('Select Married or not ', 'yes', 'no')
married_choose.current(0)
married_choose.place(x= 285 ,y = 85)


#---------------Dependent label--------------
dependentl=Label(myroot,text='Dependent',fg='black',font='lucida 30 bold')
dependentl.place(x=720,y=80)
dependent_entry= Entry(myroot, fg="blue", font="rockwell 20 bold")
dependent_entry.place(x=1095, y=85, width=200, height=35)


#----------------Gender label---------------
genl=Label(myroot,text='Gender',fg='black',font='lucida 30 bold')
genl.place(x=10,y=320)
n = StringVar()
gender_choose = tkinter.ttk.Combobox(myroot, width=20, height=400,font='lucida 15 ', textvariable=n)
gender_choose['value'] = ('Select Gender', 'male', 'female')
gender_choose.current(0)
gender_choose.place(x=285, y=325)


#---------------self employed label------------
empl=Label(myroot,text='Self employed',fg='black',font='lucida 30 bold')
empl.place(x=10,y=440)
p = StringVar()
emp_choose = tkinter.ttk.Combobox(myroot, width=20, height=400,font='lucida 15 ', textvariable=p)
emp_choose['value'] = ('Select Self employed', 'yes', 'no')
emp_choose.current(0)
emp_choose.place(x=285, y=440)


#-------------- Education label------------
educationl=Label(myroot,text='Education',fg='black',font='lucida 30 bold')
educationl.place(x=10,y=560)

m = StringVar()
education_choose = tkinter.ttk.Combobox(myroot, width=20, height=400,font='lucida 15 ', textvariable=m)
education_choose['value'] = ('Select Education', 'graduate', 'not graduate')
education_choose.current(0)
education_choose.place(x=285, y=565)


#------------Area label--------------
areal=Label(myroot,text='Area',fg='black',font='lucida 30 bold')
areal.place(x=10,y=200)

o = StringVar()
area_choose = tkinter.ttk.Combobox(myroot, width=20, height=400,font='lucida 15 ', textvariable=o)
area_choose['value'] = ('Select Area', 'urban', 'semiurban','rural')
area_choose.current(0)
area_choose.place(x=285, y=205)


#---------Applicantincome-----------
appincomel=Label(myroot,text='Applicant Income',fg='black',font='lucida 30 bold')
appincomel.place(x=720,y=200)
appincome_entry= Entry(myroot, fg="blue", font="rockwell 20 bold")
appincome_entry.place(x=1095, y=205, width=200, height=35)


#-----------Coapplicantincome---------
coappincomel=Label(myroot,text='Coapplicant Income',fg='black',font='lucida 30 bold')
coappincomel.place(x=720,y=320)
coappincome_entry= Entry(myroot, fg="blue", font="rockwell 20 bold")
coappincome_entry.place(x=1095, y=325, width=200, height=35)


#------------Loan amount term----------
lmtl=Label(myroot,text='Loan amount term',fg='black',font='lucida 30 bold')
lmtl.place(x=720,y=440)
lmt_entry= Entry(myroot, fg="blue", font="rockwell 20 bold")
lmt_entry.place(x=1095, y=445, width=200, height=35)


#------------load joblib files ---------
lo=joblib.load('Gender1.joblib')
la=joblib.load('Married1.joblib')
le=joblib.load('Education1.joblib')
lu=joblib.load('Self_Employed1.joblib')
li=joblib.load('Dependents1.joblib')
ct=joblib.load('onehot1.joblib')
sc=joblib.load('scaler1.joblib')
regressor1=joblib.load('regressor1.joblib')


def value():

 Gen = gender_choose.get()
 dependent = dependent_entry.get()
 married = married_choose.get()
 self_employed = emp_choose.get()
 education = education_choose.get()
 area = area_choose.get()
 Applicantincome = appincome_entry.get()
 Coapplicantincome = coappincome_entry.get()
 Lmt = lmt_entry.get()



 data = pd.DataFrame({'Gender': [Gen], 'Married': [married], 'Dependents': [dependent], 'Education': [education],
                      'Self_Employed': [self_employed], 'ApplicantIncome': [Applicantincome],
                      'CoapplicantIncome': [Coapplicantincome], 'Loan_Amount_Term': [Lmt],
                      'Property_Area': [area]})

 data['Gender'] = lo.transform(data['Gender'])
 data['Married'] = la.transform(data['Married'])
 data['Dependents'] = li.transform(data['Dependents'])
 data['Education'] = le.transform(data['Education'])
 data['Self_Employed'] = lu.transform(data['Self_Employed'])
 data = ct.transform(data)
 data = sc.transform(data)

 label = Label(myroot, text=regressor1.predict(data),bg="#CBD7F3",font="lucida 25 bold")
 label.place(x=550,y=690)
 my_value = Label(myroot, text="", fg="black", bg="#CBD7F3", font="lucida 25 bold ")
 my_value.place(x=390, y=250)



#---------Predict Image-------------
myimage3 = Image.open("Image/predict.jpg")
myimage_resize_newuser2 = myimage3.resize((160, 70), Image.Resampling.LANCZOS)
get_image_newuser2 = ImageTk.PhotoImage(myimage_resize_newuser2)
button_newuser2 = Button(myroot, image=get_image_newuser2, cursor="hand2", command=value, borderwidth=0)
button_newuser2.place(x=550, y=610)


#---------------Title label-----------
my_title = Label(myroot, text="LOAN PREDICTION ", fg="black", bg="#CBD7F3", font="Castellar 35 bold ")
my_title.place(x=400, y=10)
myroot.mainloop()
