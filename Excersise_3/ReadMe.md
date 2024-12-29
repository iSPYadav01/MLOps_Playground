# Exercise 3: DVC and Git Integration

Welcome to **Exercise 3** of the **MLOps Playground Repository**! In this exercise, you will learn how to integrate **Data Version Control (DVC)** with **Git** for efficiently managing datasets, training pipelines, and tracking experiments in machine learning projects. The exercise will also demonstrate how to integrate **WandB (Weights and Biases)** for experiment tracking, simulating ML pipeline execution, and monitoring real-time metrics.

---

## **Prerequisites**

Make sure you have the following tools installed on your local machine before starting Exercise 3:

1. **Python** (version 3.7 or above)
   - Install Python: [https://www.python.org/](https://www.python.org/)

2. **Git**  
   - Download and install Git: [https://git-scm.com/](https://git-scm.com/)

3. **Visual Studio Code (VS Code)**  
   - Install VS Code: [https://code.visualstudio.com/](https://code.visualstudio.com/)

4. **WandB Account** (Weights and Biases)  
   - Create a WandB account: [https://wandb.ai/](https://wandb.ai/)

5. **DVC (Data Version Control)**  
   - Install DVC: [https://dvc.org/doc/install](https://dvc.org/doc/install)

6. **Git LFS (Large File Support)**  
   - Install Git LFS: [https://git-lfs.github.com/](https://git-lfs.github.com/)

---

## **Repository Setup**

### **Step 1: Clone the Repository**

Clone the repository by running the following command:

```bash
git clone https://github.com/iSPYadav01/MLOps_Playground.git
cd MLOps_Playground/Exercise_3
```

### **Step 2: Open the Repository in VS Code**

1. Launch **Visual Studio Code**.
2. Open the folder `MLOps_Playground/Exercise_3` using **File > Open Folder**.
3. Open the integrated terminal in VS Code (`Ctrl + Backtick` or `Ctrl + ~`).

---

### **Step 3: Install Dependencies**

Install the required dependencies via pip:

```bash
pip install dvc wandb
```

Once the dependencies are installed, authenticate with WandB by running the following:

```bash
wandb login
```

- Follow the on-screen instructions to complete authentication.
- Paste your API key when prompted.

---

### **Step 4: Install and Configure Git LFS**

To track large files (like datasets) with Git LFS:

1. Install Git LFS by running:

   ```bash
   git lfs install
   ```

2. Configure Git LFS to track `.csv` files:

   ```bash
   git lfs track "*.csv"
   ```

3. Stage and commit changes:

   ```bash
   git add .gitattributes
   git commit -m "Configure Git LFS to track .csv files"
   git push origin main
   ```

---


### **Step 5: Initialize and Configure DVC**

1. Initialize DVC in the repository:

   ```bash
   dvc init
   ```

2. Track your datasets with DVC:

   ```bash
   dvc add data/sample.csv
   ```

3. Configure DVC to connect to remote storage:

   ```bash
   dvc remote add -d MLOps_Playground https://github.com/iSPYadav01/MLOps_Playground.git
   ```

4. Push the dataset to the remote storage:

   ```bash
   dvc push
   ```

---

## **Run Python Script for Experiment Tracking with WandB**

The following steps demonstrate how to run Python scripts that integrate **WandB** for experiment tracking.

### **Step 1: Open Python Script**

Navigate to the Python script (e.g., `mlops_script.py`) that simulates model training and logs metrics using **WandB**.

### **Step 2: Run the Script**

Execute the script in the terminal:

```bash
python mlops_script.py
```

This script will log metrics such as accuracy and loss in real-time and display the logs on your **WandB** dashboard.

Here’s an example of what the Python script might look like:

```python
import wandb
import random

# Initialize WandB
wandb.init(
    project="MLOps_Playground",
    config={
        "learning_rate": 0.02,
        "architecture": "CNN",
        "dataset": "CIFAR-100",
        "epochs": 10,
    },
)

# Simulate model training and log metrics
epochs = 10
offset = random.random() / 5
for epoch in range(2, epochs):
    acc = 1 - 2 ** -epoch - random.random() / epoch - offset
    loss = 2 ** -epoch + random.random() / epoch + offset

    # Log metrics to WandB
    wandb.log({"accuracy": acc, "loss": loss})

# Finish the WandB run
wandb.finish()
```

---

## **Using Git to Track Code Changes**

Git enables version control and collaboration for managing code.

### **Stage and Commit Changes**

To add and commit changes:

```bash
git add .
git commit -m "Update scripts"
```

### **Push Changes to GitHub**

After committing, push the changes to the remote GitHub repository:

```bash
git push origin main
```

---

## **Common DVC Commands**

- **Initialize DVC in the repository**:

  ```bash
  dvc init
  ```

- **Track a file with DVC**:

  ```bash
  dvc add <file_name>
  ```

  For example, adding `data/sample.csv`:

  ```bash
  dvc add data/sample.csv
  ```

- **Push data to remote storage**:

  ```bash
  dvc push
  ```

- **Pull data from remote storage**:

  To retrieve data from remote storage:

  ```bash
  dvc pull
  ```

- **Visualize DVC pipeline**:

  To view the pipeline, use:

  ```bash
  dvc pipeline show --ascii
  ```

---

## **Resources**

For additional help with DVC, Git, and WandB:

1. [DVC Documentation](https://dvc.org/doc)
2. [WandB Documentation](https://docs.wandb.ai/)
3. [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
4. [MLOps Concepts](https://mlops.community/)

---

## **License and Copyright**

This repository and associated content are licensed under the **MIT License**.

**Author**: S. Pratap Yadav  
- **GitHub**: [iSPYadav01](https://github.com/iSPYadav01)  
- **Portfolio**: [https://ispyadav01.github.io/Portfolio/](https://ispyadav01.github.io/Portfolio/)

Follow me on:
- [LinkedIn](https://www.linkedin.com/in/iSPYadav01)
- [Twitter](https://twitter.com/iSPYadav01)
- [GitHub](https://github.com/iSPYadav01)
- [Medium](https://medium.com/@ispyadav01)

© 2024 Data Dynasty Lab. All Rights Reserved.  
This project is available under the MIT License. Feel free to use, modify, and distribute with proper attribution.

---