import pandas as pd
import joblib


lf = pd.read_csv('loan.csv')

lf = lf.dropna()
lf = lf.drop('Loan_ID', axis=1)
lf = lf.drop('Loan_Status', axis=1)
lf = lf.drop('Credit_History', axis=1)
X = lf.drop('LoanAmount', axis=1)
X['Gender']=X['Gender'].str.lower()
X['Married']=X['Married'].str.lower()
X['Education']=X['Education'].str.lower()
X['Self_Employed']=X['Self_Employed'].str.lower()
X['Property_Area']=X['Property_Area'].str.lower()
y = lf.LoanAmount

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
X['Gender'] = le.fit_transform(X['Gender'])
joblib.dump(le, 'Gender1.joblib')

lo = LabelEncoder()
X['Married'] = lo.fit_transform(X['Married'])
joblib.dump(lo, 'Married1.joblib')

li = LabelEncoder()
X['Education'] = li.fit_transform(X['Education'])
joblib.dump(li, 'Education1.joblib')

la = LabelEncoder()
X['Self_Employed'] = la.fit_transform(X['Self_Employed'])
joblib.dump(la, 'Self_Employed1.joblib')

lx = LabelEncoder()
X['Dependents'] = lx.fit_transform(X['Dependents'])
joblib.dump(lx, 'Dependents1.joblib')

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

ct = ColumnTransformer([('encoder', OneHotEncoder(), [8])], remainder='passthrough')
X = ct.fit_transform(X)
joblib.dump(ct, 'onehot1.joblib')
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X = sc.fit_transform(X)
joblib.dump(sc, 'scaler1.joblib')

from sklearn.model_selection import train_test_split as tts

X_train, X_test, y_train, y_test = tts(X, y, test_size=0.02, random_state=1)

from sklearn.svm import SVR

regressor = SVR(C=100) #support vector regression
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)

from sklearn.metrics import r2_score

print(r2_score(y_test, y_pred))

joblib.dump(regressor,'regressor1.joblib')