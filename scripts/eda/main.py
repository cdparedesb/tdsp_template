import sys
import pandas as pd
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeRegressor
sys.path.append('scripts')

from data_acquisition.main import get_dataframe
from preprocessing.main import cleanDate


def convert_fecha(fecha):
    try:
        return pd.to_datetime(fecha, format='%d/%m/%Y')
    except ValueError:
        return pd.to_datetime(fecha, format='%m/%d/%Y')

def serieTemporal():
    data = get_dataframe()
    data['FECHA'] = data['FECHA'].apply(convert_fecha)

    data.sort_values('FECHA', inplace=True)
    serie_temporal = data['NUMERO']

    return serie_temporal

def columCategorica():
    data = get_dataframe()
    bins = [i for i in range(0, 10001, 1000)]
    labels = [f'{i}-{i+999}' for i in range(0, 9001, 1000)]
    data['categoria'] = pd.cut(data['NUMERO'], bins=bins, labels=labels, right=False)
    print(data.head())
    return data

def splitData():
    data=cleanDate()
    X=data[0]
    y=data[1]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test