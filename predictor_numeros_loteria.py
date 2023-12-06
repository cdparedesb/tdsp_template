import joblib
import pandas as pd
import numpy as np

class ModeloLoteria:
    def __init__(self, model_path):
        self.model = joblib.load(model_path)

    def predecir_numero(self, fecha):
        timestamp = pd.to_datetime(fecha).value // 10 ** 9
        return self.model.predict([[timestamp]])

if __name__ == "__main__":
    modelo = ModeloLoteria('modelo_numeros_loteria.joblib')
    fecha_prediccion = "2024-01-01"
    prediccion = modelo.predecir_numero(fecha_prediccion)
    print(f"Predicción para {fecha_prediccion}: {prediccion[0]}")
