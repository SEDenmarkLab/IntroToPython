## Version Control, Git and Github commands

### What Is Version Control?

Version control is a system that records changes to a file or set of files over time so that you can recall specific versions later. It acts as an automated, highly reliable safety net for your codebase, recording not only what was changed, but who changed it, when, and why.

### Why Do You Need It?

* **Time Travel & Rollbacks:** If a recent update breaks your project, you can instantly revert back to a known stable version without manual file backups (main_v1_final_really_final.py).
* **Traceability & Account Management:** Every snapshot (commit) includes an author and a message explaining the rationale behind the change.
* **Concurrent Collaboration:** Multiple team members can work on different parts of the same project simultaneously. Version control manages merging and detects overlapping edits (merge conflicts).
* **Safe Experimentation:** Branches let you isolate feature development, exploratory testing, or bug fixes without risking your primary, production-ready code.

### Git vs. GitHub

**Git:** The distributed version control tool running locally on your computer. It tracks your files and project history offline.

**GitHub:** A cloud-based hosting platform for Git repositories. It provides remote storage, team collaboration tools (Pull Requests, Code Reviews, Issue Tracking), and CI/CD pipelines.

### Essential Git Commands

```Shell
# Initialize a new local Git repository in the current folder
git init

# Clone an existing remote repository to your local machine
git clone https://github.com/username/repository-name.git

# Check the status of modified, staged, or untracked files
git status

# Stage a specific file for the next commit ("git add" means to add to the what's called "staged area", any files at this area will be committed in the next commit)
git add main.py

# Stage all tracked and untracked changes in the project
git add .

# Record staged changes as a new snapshot in the local repository
git commit -m "Implement data preprocessing pipeline"

# Inspect the commit history
git log --oneline --graph --decorate

# List all local branches (current branch highlighted)
git branch

# Create and switch to a new feature branch
git switch -c feature/new-algorithm
# (Legacy alternative: git checkout -b feature/new-algorithm)

# Switch back to an existing branch
git switch main

# Merge changes from another branch into your current active branch
git merge feature/new-algorithm

# Delete a branch once merged
git branch -d feature/new-algorithm

# View line-by-line differences not yet staged
git diff

# Unstage a file without altering its contents on disk
git restore --staged main.py

# Discard uncommitted local modifications in a file
git restore main.py

# Temporarily stash uncommitted changes to switch tasks cleanly
git stash
git stash pop

# Link a local repository to a remote repository on GitHub
git remote add origin https://github.com/username/repository-name.git

# View configured remote connections
git remote -v

# Upload local commits on the current branch to GitHub (and set upstream tracking)
git push -u origin main

# Download and integrate changes from GitHub into your active local branch
# pull = fetch + merge
git pull origin main

# Download remote changes without automatically merging them
git fetch origin

# Push the branch to remote and set tracking
git push -u origin feature/model-training
```

### Essential Github CLI Commands

Remember that these are the commands that used to connect or do any operations between your local offline repository and the cloud remote repository**(these only works after downloading Github CLI, which is not required, but it is a very useful)**

```Shell


# Interactive PR creation (prompts for title, body, and reviewers in terminal)
gh pr create

# Fast single-line PR creation specifying title, description, and target branch
gh pr create --title "Add model training script" --body "Implements baseline training and logging." --base main

# Create a draft PR (prevents premature merges)
gh pr create --draft --title "WIP: Feature optimization"

# List open PRs for the current repository
gh pr list

# Filter PRs by author, label, or state
gh pr list --author "@me"
gh pr list --state closed

# View details, description, and conversation of a specific PR
gh pr view 12

# Open the PR directly in your default web browser
gh pr view 12 --web

# View code changes (diff) introduced by the PR
gh pr diff 12

# Check out a colleague's PR locally into a dedicated branch for testing
gh pr checkout 12

# Submit a code review: approve the PR
gh pr review 12 --approve -b "Implementation verified and benchmarks look solid."

# Submit a code review: request changes
gh pr review 12 --request-changes -b "Please address edge cases in input sanitization."

# Add an informational comment to a PR
gh pr comment 12 --body "Tested locally, runs as expected."

# Interactively merge a PR
gh pr merge 12

# Merge using squash-and-merge, automatically deleting the remote and local branch
gh pr merge 12 --squash --delete-branch

# Rebase and merge
gh pr merge 12 --rebase

# Close an abandoned PR without merging
gh pr close 12
```

### Understanding Key Concepts: Clone vs. Fork vs. Template vs. Branch vs. Pull Request

| **Feature / Question**                  | **Clone**                                                   | **Fork**                                                                   | **Use Template**                                                            | **Branch**                                                                      | **Pull Request**                                   |
| --------------------------------------------- | ----------------------------------------------------------------- | -------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **Where Does the Result Live?**         | Your local machine                                                | Your remote GitHub account                                                       | Your remote GitHub account                                                        | Local machine and/or the remote repository                                            | *N/A (action / proposal, not a standalone copy)*       |
| **Retains Full Git History?**           | **Yes**(clones entire commit graph)                         | **Yes**(full upstream commit graph)                                        | **No**(resets to a single initial commit)                                   | **Yes**(inherits all history up to the branching point)                         | References relevant branch commits                       |
| **Connected to Original Repo?**         | Yes (remote points to source URL as`origin`)                    | Yes (linked via GitHub upstream network)                                         | **No**(completely isolated new repository)                                  | **Yes**(exists directly inside the same repository)                             | Directly links a source branch to the target base branch |
| **Can You Open a PR Back to Original?** | **Not directly**(requires pushing a branch somewhere first) | **Yes (Cross-Repo PR)**(standard workflow when you lack write access)      | **No**(treated as a totally separate project with unrelated histories)      | **Yes (Internal PR)**(standard workflow when you have write access to the repo) | *This IS the Pull Request itself*                      |
| **Primary Use Case**                    | Download files locally to run, test, and write code.              | Safely customize code or prepare open-source contributions without write access. | Bootstrap a new standalone project using existing folder scaffolding and configs. | Isolate a new feature, experiment, or bug fix without affecting`main`.              | Submit reviewed code to be merged into a target branch.  |

### CLI vs. GUI (you can make your own choice)

While understanding CLI commands is essential for understanding how version control works, everyday development often does not require typing these commands by hand.

There are also a graphic interface buttons that you can interact with on VS Code and the Github website. For example, you can simply click a button to commit and push your code to synchronize it with the cloud repository on Github, you can also simply do the pull request by clicking the pull request button on the Github website. Therefore, you can use what makes your workflow fastest and most reliable.
