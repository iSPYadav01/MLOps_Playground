<<<<<<< HEAD
from sklearn.datasets import make_regression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

import mlflow
import mlflow.sklearn
from mlflow.models import infer_signature

# mlflow.set_tracking_uri(uri="http://127.0.0.1:8080")

with mlflow.start_run() as run:
    X, y = make_regression(n_features=4, n_informative=2, random_state=0, shuffle=False)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    params = {"max_depth": 2, "random_state": 42}
    model = RandomForestRegressor(**params)
    model.fit(X_train, y_train)

    # Infer the model signature
    y_pred = model.predict(X_test)
    signature = infer_signature(X_test, y_pred)

    # Log parameters and metrics using the MLflow APIs
    mlflow.log_params(params)
    mlflow.log_metrics({"mse": mean_squared_error(y_test, y_pred)})

    # Log the sklearn model and register as version 1
    mlflow.sklearn.log_model(
        sk_model=model,
        artifact_path="sklearn-model",
        signature=signature,
        registered_model_name="sk-learn-random-forest-reg-model",
    )


import mlflow.pyfunc

model_name = "sk-learn-random-forest-reg-model"
model_version = 1

model = mlflow.pyfunc.load_model(model_uri=f"models:/{model_name}/{model_version}")

# model.predict(data)


model



## If you had also created the second version:
model_name = "sk-learn-random-forest-reg-model"
model_version = 2

model = mlflow.pyfunc.load_model(model_uri=f"models:/{model_name}/{model_version}")


model
=======
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
>>>>>>> 9e8de85791c56f69b71050f3298b6b1d8cfc5eb2
