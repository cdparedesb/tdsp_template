import sys
sys.path.append('scripts')
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeRegressor
import numpy as np

from preprocessing.main import splitData

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