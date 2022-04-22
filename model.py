#import libraries
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from xgboost import  XGBClassifier
from sklearn.metrics import  classification_report, accuracy_score
import pickle


data = pd.read_csv('heart.csv')
print(data.head())
print(data.shape)
print(data.describe())
print(data.info())
print(data.isna().sum())
print(data.nunique())
print(data.dtypes)
print(data.columns)

#s = (data.dtypes  == 'object')
#cat_cols = list(s[s].index)
#cat_cols = data.select_dtypes(include=['object']).columns.tolist()
#print(cat_cols)
cat_cols = data[["Sex","ChestPainType","RestingECG", "ExerciseAngina", "ST_Slope"]]
cat_cols_encoded = pd.get_dummies(cat_cols)
data.join(cat_cols_encoded)
data.drop(["Sex","ChestPainType","RestingECG", "ExerciseAngina", "ST_Slope"], axis=1, inplace=True)
data.columns
data = data.join(cat_cols_encoded)
print(data.shape)

x = data.drop('HeartDisease', axis =1)
y = data.HeartDisease
print(x.columns)
print(y.head())

scaler = StandardScaler()
x = scaler.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.2, random_state=0)

xgb_model = XGBClassifier(n_estimators=1000, learning_rate=0.05, n_jobs=4)
xgb_model.fit(x_train,y_train,early_stopping_rounds=5, eval_set = [(x_test,y_test)], verbose=False)
prediction = xgb_model.predict(x_test)
accuracy = accuracy_score(y_test, prediction)
print('accuracy score = {}'.format(accuracy))
pickle.dump(xgb_model, open("model.pkl", 'wb'))
