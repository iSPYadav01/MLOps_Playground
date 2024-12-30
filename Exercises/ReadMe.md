# MLOps Exercises Repository

Welcome to the **MLOps Exercises Repository**, a structured collection of exercises that demonstrate hands-on implementation of various MLOps principles, tools, and workflows.

This repository is maintained as part of the M.Tech. program in **Artificial Intelligence and Machine Learning (AIML)** at **BITS Pilani** (Work Integrated Learning Programmes).

**Author**: Surendra  
**GitHub Profile**: [iSPYadav01](https://github.com/iSPYadav01)  
**Portfolio**: [Surendra's Portfolio](https://ispyadav01.github.io/Portfolio/)

---

## Table of Contents

- [Introduction](#introduction)
- [Exercises Overview](#exercises-overview)
- [Repository Structure](#repository-structure)
- [Technologies and Tools](#technologies-and-tools)
- [How to Use This Repository](#how-to-use-this-repository)
- [Committing Changes with Git and DVC](#committing-changes-with-git-and-dvc)
- [License](#license)
- [Copyright](#copyright)

---

## Introduction

This repository organizes and documents the exercises designed to reinforce and test key MLOps concepts, such as model experimentation, deployment, versioning, and automation. Each exercise helps you build your skills in deploying and maintaining machine learning systems following MLOps best practices.

### Objectives

1. Strengthen your understanding of **data versioning**, **experiment tracking**, and **model deployment**.
2. Implement real-world **CI/CD** and **data pipelines** to automate model workflows.
3. Learn to use industry-standard tools for experimentation and deployment, including **DVC**, **MLflow**, **Docker**, **Kubernetes**, and **GitLab CI**.

---

## Exercises Overview

Here’s an overview of the exercises included in this repository:

| **Exercise**      | **Topic**                                      | **Status** |
|-------------------|------------------------------------------------|------------|
| **Exercise 1**        | **Exercise 1: Iris Flower Classification with Random Forest** <br> This exercise demonstrates the implementation of a Random Forest classifier for the Iris dataset, with a focus on simplicity and modularity. The goal is to guide you through the setup, training, evaluation, and deployment of the model in a modular, reproducible way. | ✅ Completed |
| **Exercise 2**        | **Iris Model Training and Deployment** <br> A step-by-step guide to training a Random Forest model using the Iris dataset, and deploying it as a prediction service with Flask and FastAPI. | ✅ Completed |
| **Exercise 3**        | **DVC and Git Integration** <br> This exercise shows how to integrate Data Version Control (DVC) with Git for efficiently managing datasets, tracking experiments, and controlling versions of machine learning models. | ✅ Completed |
| **Exercise 4**        | **Feature Store and Model Store Implementation** <br> A comprehensive guide to implementing a feature store using **Feast** and a model store using **MLflow**. It covers setup, configuration, and management of features and models for streamlining machine learning workflows. | ✅ Completed |


Status:
- ✅ Completed
- 🚧 In Progres
- ❌ Pending
- 🔴 Abandoned
---

---

## Repository Structure

The repository is organized as follows:

```
MLOps_Playground/Exercises/
├── Exercise_1/                                  # Exercise 1: Iris Flower Classification with Random Forest
│   ├── README.md                                # Documentation for Exercise 1
│   └── iris_classification/                     # Project root directory
├── Exercise_2/                                  # Exercise 2: Iris Model Training and Deployment
│   ├── README.md                                # Documentation for Exercise 2
│   └── iris_app_deploy/                         # Project root directory
├── Exercise_3/                                  # Exercise 3: DVC and Git Integration
│   ├── README.md                                # Documentation for Exercise 3
│   └── ...                                      # Additional directories for Exercise 3
├── Exercise_4/                                  # Exercise 4: Feature Store and Model Store Implementation
│   ├── README.md                                # Documentation for Exercise 4
│   └── ...                                      # Additional directories for Exercise 4
└── README.md                                    # Main documentation file (this file)
```

Each exercise follows a modular structure, consisting of:
- **README.md**: Documentation with detailed instructions for the exercise.
- **Source Code**: Implementations for the tasks, often found in the `src/` directory.
- **Data**: Datasets used for training, typically in a `data/` folder.
- **Models**: Saved models and their outputs, typically stored in a `models/` directory.

---

## Technologies and Tools

The exercises use a variety of tools for different MLOps tasks. Below is a list of tools categorized by their usage:

| **Category**             | **Tools Used**                             |
|--------------------------|--------------------------------------------|
| **CI/CD**                | GitHub Actions, GitLab CI, Jenkins        |
| **Experiment Tracking**  | MLflow, DVC                               |
| **Data Versioning**      | DVC                                        |
| **Model Packaging**      | Docker, Flask                              |
| **Model Deployment & Orchestration** | Kubernetes (Helm, GKE, AKS)          |
| **Version Control**      | Git and GitHub                             |

These tools help create efficient, reproducible, and scalable pipelines for the MLOps lifecycle.

---
## Prerequisites

Before you start using this repository, ensure that you have the following tools installed:

### 1. **Python 3.7+**  
Install Python from the official [Python website](https://www.python.org/).

### 2. **Git**  
You will need **Git** for version control. Install it from [Git](https://git-scm.com/).

### 3. **Visual Studio Code (VS Code)**  
VS Code is a popular code editor that supports integrated terminal functionality and necessary extensions for ML development. Install it from [VS Code](https://code.visualstudio.com/).

### 4. **WandB (Weights and Biases)**  
For experiment tracking, logging, and visualizing metrics such as loss, accuracy, etc., sign up for a **WandB** account at [wandb.ai](https://wandb.ai/).

### 5. **DVC (Data Version Control)**  
DVC allows you to manage and version datasets and models. You can find installation instructions on the official [DVC Documentation](https://dvc.org/doc).

---

## Repository Setup

To set up the project and environment, follow these instructions:

### 1. Clone the Repository

To clone this repository, use the following command:

```bash
git clone https://github.com/iSPYadav01/MLOps_Playground.git
```

> **Tip:** You can create your own copy of this repository if needed.

### 2. Navigate to the Project Folder

Once cloned, go to your project directory:

```bash
cd MLOps_Playground
```

### 3. Open Repository in VS Code

Open your repository in **Visual Studio Code** to start working with the code:

```bash
code .
```

### 4. Switch to the Dev Branch

It's important to work on a feature branch. Follow these commands:

1. First, ensure you are on the `main` branch and pull the latest updates:

    ```bash
    git checkout main
    git pull origin main
    ```

2. Next, create and switch to your **feature branch**:

    ```bash
    git checkout -b Dev_Branch_iSPYadav01
    ```

### 5. Install Required Dependencies

Run this command to install all necessary Python dependencies:

```bash
pip install -r requirements.txt
```

If you're working with **DVC** for dataset versioning, follow the [DVC setup guide](https://dvc.org/doc) for initialization and remote storage configuration.

---

## Working with Git and DVC

Follow these steps to commit and manage your changes in **Git** and **DVC**:

### 1. Check the Status of Your Changes

To view which files have changed or been added, use:

```bash
git status
```

### 2. Stage the Changes

Once you've modified or added files, stage them for commit:

```bash
git add .
```

### 3. Commit the Changes

After staging the changes, commit them with a detailed message:

```bash
git commit -m "Updated [specific files/folders] for Exercise [X]"
```

### 4. Push Changes to the Feature Branch

To push your changes to your feature branch on GitHub:

```bash
git push origin Dev_Branch_iSPYadav01
```

---

## Create a Pull Request (PR)

After pushing your feature branch, you can create a pull request on GitHub. Follow these steps:

1. Go to the **Pull Requests** section of your GitHub repository.
2. Click **New pull request**.
3. Set the **base branch** to `main` and the **compare branch** to `Dev_Branch_iSPYadav01`.
4. Write a descriptive title and detailed message about the changes you made.
5. Click **Create pull request** to submit it for review.

---

## Merging and Cleanup

Once the pull request is reviewed and merged, you can delete the feature branch.

### Delete the Feature Branch (Locally and Remotely)

1. Locally delete the branch:

    ```bash
    git branch -d Dev_Branch_iSPYadav01
    ```

2. Remotely delete the branch:

    ```bash
    git push origin --delete Dev_Branch_iSPYadav01
    ```

---

## License and Copyright
All rights reserved.  
This project is intended for academic and educational purposes as part of the **M.Tech.** program at **BITS Pilani**. Redistribution or commercial use without permission is prohibited. For inquiries or permissions, please contact the author via email or GitHub.

**Author:** S. Pratap Yadav  
- **GitHub**: [iSPYadav01](https://github.com/iSPYadav01)  
- **Portfolio**: [Portfolio](https://ispyadav01.github.io/Portfolio/)

You can follow me on:
- [LinkedIn](https://www.linkedin.com/in/iSPYadav01)
- [Twitter](https://twitter.com/iSPYadav01)
- [Medium](https://medium.com/@ispyadav01)

© 2024 Data Dynasty Lab. All Rights Reserved.  
Distributed under the MIT License.
```