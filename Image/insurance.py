import pandas as pd
import numpy as np

import joblib

df=pd.read_csv(r'C:\Users\91946\PycharmProjects\GUI\insurance.csv')

X=df.iloc[:,:-1]
y=df.iloc[:,-1]


### Dummy Variable trap ###


from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
X['gender']=le.fit_transform(X['gender'])
joblib.dump(le,'gender.joblib')


lo=LabelEncoder()
X['smoker']=lo.fit_transform(X['smoker'])
joblib.dump(lo,'smoker.joblib')


from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct=ColumnTransformer([('encoder',OneHotEncoder(),[5])],remainder='passthrough')
X=ct.fit_transform(X)
joblib.dump(ct,'onehot.joblib')

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X=sc.fit_transform(X)
joblib.dump(sc,'scaler.joblib')

from sklearn.model_selection import train_test_split as tts
X_train,X_text,y_train,y_test=tts(X,y,test_size=0.2,random_state=0)



#from sklearn.linear_model import LinearRegression as LR
#regressor=LR()

from sklearn.svm import SVR
regressor=SVR(C=10000)
regressor.fit(X_train,y_train)

y_pred=regressor.predict(X_text)


from sklearn.metrics import r2_score
print(r2_score(y_test,y_pred))


joblib.dump(regressor,'regressor.joblib')


