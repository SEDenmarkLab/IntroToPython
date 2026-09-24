

# General Environment setup (installation)

This document will focus on the general installations and account creation on your machine.

### 1. Create a GitHub account

Github is where developers upload there code and repositories to the cloud/internet to keep track of their progess. While Git tracks code changes locally on your machine, GitHub acts as the remote hub where code is backed up, shared, and collaborated on with others.

1. Navigate your browser to [github.com](https://github.com/)
2. follow their steps to signup.

### 2. Installing Git

Git is a distributed version control system running locally on your computer. It snapshots project files over time, allowing you to branch off experiments, track historical revisions, and revert mistakes without losing work.

#### macOS

1. Open the Terminal application
2. Run the command:

```Shell
xcode-select --install
```

3. If system prompt will appear asking to install "command line developer tools." Click Install and accept the license agreement.

For more, reference to [git-scm.com/install/mac](https://git-scm.com/install/mac)

#### Windows

#### * Go to [git-scm.com/install/windows](https://git-scm.com/install/windows)
* follow their steps to install.

#### Linux

1. Go to [git-scm.com/install/linux](https://git-scm.com/install/linux)
2. follow their steps to install

Go to [git-scm.com/install](https://git-scm.com/install/) for reference


#### Verification

After installing, run the following command in your terminal:

```Shell
git --version
```

If you see the version printed out, you are all set. (something like git version 2.x.x)


### 3. Installing VS Code and Login with Github

VS Code is a lightweight, cross-platform source code editor/Integrated Development Environment(IDE) built by Microsoft. It features built-in Git tooling, integrated terminals, debugging support, and an ecosystem of extensions for virtually any programming language. ([code.visualstudio.com](https://code.visualstudio.com/))


#### macOS

1. Go to [code.visualstudio.com/docs/setup/mac](https://code.visualstudio.com/docs/setup/mac)
2. follow their steps to install
3. Usually, they will lead you to [code.visualstudio.com/download](https://code.visualstudio.com/download)



#### Windows

1. Go to [code.visualstudio.com/docs/setup/windows](https://code.visualstudio.com/docs/setup/windows)
2. follow their steps to install
3. Usually, they will lead you to [code.visualstudio.com/download](https://code.visualstudio.com/download)


#### Linux

1. Go to [code.visualstudio.com/docs/setup/linux](https://code.visualstudio.com/docs/setup/linux)
2. follow their steps to install
3. Usually, they will lead you to [code.visualstudio.com/download](https://code.visualstudio.com/download)


#### Login using your Github account

1. After the VS Code application is successfully installed you will now launch the application.
2. In the bottom left corner, there will be an "Account" icon.
3. Click on that icon and choose "Sign in with GitHub".
4. Follow rest of the steps they provided


#### Downloading some VS Code extensions

1. Navigate to the extension category located at the side bar to the left.
2. Search for "Python"(provide you with some Python debuggers), "Jupyter"(allow you to use Jupyter notebook in VS code), "autoDocstring - Python Docstring Generator"(generate Docstring templates) extension packs. Note: The Jupyter notebook here it's quite important because this entire exercise template files(ends in .ipynb) are based upon this package, this package allows you to execute your Python code by different separate blocks. However, you might wonder the reason why unit one is not using Jupyter notebook, this is actually because you will be learning how to do imports, and you cannot import a .ipynb file to another file. You could only do it with a native python file. However, you could import other native Python files to a .ipynb file, as you will see you later.
3. Download these them sequentially



### 4. Installing Miniconda (future guidance on what that is and how to use it will be on Unit 0.3)

Miniconda is a minimal, lightweight distribution of Conda that includes only Python, Conda package manager, and a few core dependencies. It lets you create isolated virtual environments with specific Python versions and native C/C++ libraries, preventing project dependency conflicts and keeping your base operating system clean.

1. Go to [www.anaconda.com/download/success](https://www.anaconda.com/download/success)
2. Choose your system and download Miniconda(Do not choose Anaconda if you really need it for yourself, Miniconda will be enough for this exercise at the future work in the lab, Anaconda is too bulky with too many things that we are not going to use)

#### Verification

To verify that you have installed conda successfully, run the following in your terminal:

```Shell
conda --version
```

Expected output: conda 24.x.x (or later).

Or, you can also check if your command prompt prefix has a "(base)" at the front

```Shell
#if this was the original:
[user@localHost] ~ %
#after installing conda, it would be like this:
(base) [user@localHost] ~ %
```
