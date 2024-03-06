import pandas as pd
import joblib
import numpy as np

df=pd.read_csv('Car.csv')

df=df.drop(columns='torque')
df=df.drop(columns='i')
df=df.drop(columns='name')
#df=df.drop(columns='max_power')
#df=df.drop(columns='engine')

df['km_driven']=df['km_driven'].astype('float64')
df['km_driven']=df['km_driven'].astype('float64')
df['engine']=df['engine'].replace({'CC':''},regex=True)
df['engine']=df['engine'].replace({' ':''},regex=True)

df['max_power']=df['max_power'].replace({'.bhp':''},regex=True)
df = df.replace(r'^\s*$', np.nan, regex=True)
df=df.dropna()

Y=df['selling_price']
X=df.drop(columns='selling_price')

#owner

X['owner']=X['owner'].str.lower()
#print(X['owner'].unique())
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
X['owner']=le.fit_transform(X['owner'])
joblib.dump(le,'owner.joblib')

#fuel
X['fuel']=X['fuel'].str.lower()
print(X['fuel'].unique())
from sklearn.preprocessing import LabelEncoder
la=LabelEncoder()
X['fuel']=la.fit_transform(X['fuel'])
#X['fuel']=X['transmission'].astype('float64')
joblib.dump(la,'fuel.joblib')

#seller_type
from sklearn.preprocessing import LabelEncoder
X['seller_type']=X['seller_type'].str.lower()
print(X['seller_type'].unique())
lu=LabelEncoder()
X['seller_type']=lu.fit_transform(X['seller_type'])
#X['seller_type']=X['seller_type'].astype('float64')
joblib.dump(lu,'seller_type.joblib')

#transmission

X['transmission']=X['transmission'].str.lower()
print(X['transmission'].unique())
lo=LabelEncoder()

X['transmission']=lo.fit_transform(X['transmission'])
X['transmission']=X['transmission'].astype('float64')
joblib.dump(lo,'transmission.joblib')

#seats

#X['seats']=X['seats'].str.lower()
print(X['seats'].unique())
from sklearn.preprocessing import LabelEncoder
li=LabelEncoder()
X['seats']=li.fit_transform(X['seats'])
joblib.dump(li,'seats.joblib')

#mileage

X['mileage']=X['mileage'].replace({'kmpl':''},regex=True)
X['mileage']=X['mileage'].replace({'km/kg':''},regex=True)
X['mileage']=X['mileage'].astype('float64')

#engine


#X=X.dropna()
#X['engine']=X['engine'].astype('float64')

'''#max_power
X['max_power']=X['max_power'].replace({' ':''},regex=True) 
X['max_power']=X['max_power'].replace({'bhp':''},regex=True) 
#X['max_power']=X['max_power'].replace({'.':''},regex=True) 
X['max_power']=X['max_power'].astype('float64')
print(X.dtypes)'''

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct=ColumnTransformer(transformers=[('encoder',OneHotEncoder(),[4])],remainder='passthrough')
X=ct.fit_transform(X)

joblib.dump(ct,'onehot.joblib')


from sklearn.preprocessing import StandardScaler as SC
sc=SC()#Transformers
X=sc.fit_transform(X)
joblib.dump(sc,'scaler.joblib')



from sklearn.model_selection import train_test_split as tts

X_train,X_test,y_train,y_test=tts(X,Y,test_size=0.05,random_state=2)



#Training Linear Regression
from sklearn.svm import SVR as LR
regressor=LR(C=1000000)#Estimator
regressor.fit(X_train,y_train)


y_pred=regressor.predict(X_test)


#Metrics

from sklearn.metrics import r2_score
print(r2_score(y_test,y_pred))



joblib.dump(regressor,'regressor.joblib')






lo=joblib.load('transmission.joblib')
la=joblib.load('fuel.joblib')
le=joblib.load('owner.joblib')
lu=joblib.load('seller_type.joblib')
li=joblib.load('seats.joblib')

ct=joblib.load('onehot.joblib')

sc=joblib.load('scaler.joblib')
regressor=joblib.load('regressor.joblib')

transmission=float(input('Enter transmission '))
fuel=float(input('Enter fuel '))
owner=input('Enter owner')
seller_type=int(input('Enter seller_type '))
seats=input('Enter seats? ')
#engine=input('Enter engine')
#max_power=input('max_power')
year=input('year ')
mileage=input('mileage ')
km_driven=input('km_driven ')

data=pd.DataFrame({'transmission':[transmission],'fuel':[fuel],'owner':[owner],'seller_type':[seller_type],
                   'seats':[seats],'year':[year],'mileage':[mileage],'km_driven':[km_driven]})

data['transmission']=lo.transform(data['transmission'])
data['owner']=le.transform(data['owner'])
data['fuel']=la.transform(data['fuel'])
data['seller_type']=lu.transform(data['seller_type'])
data['seats']=li.transform(data['seats'])
data=ct.transform(data)
data=sc.transform(data)

print(regressor.predict(data))