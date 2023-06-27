import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

data = pd.read_csv('Prediction-of-views_ML/data/processed.csv')

train, test = train_test_split(data, test_size=0.3, shuffle=True) #con shuffle, que los videos estaban ordenados por visualizaciones

train.to_csv('Prediction-of-views_ML/data/train.csv', index=False) #PARA PASAR PARTE A TRAIN Y PARTE A TEST
test.to_csv('Prediction-of-views_ML/data/test.csv', index=False)

X = train[['Med Juego Compartido']]
y = train[['Visualizaciones']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=33)

# REGRESIÓN LINEAL

lr = LinearRegression()
lr.fit(X_train,y_train)

y_pred = lr.predict(X_test) #predicciones

with open('Prediction-of-views_ML/models/modelo_LR.pkl', 'wb') as archivo:
    pickle.dump(lr, archivo)