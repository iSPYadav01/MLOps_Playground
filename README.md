# 🎓 MLOps Playground Repository 🚀

Welcome to the **MLOps Playground**! This repository serves as your virtual **lab** for diving deep into **Machine Learning Operations (MLOps)**. Whether you are just starting or looking to enhance your skills, this repo offers a comprehensive set of **hands-on exercises**, **real-world challenges**, and powerful tools to get you familiar with ML in production environments.

🌟 **MLOps Playground** is structured to help you build a strong foundation in MLOps principles, leveraging cutting-edge tools to automate and streamline every step of the machine learning pipeline.

---

## 📚 **Repository Overview**

The **MLOps Playground** repository is split into two core sections:

- **Assignments** 📝: Introduction to key MLOps concepts, guiding you through foundational tasks.
- **Exercises** 🔧: Real-world tasks where you'll tackle advanced scenarios like **version control**, **experiment tracking**, and **model deployment**.

The main goal is to prepare you for building machine learning workflows and systems in production through **continuous model retraining** and **deployment**.

---

## 🔧 **Tools and Technologies**

The exercises and assignments use several tools crucial for MLOps pipelines:

- **Python (>= 3.7)**: Core language for building and managing your ML workflows.
- **Git**: For version control, to track your code changes.
- **WandB** (Weights and Biases): Track your experiments and visualize metrics easily.
- **DVC** (Data Version Control): Version control for large datasets and models.
- **Git LFS**: For handling large files with Git.

Make sure you have the tools listed in the prerequisites installed and configured.

---

## 🚀 **Getting Started**

### 1. **Clone the Repository**:
To begin, clone the repo to your local machine. Make sure you have **Git** installed.

```bash
git clone https://github.com/iSPYadav01/MLOps_Playground.git
```

### 2. **Navigate to Your Local Repo**:
Use the following commands to enter the project directory:

```bash
cd MLOps_Playground
```

### 3. **Install Dependencies**:
To install the necessary libraries, run the following command:

```bash
pip install -r requirements.txt
```

### 4. **Initialize DVC** (For DVC tasks):
If you will be working with DVC for data versioning, initialize it with the following command:

```bash
dvc init
```

---

## 🛠️ **Create and Work on Your Own Branch**

We use a **Git workflow** with feature branches for each task. Here’s how you can get started on your own branch:

### 1. **Create a New Feature Branch**:
To create and switch to a feature branch, run:

```bash
git checkout main  # Make sure you are on the main branch
git pull origin main  # Pull the latest changes
git checkout -b Dev_Branch_iSPYadav01  # Create and switch to your feature branch
```

### 2. **Make Changes & Commit**:
Make your updates for the exercises or assignments. Afterward, commit your changes with:

```bash
git add .  # Stage changes
git commit -m "Updated Exercise1 and Exercise2 folders"  # Commit with a message
```

### 3. **Push to Remote**:
Once changes are committed, push them to your forked repo on GitHub:

```bash
git push origin Dev_Branch_iSPYadav01
```

### 4. **Create a Pull Request (PR)**:
Go to GitHub → Click on **New Pull Request** → Select `Dev_Branch_iSPYadav01` → Submit your PR.

---

## 📑 **Folder Structure**

Here’s how the repository is structured:

```
MLOps_Playground/
├── Assignments/           # Contains lab tasks for MLOps basics
│   ├── Assignment1/
│   ├── Assignment2/
│   └── Assignment3/
├── Exercises/             # Advanced MLOps challenges
│   ├── Exercise1/
│   ├── Exercise2/
│   ├── Exercise3/
│   └── Exercise4/
├── requirements.txt       # Python dependencies
├── README.md              # Main repository information
└── .dvc/                  # DVC config and data versioning files
```

## 📜 **License & Acknowledgments**

This repository is licensed under the **MIT License**. You can use, modify, and distribute it under this license.

- **Author**: S. Pratap Yadav
  - **GitHub**: [iSPYadav01](https://github.com/iSPYadav01)
  - **Portfolio**: [S. Pratap Yadav Portfolio](https://ispyadav01.github.io/Portfolio/)

Follow me on:
- [LinkedIn](https://www.linkedin.com/in/iSPYadav01)
- [Twitter](https://twitter.com/iSPYadav01)

© 2024 Data Dynasty Lab. All Rights Reserved.
```