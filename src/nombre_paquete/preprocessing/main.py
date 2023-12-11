import pandas as pd
from database.main import get_dataframe
from sklearn.model_selection import train_test_split
 

def cleanDate():
    data = get_dataframe()
    data['FECHA'] = pd.to_datetime(data['FECHA'], errors='coerce')
    lottery_data_cleaned = data.dropna(subset=['FECHA'])
    X = lottery_data_cleaned['FECHA'].map(pd.Timestamp.timestamp).values.reshape(-1, 1)
    y = lottery_data_cleaned['NUMERO'].values

    return X, y

def splitData():
    data=cleanDate()
    X=data[0]
    y=data[1]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test