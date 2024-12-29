# MLOps Playground Repository

Welcome to the **MLOps Playground** repository! This repository serves as an environment for practicing **Machine Learning Operations (MLOps)** principles. The goal is to explore various MLOps practices, focusing on workflows and tools that allow for seamless management and operationalization of machine learning models.

---

## Overview

The **MLOps Playground** repository provides a set of lab exercises aimed at simulating the real-world challenges and workflows encountered when working with machine learning in production. Each exercise is designed to deepen your understanding of the key aspects of MLOps, including:

- Data versioning and management
- Experiment tracking and visualization
- Model training and deployment pipelines
- Integration of tools like **WandB**, **DVC**, **Git**, and others into the ML lifecycle
- Collaboration in managing large-scale machine learning workflows

Each exercise is structured with clear goals, step-by-step instructions, and tools that help build the skills necessary to tackle production machine learning tasks. This repository prepares learners to integrate ML models into large and dynamic systems through continuous deployment and retraining.

---

## Prerequisites

Before starting the exercises in this repository, make sure you have the following tools installed:

- **Python 3.7 or higher**  
  You need Python installed on your system to run all code. Python can be downloaded from [python.org](https://www.python.org/).
  
- **Git**  
  Git is required for version control, which helps you track changes to the code throughout exercises. Download Git from [git-scm.com](https://git-scm.com/).
  
- **Visual Studio Code (VS Code)**  
  This text editor provides an integrated terminal for running the code and supporting extensions for better development experience. Install it from [Visual Studio Code](https://code.visualstudio.com/).

- **WandB (Weights and Biases) Account**  
  This service provides experiment tracking, enabling you to log metrics and visualize them in a dashboard. Create an account at [wandb.ai](https://wandb.ai/).

- **DVC (Data Version Control)**  
  DVC allows version control of datasets and models. Install it by following instructions available at [DVC Documentation](https://dvc.org/doc).

Ensure you have all prerequisites set up to avoid issues while executing the exercises.

---

## Repository Setup

Follow these steps to get your environment ready:

1. **Clone the Repository**  
   Use the Git command to clone the repository from GitHub to your local machine.

  Note:  create you own repo in github

```bash
git clone https://github.com/iSPYadav01/MLOps_Playground.git
```

2. **Open Repository in VS Code**  
   Open the repository using **Visual Studio Code**, and start exploring the code and files within.

To commit all the changes and push them to your remote repository, follow these steps:

2. 1. **Navigate to the project folder** if you're not already there:
   ```bash
   cd MLOps_Playground
   ```

2. 2. **Check the status** of your Git repository to see which files have been modified or added:
   ```bash
   git status
   
   or

   git status --porcelain
   ```

2. 3. **Add all changes** (including modified files and new files):
   ```bash
   git add .
   ```

2. 4. **Commit your changes** with a descriptive commit message:
   ```bash
   git commit -m "Updated README and setup instructions"
   ```

2. 5. **Push the changes** to your remote repository:
   ```bash
   git push origin main
   ```

This will commit all the updates (like your README file, scripts, and DVC configurations) and push them to your GitHub repository.

If you've never used `git lfs` to handle large files, don't forget to ensure they are properly managed:

```bash
git lfs push --all origin main
```

This command ensures that Git LFS handles large files, pushing them to your remote storage.


3. **Install Dependencies**  
   Inside the repository, there is a `requirements.txt` file. Run the `pip install` command to install the necessary libraries.

4. **Initialize DVC (If Needed)**  
   If you are working with DVC for versioning the datasets, initialize DVC and configure any remote storage settings.

---

## Exercise Execution

Each exercise aims to teach you different aspects of **MLOps**. Here's a summary of how exercises will proceed:

1. **WandB Experiment Tracking**  
   These exercises teach you how to log metrics such as loss, accuracy, and validation scores during model training. WandB allows you to track and visualize the performance of various models in a user-friendly web interface. By integrating it into your pipeline, you can track multiple experiment runs and identify optimal hyperparameters.
   
2. **DVC - Data Version Control**  
   You will learn how to use DVC to manage datasets in a versioned, collaborative manner. DVC allows you to track changes to your datasets, add new versions, and ensure that team members are on the same page in terms of dataset management. This is critical in an MLOps pipeline for maintaining dataset consistency across different stages of the model lifecycle.

3. **Model Training with DVC and WandB**  
   Combining DVC for data versioning and WandB for tracking experiment results ensures that your machine learning model can be reliably trained, tested, and monitored. These tools, when combined, give you the full spectrum of operational oversight, from dataset changes to real-time model performance monitoring.

---

## Version Control

Git is used for version control throughout this repository. You'll learn to use Git for tracking changes in scripts, notebooks, and project structure as you progress through exercises. Committing and pushing updates to your GitHub repository will be a fundamental skill demonstrated in every lab exercise.

---

## Experiment Tracking and Results

Experiment tracking is key to understanding how well your models are performing. With **WandB** integration, you'll monitor metrics such as:

- **Accuracy**
- **Loss**
- **F1 Score**
- **AUC**

For every training session, you’ll log performance statistics so that results can be visualized and compared easily in the WandB dashboard. These visualizations help you identify trends, compare different configurations, and facilitate faster iterations for model improvement.

---

## Work with Dev Branch
To create a feature branch named `Dev_Branch_iSPYadav01` and proceed with the steps as described, here’s what you need to do:

### 1. **Create a New Feature Branch**

Ensure you're on the `main` branch first, and then create and switch to your new feature branch:

```bash
git checkout main  # Ensure you're on the main branch
git pull origin main  # Pull the latest changes from the remote repository

git checkout -b Dev_Branch_iSPYadav01  # Create and switch to the feature branch
```

### 2. **Make Changes on the Feature Branch**

Make your desired changes to the `Excersise_1` and `Excersise_3` folders or any other updates you need.

### 3. **Stage the Changes**

After making your changes, stage them with:

```bash
git add .
```

### 4. **Commit the Changes**

Once the changes are staged, commit them:

```bash
git commit -m "Updated Excersise_1 and Excersise_3 folders in Dev_Branch_iSPYadav01"
```

### 5. **Push the Feature Branch to the Remote Repository**

Push your feature branch to GitHub:

```bash
git push origin Dev_Branch_iSPYadav01
```

### 6. **Create a Pull Request (PR) on GitHub**

1. Go to your repository on GitHub: [https://github.com/iSPYadav01/MLOps_Playground](https://github.com/iSPYadav01/MLOps_Playground).
2. A banner will appear asking you to create a pull request for the newly pushed branch. You can also go to the **Pull Requests** tab and click **New pull request**.
3. Set `main` as the base branch and `Dev_Branch_iSPYadav01` as the compare branch.
4. Add a title and description for the PR.
5. Click **Create pull request**.

### 7. **Review and Merge the PR**

After review (if necessary), merge the PR into the `main` branch. 

### 8. **Clean up (Optional)**
If the branch is no longer needed after the merge, delete it both locally and remotely:

Locally:

```bash
git branch -d Dev_Branch_iSPYadav01
```

Remotely:

```bash
git push origin --delete Dev_Branch_iSPYadav01
```


---
## License and Copyright

This repository and its contents are licensed under the **MIT License**. By using or modifying this repository, you agree to comply with the license terms and attribution rules outlined below.

**Author**: S. Pratap Yadav  
- **GitHub**: [iSPYadav01](https://github.com/iSPYadav01)  
- **Portfolio**: [https://ispyadav01.github.io/Portfolio/](https://ispyadav01.github.io/Portfolio/)

Follow me on:
- [LinkedIn](https://www.linkedin.com/in/iSPYadav01)
- [Twitter](https://twitter.com/iSPYadav01)
- [GitHub](https://github.com/iSPYadav01)
- [Medium](https://medium.com/@ispyadav01)

© 2024 Data Dynasty Lab. All Rights Reserved.

This project is made available under the MIT License. Feel free to use, modify, and distribute with proper attribution.
```