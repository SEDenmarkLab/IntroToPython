## Conda commands and creating your first conda environment

### What is Conda？

Conda is an open-source, cross-language package management and environment management system. Miniconda is a lightweight, minimal installer for Conda. It ships only with Conda, Python, and a handful of essential system packages, allowing you to install only what you need. Unlike standard tools such as pip (which only manages Python packages), Conda can manage packages and dependencies across multiple languages, including Python, C/C++, and R.

### Why Do We Use Conda?

**1. Isolated Environments:** Imagine you are working on different projects and you need different environment for different projects. For example, you might need the numpy package when you are doing Python array calculations, but you might not need it if you're not doing any calculations; or if you are programming in another programming language like C++, you might not need any Python packages in your environment for that project. So conda allow developers to create a unique environment for each specific project that they are working on. Different projects often demand conflicting package versions. Conda allows you to partition your machine into clean, self-contained "rooms" (virtual environments). A change in one room never damages another.

**2. Binary Dependency Resolution:** Many scientific libraries (e.g., NumPy, RDKit, OpenBabel) rely on low-level, pre-compiled C/C++ libraries. pip frequently fails to build these on local machines lacking pre-installed C++ compilers, whereas Conda downloads pre-compiled binaries directly.

**3. No Root Privileges Required:** You can install tools and change versions inside a Conda environment without needing system administrative (sudo) privileges.

### Common Conda Commands

#### Environment Management

**List all environments**

```Shell
conda env list
# or
conda info --envs
```

(The asterisk * *indicates your currently active environment.)*

**Activate an environment:**

```Shell
conda activate <env_name>
```

**Deactivate the current environment:**

```Shell
conda deactivate
```

**Remove an environment completely:**

```Shell
conda remove -n <env_name> --all
```

#### Package Management

**List packages installed in the active environment:**

```Shell
conda list
```

**Install a package:**

```Shell
conda install <package_name>
```

**Install from a specific channel (e.g., conda-forge):**

```Shell
conda install -c conda-forge <package_name>
```

**Update a package:**

```Shell
conda update <package_name>
```

**Uninstall a package:**

```Shell
conda remove <package_name>
```

#### Configuration Tips

Usually after you installed miniconda to your device, you will be automatically placed at the "(base)" conda environment whenever you turn on the terminal, indicating that conda is now activated, which you are not in any specific environment created by yourself, you are just in the root environment. You could download packages in the base environment, but it's not recommended to do so because you should create a specific environment for your project. So what if you don't want conda to be activated when you turn on the terminal? What if you only want to be in the original terminal of your device, just like what you have before you install miniconda. Here are the steps that you can do:

**Disable auto-activating the base environment upon opening a shell(Conda will not be automatically activated when you open your terminal):**

```Shell
conda config --set auto_activate_base false
```

If you do this, you would have to run:

```Shell
conda activate <env_name> #to go directly into your specific environment
```

Or you can do:

```Shell
conda activate
#go into the base conda environment first
conda activate <env_name>
#and then go to your specific environment
```

**Re-enable auto-activating base(if you want the automatic activation to be turned on again):**

```Shell
conda config --set auto_activate_base true
```

### Creating Your First Conda Environment

Now we are going to create the first environment specifically for this exercise, probably also an environment that you can use for future work in the lab.

#### Step 1: Create a Clean Environment

Open your terminal (macOS/Linux) or Anaconda Prompt (Windows) and create a new environment named chemo_env running Python 3.10:

```Shell
conda create -n chemo_env python=3.10 -y
```

I named the environment "chemo_env", however, you can name it whatever you want. "-y" simply means to automatically answer "yes" after this command, if you don't add -y, it would ask you "Proceed ([y]/n)?" Then you can press y to confirm, so it's totally OK if you don't add -y in the command. I choose Python 3.10 as my Python version, you can choose whatever version you want, just don't be too outdated.

### Step 2: Activate the Environment

Enter the isolated workspace:

```Shell
conda activate chemo_env
```

The prefix of the shell prompt will be changed to (chemo_env)

### Step 3: Install Heavy Scientific & Chemoinformatics Libraries via Conda

Libraries containing compiled C/C++ binaries—especially openbabel and rdkit must be installed using "conda install" rather than "pip" to avoid missing dynamic linked libraries or compilation errors. We use the community-maintained "conda-forge" channel:

```Shell
conda install -c conda-forge openpyxl rdkit openbabel pandas numpy matplotlib seaborn ipykernel jupyter notebook -y
```

### Step 4: Install Pure Python & Specialized Packages via Pip

Packages like molli (molecular manipulation toolkit) and py3DMol (WebGL-based molecular visualization) are primarily distributed via PyPI. Install them inside the active environment:

```Shell
pip install molli py3Dmol
```
