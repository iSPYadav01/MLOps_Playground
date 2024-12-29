import mlflow
import mlflow.sklearn
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Train Model
X, y = make_regression(n_samples=1000, n_features=10, noise=0.1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Log Model in MLflow
mlflow.sklearn.log_model(model, artifact_path="model")
mlflow.log_param("model_type", "RandomForest")
mlflow.log_metric("r2_score", model.score(X_test, y_test))

# Retrieve Model
logged_model = "runs:/<run-id>/model"
loaded_model = mlflow.pyfunc.load_model(logged_model)
print(loaded_model.predict(X_test[:1]))
