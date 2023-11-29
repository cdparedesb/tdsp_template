import sys
import pandas as pd
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
sys.path.append('scripts')

from data_acquisition.main import get_dataframe


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

# serie_temporal=serieTemporal()

# plot_acf(serie_temporal, lags=50)
# plt.show()

# plot_pacf(serie_temporal, lags=50)
# plt.show()

# resultado_df = adfuller(serie_temporal)
# print('p-valor: %f' % resultado_df[1])

def columCategorica():
    data = get_dataframe()
    bins = [i for i in range(0, 10001, 1000)]
    labels = [f'{i}-{i+999}' for i in range(0, 9001, 1000)]
    data['categoria'] = pd.cut(data['NUMERO'], bins=bins, labels=labels, right=False)
    print(data.head())
    return data
