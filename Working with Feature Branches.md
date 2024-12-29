# Working with Feature Branches in Git

This guide covers how to create a feature branch, make changes, and then merge it back into the `main` branch using **Git** and **GitHub**. It is designed for beginners and follows the steps to successfully create and work on your feature in isolation.

## Step 1: Clone the Repository

Start by cloning the repository from GitHub to your local machine. If you don't have the repository cloned yet, use the following command:

```bash
git clone https://github.com/iSPYadav01/MLOps_Playground.git
```

This command creates a local copy of your GitHub repository.

## Step 2: Navigate to the Repository Directory

After cloning, navigate into the project directory:

```bash
cd MLOps_Playground
```

Now you're inside the project folder, ready to work.

## Step 3: Check the Current Branch

It’s important to make sure you are on the `main` branch (or master) initially. You can check the current branch by running:

```bash
git branch
```

By default, you’ll be on the `main` branch.

## Step 4: Create a New Feature Branch

Create a new branch to isolate your feature changes. For example, to create a branch called `Dev_Branch_iSPYadav01`, use the following command:

```bash
git checkout -b Dev_Branch_iSPYadav01
```

This command both creates and switches you to the `Dev_Branch_iSPYadav01` branch.

## Step 5: Stage the Changes

Once you've made your modifications, stage them for commit:

To stage a single file, use:

```bash
git add newfile.txt
```

Alternatively, stage all changes in the directory:

```bash
git add .
```

## Step 6: Commit the Changes

Now that the changes are staged, commit them locally with a meaningful message describing the update:

```bash
git commit -m "Working with Feature Branches.md"
```

## Step 7: Push the Feature Branch to GitHub

After committing, push your new feature branch to GitHub:

```bash
git push origin Dev_Branch_iSPYadav01
```

This command pushes your `Dev_Branch_iSPYadav01` branch to the remote repository on GitHub.

## Step 8: Create a Pull Request (PR)

Once the feature branch is pushed, go to the **GitHub repository**:

1. Click on the **Pull Requests** tab.
2. Click **New Pull Request**.
3. Select `Dev_Branch_iSPYadav01` as the source branch and `main` as the target branch.
4. Add a description of the changes made and submit the pull request.

## for ADMIN

## Step 9: Merge the Pull Request (PR) 

After reviewing the changes (and once the PR is approved), you can merge the PR into the `main` branch. On GitHub, you'll have an option to merge the PR.

Once merged, you can delete the feature branch if no longer required.

## Git Command Summary

Here is a quick summary of the most useful Git commands used in the feature branch workflow:

| Command                                | Description                                          |
|----------------------------------------|------------------------------------------------------|
| `git clone <repo_url>`                 | Clone the repository to your local machine           |
| `git checkout -b <branch_name>`        | Create and switch to a new branch                    |
| `git add <file>`                       | Stage a specific file                                |
| `git add .`                            | Stage all changes in the working directory           |
| `git commit -m "<commit_message>"`     | Commit staged changes with a message                 |
| `git push origin <branch_name>`        | Push the feature branch to the remote repository     |
| `git branch`                           | View the current branch status                       |