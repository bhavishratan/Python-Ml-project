import joblib
import pandas as pd
from tkinter import *
import tkinter.ttk
from PIL import Image, ImageTk

myroot = Tk()

myroot.geometry('1300x1000')
myroot.title("USED CAR PRICE PREDICTION")
myroot.resizable(False, False)
myimage = Image.open("562673.jpg")
myimage_resize = myimage.resize((1300,1000), Image.Resampling.LANCZOS)
get_image = ImageTk.PhotoImage(myimage_resize)
my_root_label = Label(myroot, image=get_image, bd=0)
my_root_label.place(x=0, y=0)

obj_frame1=Frame(myroot,bg="#5794a9")
obj_frame1.place(x=5,y=90,width=500,height=525)


#----------------Transmission label---------------
Transmissionl=Label(myroot,text='Transmission',fg='black',font='lucida 20 bold',bg="#5794a9")
Transmissionl.place(x=10,y=100)
n = StringVar()
Transmission_choose = tkinter.ttk.Combobox(myroot, width=15, height=200, textvariable=n,font='lucida 15')
Transmission_choose['value'] = ('Select Transmission', 'manual', 'automatic')
Transmission_choose.current(0)
Transmission_choose.place(x=250, y=100)

#----------------Fuel label---------------
Fuell=Label(myroot,text='Fuel',fg='black',font='lucida 20 bold',bg="#5794a9")
Fuell.place(x=10,y=140)
m = StringVar()
Fuel_choose = tkinter.ttk.Combobox(myroot, width=15, height=400, textvariable=m,font='lucida 15')
Fuel_choose['value'] = ('Fuel Type', 'diesel', 'petrol','lpg','cng')
Fuel_choose.current(0)
Fuel_choose.place(x=250, y=140)

#----------------Owner label---------------
Ownerl=Label(myroot,text='Owner',fg='black',font='lucida 20 bold',bg="#5794a9")
Ownerl.place(x=10,y=180)
o = StringVar()
Owner_choose = tkinter.ttk.Combobox(myroot, width=15, height=400, textvariable=o,font='lucida 15')
Owner_choose['value'] = ('Owner', 'first owner', 'second owner','third owner')
Owner_choose.current(0)
Owner_choose.place(x=250, y=180)

#----------------Seller label---------------
Seller_typel=Label(myroot,text='Seller type',fg='black',font='lucida 20 bold',bg="#5794a9")
Seller_typel.place(x=10,y=220)
p = StringVar()
Seller_choose = tkinter.ttk.Combobox(myroot, width=15, height=400, textvariable=p,font='lucida 15')
Seller_choose['value'] = ('Seller Type', 'individual', 'dealer','trustmark dealer')
Seller_choose.current(0)
Seller_choose.place(x=250, y=220)

#----------------Seats label---------------
Seatsl=Label(myroot,text='Seats',fg='black',font='lucida 20 bold',bg="#5794a9")
Seatsl.place(x=10,y=260)
q = StringVar()
Seats_choose = tkinter.ttk.Combobox(myroot, width=15, height=400, textvariable=q,font='lucida 15')
Seats_choose['value'] = ('Seats', '2', '4','5','7','8')
Seats_choose.current(0)
Seats_choose.place(x=250, y=260)

#----------------Engine label-----------------
Enginel=Label(myroot,text='Engine(cc)',fg='black',font='lucida 18 bold',bg="#5794a9")
Enginel.place(x=10,y=300)
Engine_entry = Entry(myroot, fg="black", font="rockwell 18 bold")
Engine_entry.place(x=250, y=300, width=200, height=35)

#----------------Power label-----------------
Powerl=Label(myroot,text='Power(bhp)',fg='black',font='lucida 18 bold',bg="#5794a9")
Powerl.place(x=10,y=340)
Power_entry = Entry(myroot, fg="black", font="rockwell 18 bold")
Power_entry.place(x=250, y=340, width=200, height=35)

#----------------Year label-----------------
Yearl=Label(myroot,text='Year',fg='black',font='lucida 18 bold',bg="#5794a9")
Yearl.place(x=10,y=380)
Year_entry = Entry(myroot, fg="black", font="rockwell 18 bold")
Year_entry.place(x=250, y=380, width=200, height=35)

#----------------mileage label-----------------
Mileagel=Label(myroot,text='Mileage(kmph)',fg='black',font='lucida 18 bold',bg="#5794a9")
Mileagel.place(x=10,y=420)
Mileage_entry = Entry(myroot, fg="black", font="rockwell 18 bold")
Mileage_entry.place(x=250, y=420, width=200, height=35)

#----------------Km label-----------------
Km_drivenl=Label(myroot,text='Kilometers driven',font='lucida 18 bold',bg="#5794a9")
Km_drivenl.place(x=10,y=460)
Km_driven_entry = Entry(myroot, fg="black", font="rockwell 18 bold")
Km_driven_entry.place(x=250, y=460, width=200, height=35)


#------------load joblib files ---------
la=joblib.load('transmission.joblib')
li=joblib.load('fuel.joblib')
le=joblib.load('seller_type.joblib')
ct=joblib.load('onehot.joblib')
sc=joblib.load('scaler.joblib')
regressor=joblib.load('regressor.joblib')

def value():
 transmission = Transmission_choose.get()
 fuel = Fuel_choose.get()
 owner = Owner_choose.get()
 seller_type = Seller_choose.get()
 seats = Seats_choose.get()
 engine = Engine_entry.get()
 max_power = Power_entry.get()
 year = Year_entry.get()
 mileage=Mileage_entry.get()
 km_driven=Km_driven_entry.get()

 data = pd.DataFrame({'transmission': [transmission], 'fuel': [fuel], 'owner': [owner], 'seller_type': [seller_type],
                      'seats': [seats], 'year': [year], 'mileage': [mileage], 'km_driven': [km_driven],
                      'max_power': [max_power], 'engine': [engine]})
 data['transmission'] = la.transform(data['transmission'])
 data['fuel'] = li.transform(data['fuel'])
 data['seller_type'] = le.transform(data['seller_type'])
 data = ct.transform(data)
 data = sc.transform(data)
 label = Label(myroot, text=(regressor.predict(data)).astype(int),bg="white",font="lucida 20 bold")
 label.place(x=730,y=500)
 my_value = Label(myroot, text="Your Car is Worth:  ", fg="black", bg="white", font="lucida 20 bold ")
 my_value.place(x=720, y=450)


#---------Predict Image-------------
myimage3 = Image.open("get-it-now-button.png")
myimage_resize_newuser2 = myimage3.resize((160, 70), Image.Resampling.LANCZOS)
get_image_newuser2 = ImageTk.PhotoImage(myimage_resize_newuser2)
button_newuser2 = Button(myroot,image=get_image_newuser2, cursor="hand2",command=value, borderwidth=0)
button_newuser2.place(x=150, y=520)

#---------------Title label-----------
my_title = Label(myroot, text=" USED CAR PRICE PREDICTION ", fg="white", bg="#1e02a8", font="lucida 25 bold ")
my_title.place(x=380, y=0)
myroot.mainloop()