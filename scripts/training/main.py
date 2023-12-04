import sys
import pandas as pd
sys.path.append('scripts')
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeRegressor
import numpy as np

from eda.main import serieTemporal, columCategorica,splitData

serie_temporal=serieTemporal()
print(serie_temporal)

#Modelo 1 serie Temporal

# serie_temporal=serieTemporal()
# plot_acf(serie_temporal, lags=50)
# plt.show()
# plot_pacf(serie_temporal, lags=50)
# plt.show()
# resultado_df = adfuller(serie_temporal)
# print('p-valor: %f' % resultado_df[1])

# modelo = ARIMA(serie_temporal, order=(1, 0, 1))
# modelo_ajustado = modelo.fit()

# predicciones = modelo_ajustado.forecast(steps=7)
# print(predicciones)

# MODELO 2 Serie temporal

# train = serie_temporal[:int(0.8*len(serie_temporal))]
# test = serie_temporal[int(0.8*len(serie_temporal)):]

# p_range = range(0, 3) 
# d_range = range(0, 3) 
# q_range = range(0, 3)  

# best_aic = float("inf")
# best_order = None
# best_model = None

# for p in p_range:
#     for d in d_range:
#         for q in q_range:
#             try:
#                 tmp_model = ARIMA(train, order=(p, d, q)).fit()
#                 tmp_aic = tmp_model.aic

#                 if tmp_aic < best_aic:
#                     best_aic = tmp_aic
#                     best_order = (p, d, q)
#                     best_model = tmp_model
#             except: 
#                 continue

# print(f'Mejor modelo ARIMA: order={best_order} con AIC={best_aic}')

# Mejor modelo ARIMA: order=(0, 1, 2) con AIC=424716.2503949843

# modelo = ARIMA(serie_temporal, order=(0, 1, 2))
# modelo_ajustado = modelo.fit()

# predicciones = modelo_ajustado.forecast(steps=7)
# print(predicciones)

# MODELO 3 Arbol de decisión 
X_train, X_test, y_train, y_test=splitData()
tree_model = DecisionTreeRegressor(random_state=42)
param_grid = {
    'max_depth': [3, 5, 10, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}
grid_search = GridSearchCV(tree_model, param_grid, cv=3, scoring='neg_mean_squared_error', verbose=1)
grid_search.fit(X_train, y_train)
best_params = grid_search.best_params_
best_score = np.sqrt(-grid_search.best_score_)
print(f"Mejores parámetros: {best_params}")
print(f"Puntuación del mejor modelo (RMSE): {best_score}")