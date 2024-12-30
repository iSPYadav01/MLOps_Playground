# Exercise 1: Iris Flower Classification with Random Forest

This repository demonstrates the implementation of a Random Forest classifier for the Iris dataset, focusing on simplicity and modularity for Machine Learning Operations (MLOps). The project is structured to guide you through the setup, training, evaluation, and deployment of the model.

## **Project Structure**

```plaintext
.
MLOps_Playground/Exercises/Exercise_1/
├── iris_classification/         # Project root directory
│   ├── README.md                # Documentation (you're reading this)
│   ├── iris_classification.py   # Main Python script for model training and evaluation
│   ├── requirements.txt         # Required Python libraries
│   └── iris_model.joblib        # Saved model (Optional: created after running the script)
```

---

## **Environment Setup**

1. Clone this repository:
   ```bash
   git clone https://github.com/iSPYadav01/MLOps_Playground.git
   cd MLOps_Playground
   ```

2. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```bash
     .\.venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. Upgrade pip and install the dependencies:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

5. If `requirements.txt` is not available, manually install the libraries:
   ```bash
   pip install pandas scikit-learn matplotlib joblib
   ```

---

## **Code Workflow**

### 1. Import Libraries
```python
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt
import joblib
```

### 2. Load the Iris Dataset
```python
iris = load_iris()
X = iris.data  # Features
y = iris.target  # Labels
```

### 3. Split Data into Training and Testing Sets
```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

### 4. Create and Train the Model
```python
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
```

### 5. Make Predictions
```python
y_pred = model.predict(X_test)
```

### 6. Evaluate the Model
```python
# Accuracy Score
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

# Detailed Classification Report
print("Classification Report:")
print(classification_report(y_test, y_pred))
```

### 7. Save and Load the Model
#### Save the Trained Model
```python
joblib.dump(model, 'iris_model.joblib')
```

#### Load the Saved Model (for later use)
```python
loaded_model = joblib.load('iris_model.joblib')
```

### 8. (Optional) Visualize Results
#### Plot a Confusion Matrix
```python
from sklearn.metrics import ConfusionMatrixDisplay

ConfusionMatrixDisplay.from_estimator(model, X_test, y_test, display_labels=iris.target_names)
plt.title("Confusion Matrix")
plt.show()
```

#### Feature Importance Visualization
```python
import seaborn as sns

feature_importances = model.feature_importances_
sns.barplot(x=feature_importances, y=iris.feature_names)
plt.title("Feature Importances")
plt.show()
```

---

## **Running the Code**

1. Save the provided code snippets in a Python file named `iris_classification.py`.
2. Open a terminal or command prompt in the project directory.
3. Run the script:
   ```bash
   python iris_classification.py
   ```

This script will train the model, evaluate its performance, and optionally save it for later use.

---

## **Requirements**
Here are the key libraries required for this project:

- Python >= 3.7
- pandas
- scikit-learn
- matplotlib
- joblib

Install them using:
```bash
pip install -r requirements.txt
```

---

## **Future Enhancements**

1. **Hyperparameter Tuning:** Use GridSearchCV or RandomizedSearchCV to optimize model parameters.
2. **Data Visualization:** Create confusion matrix plots, decision boundaries, or other insights to better understand results.
3. **MLOps Integration:** Automate model deployment pipelines using tools like Docker, Kubernetes, or CI/CD frameworks.
4. **Dataset Expansion:** Apply the Random Forest model to more complex datasets.

---

## **Contributing**

Contributions are welcome! If you'd like to suggest improvements, report bugs, or create pull requests, please feel free to contribute to [this repository](https://github.com/iSPYadav01/MLOps_Playground.git).

---

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
```