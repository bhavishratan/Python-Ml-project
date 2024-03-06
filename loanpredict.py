import joblib
import pandas as pd
import numpy as np



#----------------Storing Values------------------
lo=joblib.load('Gender1.joblib')
la=joblib.load('Married1.joblib')
le=joblib.load('Education1.joblib')
lu=joblib.load('Self_Employed1.joblib')
li=joblib.load('Dependents1.joblib')
ct=joblib.load('onehot1.joblib')
sc=joblib.load('scaler1.joblib')
regressor1=joblib.load('regressor1.joblib')


Gender=input('Gender ')
Married=input('Married ')
Dependents=input('Dependents')
Education=input('Education ')
Self_employed=input('Self employed ')
Applicantincome=float(input('ApplicantIncome'))
Coapplicantincome=float(input('CoapplicantIncome'))
Lmt=float(input('Loan_Amount_Term '))
Propertyarea=input('Property_Area')


data=pd.DataFrame({'Gender':[Gender],'Married':[Married],'Dependents':[Dependents],'Education':[Education],
                   'Self_Employed':[Self_employed],'ApplicantIncome':[Applicantincome],'CoapplicantIncome':[Coapplicantincome],'Loan_Amount_Term':[Lmt],'Property_Area':[Propertyarea]})

data['Gender']=lo.transform(data['Gender'])
data['Married']=la.transform(data['Married'])
data['Dependents']=li.transform(data['Dependents'])
data['Education']=le.transform(data['Education'])
data['Self_Employed']=lu.transform(data['Self_Employed'])
data=ct.transform(data)
data=sc.transform(data)

print(regressor1.predict(data))