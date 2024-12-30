# Exercise 4: Feature Store and Model Store Implementation

This document provides a step-by-step guide to implementing a feature store using Feast and a model store using MLflow. It demonstrates setup, configuration, and management of features and models to streamline machine learning workflows.

---

## **1. Project Overview**

Here is the output image:
<!--  -->

### You can Notebook Either

### **File Structure**
```plaintext
MLOps_Playground/Exercises/Exercise_4/
├── feature_store.py     # Code to implement the Feast feature store
├── model_store.py       # MLflow model store implementation
├── feature_store_example.ipynb  # Note Book for Feature Store
├── model_store_example.ipynb    # Note Book for Model Store
```

---

## **2. Feature Store Implementation**

### **feature_store.py**
This script sets up a feature store using Feast and provides functionality for retrieving historical and real-time features.

#### **Code**
```python
from feast import FeatureStore
import pandas as pd

store = FeatureStore(repo_path=".")

# Historical Features Retrieval
def get_historical_features():
    entity_df = pd.DataFrame(
        {
            "driver_id": [1001, 1002],
            "event_timestamp": ["2021-04-12 10:59:42", "2021-04-12 08:12:10"],
        }
    )
    features = store.get_historical_features(
        entity_df=entity_df,
        feature_refs=["driver.conv_rate", "driver.acc_rate", "driver.avg_daily_trips"],
    ).to_df()
    return features

# Materialize Features
store.materialize_incremental(end_date=pd.Timestamp.now().isoformat())

# Read Online Features
features = store.get_online_features(
    feature_refs=["driver.conv_rate", "driver.acc_rate"],
    entity_rows=[{"driver_id": 1001}],
).to_dict()
```

#### **Steps to Execute**
1. Install Feast:
   ```bash
   pip install feast
   ```
2. Initialize the feature repository:
   ```bash
   feast init feature_repo
   cd feature_repo
   ```
3. Apply changes and retrieve features:
   ```bash
   feast apply
   python feature_store.py
   ```

   This will fetch the required features and materialize them for online use.

---

## **3. Model Store Implementation**

### **model_store.py**
This script demonstrates model management using MLflow, including registering, logging, and retrieving models.

#### **Code**
```python
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
```

#### **Steps to Execute**
1. Install MLflow:
   ```bash
   pip install mlflow scikit-learn
   ```
2. Train and log the model:
   ```bash
   python model_store.py
   ```
3. Use the logged model for predictions by loading it through MLflow’s APIs.

---

## **4. Docker Deployment**

### **Dockerfile**
The Dockerfile builds a container for both feature and model stores.

#### **Code**
```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "feature_store.py"]
```

### **requirements.txt**
List of required dependencies:
```
feast
mlflow
scikit-learn
pandas
```

#### **Steps to Build and Run**
1. Build the Docker image:
   ```bash
   docker build -t feature_model_store .
   ```
2. Run the Docker container:
   ```bash
   docker run -p 5000:5000 feature_model_store
   ```

---

## **5. Notes and Best Practices**
- **Feature Store:** Use proper configurations to streamline feature retrieval for both batch and online modes.
- **Model Store:** Document and track model parameters and metrics for reproducibility.
- **General:** Ensure your Docker container exposes necessary ports and is configured correctly for both feature and model store endpoints.

---

## **License and Copyright**
S. Pratap Yadav
GitHub: iSPYadav01
Portfolio: https://ispyadav01.github.io/Portfolio/

Follow me on:
[S. Pratap Yadav](https://ispyadav01.github.io/Portfolio/)
[LinkedIn](https://www.linkedin.com/in/iSPYadav01)
[Twitter](https://twitter.com/iSPYadav01)
[GitHub](https://github.com/iSPYadav01)
[Medium](https://medium.com/@ispyadav01)

© 2024 Data Dynasty Lab. All Rights Reserved.
This project is made available under the MIT License.  
Feel free to use, modify, and distribute with attribution.
