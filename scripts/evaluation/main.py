import sys
sys.path.append('scripts')
from sklearn.model_selection import  GridSearchCV
from sklearn.tree import DecisionTreeRegressor
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score, explained_variance_score

from eda.main import splitData

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
# print(f"Mejores parámetros: {best_params}")
# print(f"Puntuación del mejor modelo (RMSE): {best_score}")
y_pred = grid_search.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
explained_var = explained_variance_score(y_test, y_pred)

print(f"Mejores parámetros: {best_params}")
print(f"RMSE: {best_score}")
print(f"MSE: {mse}")
print(f"MAE: {mae}")
print(f"R²: {r2}")
print(f"Score de Explicación: {explained_var}")


from datetime import datetime
import pandas as pd

fecha_deseada = "2024-01-01"
fecha_deseada_timestamp = pd.to_datetime(fecha_deseada).value // 10 ** 9
numero_predicho = grid_search.predict([[fecha_deseada_timestamp]])
print(f"La predicción para la fecha {fecha_deseada} es: {numero_predicho[0]}")