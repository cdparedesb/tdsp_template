import sys
sys.path.append('scripts')

from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score, explained_variance_score
import joblib
from evaluation.main import grid_search
import pandas as pd

fecha_deseada = "2024-01-01"
fecha_deseada_timestamp = pd.to_datetime(fecha_deseada).value // 10 ** 9
numero_predicho = grid_search.predict([[fecha_deseada_timestamp]])
print(f"La predicción para la fecha {fecha_deseada} es: {numero_predicho[0]}")

model_filename = 'modelo_numeros_loteria.joblib'
joblib.dump(grid_search.best_estimator_, model_filename)