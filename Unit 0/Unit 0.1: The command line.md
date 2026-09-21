# The command line

Before we get into the general set up,  we are going to go over several useful commands that helps you to interact with your device through the terminal window.  The Command Line Interface (CLI) is a text-based bridge between you and your operating system/device. Usually, we will interact with graphical interface on our device to perform several actions that we want our device to do, such as clicking the folder icon to get into a specific folder. However, when it comes to coding, instead of navigating with a mouse through a Graphical User Interface (GUI), you type structured instructions to inspect files, execute scripts, and configure machines with speed and precision.

### Why Learn the Command Line?

* Speed and Efficiency: Repetitive administrative tasks, bulk renaming, or file searches take seconds with short, composable commands.
* Access to Headless Systems: Remote servers, cloud virtual machines, and Docker containers do not run graphical desktops; shell access via SSH is the universal standard.
* Automation and Scripting: CLI commands chain directly into shell scripts (.sh), enabling reproducible workflows, automated builds, and data processing pipelines.
* Developer Tooling Ecosystem: Core development utilities such as Git, package managers (npm, pip), compilers (gcc, clang), and system monitors are built CLI-first.

### Core Anatomy of a Command

Every shell instruction follows a consistent syntax structure:

```Shell
[user@localHost] ~ % command -flags arguments
```

The user name is "user"

The host name is "localHost"

Current working directory is "~" (user's home directory)

% is the cursor, you might also see $ in Windows system

command: The executable program (e.g., ls, grep, mkdir).

Flags / Options: Modifiers (prefixed with - or --) altering behavior (e.g., -l, --all).

Arguments: The target operated on, such as file paths, numbers, or search patterns.

### 1. Directory Navigation and Orientation

| **Command** | **Description**   | **Common Usage** |
| ----------------- | ----------------------- | ---------------------- |
| `pwd`           | Print working directory | `pwd`                |
| `ls`            | List directory contents | `ls -la`             |
| `cd`            | Change directory        | `cd projects/`       |

### Concrete Examples

Check your absolute path:

```Shell
[user@localHost] ~/workspace % pwd
Output: /home/user/workspace
```

List all files, including hidden ones (`.` files), with detailed metadata (permissions, owner, byte size, modification timestamp):

```Shell
[user@localHost] ~/workspace % ls -la
```

Move up one directory level, return home, or jump back to the previous folder:

```Shell
[user@localHost] ~/workspace % cd ..      #Move up to parent directory
[user@localHost] ~/workspace % cd ~       #Jump to user home directory
[user@localHost] ~/workspace % cd -       #Switch back to previous directory
```

#### 2. File and Directory Management

| **Command** | **Description**                    | **Common Usage**         |
| ----------------- | ---------------------------------------- | ------------------------------ |
| `touch`         | Create an empty file or update timestamp | `touch main.cpp`             |
| `mkdir`         | Make a new directory                     | `mkdir -p src/utils`         |
| `cp`            | Copy files or directories                | `cp -r src/ backup/`         |
| `mv`            | Move or rename files                     | `mv script.py old_script.py` |
| `rm`            | Remove files or directories              | `rm -rf build/`              |

### Concrete Examples

Create nested directories without throwing missing-parent errors:

```Shell
[user@localHost] ~/workspace % mkdir -p data/raw/2026
```

Copy a directory recursively:

```Shell
[user@localHost] ~/workspace % cp -r experiments/ experiments_backup/
```

Rename or move a file:

```Shell
[user@localHost] ~/workspace % mv config.temp.json config.json
```

Permanently remove a directory and all nested contents:

```Shell
[user@localHost] ~/workspace % rm -rf temp_trash/
```

> **Warning:** `rm -rf` bypasses the trash bin. Deleted items cannot be restored via the OS desktop trash.

#### 3. Inspecting and Reading Files

| **Command** | **Description**                      | **Common Usage**     |
| ----------------- | ------------------------------------------ | -------------------------- |
| `cat`           | Concatenate and print entire file contents | `cat settings.yaml`      |
| `less`          | Interactive, scrollable terminal pager     | `less server.log`        |
| `head`          | Display first**$N$**lines                | `head -n 20 dataset.csv` |
| `tail`          | Display last**$N$**lines                 | `tail -f app.log`        |

### Concrete Examples

Monitor active log output live as data appends:

```Shell
[user@localHost] ~ % tail -f production.log
```

Inspect only the header row and top 5 rows of a tabular dataset:

```Shell
[user@localHost] ~ % head -n 6 measurements.csv
```

#### 4. Searching and Pattern Matching

| **Command** | **Description**                       | **Common Usage**  |
| ----------------- | ------------------------------------------- | ----------------------- |
| `grep`          | Search text for string patterns using regex | `grep -rn "TODO" .`   |
| `find`          | Search filesystem for files by name/type    | `find . -name "*.py"` |

### Concrete Examples

Search recursively through all subdirectories (`-r`), printing matching line numbers (`-n`) and ignoring case (`-i`):

```Shell
[user@localHost] ~ % grep -rni "connection_timeout" ./src
```

Find all `.log` files modified within the last 7 days:

```Shell
[user@localHost] ~ % find /var/log -name "*.log" -mtime -7
```

#### 5. Streams, Redirection, and Pipe

Unix-like shells operate on three default I/O streams:  **Standard Input (stdin)** ,  **Standard Output (stdout)** , and  **Standard Error (stderr)** .

| **Operator** | **Action**                                | **Example**                       |
| ------------------ | ----------------------------------------------- | --------------------------------------- |
| `>`              | Redirect stdout to file (overwrite)             | `echo "token=123" > .env`             |
| `>>`             | Redirect stdout to file (append)                | `echo "2026-09-14: OK" >> status.log` |
| `<`              | Read input from file into stdin                 | `sort < raw_names.txt`                |
| `\|`(Pipe)        | Pass stdout of first command as stdin to second | `cat logs.txt \| grep "ERROR" \| wc -l` |

### Concrete Examples

Find and count how many failed login events occurred:

```Shell
[user@localHost] ~ % cat auth.log | grep "Failed password" | wc -l
```

Sort an unsorted file and strip duplicates into a clean target file:

```Shell
[user@localHost] ~ % sort -u raw_ids.txt > unique_ids.txt
```

#### 6. Process Monitoring and System Diagnostics

| **Command** | **Description**                   | **Common Usage**   |
| ----------------- | --------------------------------------- | ------------------------ |
| `top`/`htop`  | Interactive real-time process viewer    | `top`                  |
| `ps`            | Snapshot of current running processes   | `ps aux \| grep python` |
| `kill`          | Terminate a process by Process ID (PID) | `kill -9 14820`        |
| `df`            | Disk space usage by filesystem          | `df -h`                |
| `du`            | Disk usage by directory/file            | `du -sh *`             |

### Concrete Examples

Inspect high-memory processes and cleanly terminate an unresponsive instance:

```Shell
[user@localHost] ~ % ps aux | grep python
#show pid
[user@localHost] ~ % kill -15 24511     # Sends SIGTERM for graceful exit
[user@localHost] ~ % kill -9 24511      # Sends SIGKILL for immediate termination
```

Audit storage usage in human-readable sizes (`GB`, `MB`):

```Shell
[user@localHost] ~ % du -sh ./models/*
```

#### 7. Permissions and Ownership

Unix file permissions assign Read (`r`), Write (`w`), and Execute (`x`) rights across three categories:  **User (Owner)** ,  **Group** , and  **Others** .

| **Permission** | **Meaning** | **Binary** | **Value** |
| -------------------- | ----------------- | ---------------- | --------------- |
| **`r`**      | Read              | `100`          | **4**     |
| **`w`**      | Write             | `010`          | **2**     |
| **`x`**      | Execute           | `001`          | **1**     |
| **`-`**      | No permission     | `000`          | **0**     |

Numeric Mode (Absolute Permissions)

```Shell
# Set exact permissions: Owner gets 7 (rwx), Group gets 5 (r-x), Others get 4 (r--)
[user@localHost] ~ % chmod 754 run_pipeline.sh

# Standard executable script: Owner has full control, everyone else can read and run
[user@localHost] ~ % chmod 755 build.sh

# Standard configuration/source file: Owner can read/write, everyone else read-only
[user@localHost] ~ % chmod 644 config.json

# Highly restricted secret: Only owner can read/write; Group and Others have zero access
[user@localHost] ~ % chmod 600 ~/.ssh/id_ed25519
```

Symbolic Mode (Relative Permissions)

```Shell
# Add execute (+x) permission for all users without changing read/write rights
[user@localHost] ~ % chmod +x deploy.sh

# Grant write (+w) permission only to the file owner (u = user)
[user@localHost] ~ % chmod u+w main.cpp

# Revoke write (-w) permission from group (g) and others (o)
[user@localHost] ~ % chmod go-w notes.txt
```

| **Command** | **Description**          | **Common Usage**         |
| ----------------- | ------------------------------ | ------------------------------ |
| `chmod`         | Modify file mode / permissions | `chmod +x deploy.sh`         |
| `chown`         | Change file owner and group    | `sudo chown user:group file` |

### Concrete Examples

Make a script directly executable:

```
[user@localHost] ~ % chmod +x run_analysis.sh
./run_analysis.sh
```

Set standard restrictive permissions on private SSH keys:

```
[user@localHost] ~ % chmod 600 ~/.ssh/id_ed25519
```

#### 8. Remote Access and Networking

| **Command** | **Description**                              | **Common Usage**                                                   |
| ----------------- | -------------------------------------------------- | ------------------------------------------------------------------------ |
| `ssh`           | Secure Shell: Connect to a remote host securely    | `ssh user@host`                                                        |
| `scp`           | Secure Copy: Transfer files over an SSH tunnel     | `scp file.txt user@host:path/`                                         |
| `rsync`         | Efficient, differential remote and local file sync | `rsync -avz src/ user@host:dest/`                                      |
| `curl`          | Transfer data to/from servers via HTTP/HTTPS/FTP   | `curl -O [https://example.com/data.csv](https://example.com/data.csv)` |
| `ping`          | Test network reachability and latency to a host    | `ping google.com`                                                      |

### Concrete Examples

Connect to a remote server using a custom port or specific private key:

```Shell
[user@localHost] ~ % ssh -p 2222 username@remote.server.com
[user@localHost] ~ % ssh -i ~/.ssh/id_ed25519 username@remote.server.com
```

Upload a local file or download a remote directory recursively:

```Shell
[user@localHost] ~ % scp dataset.csv username@remote.server.com:~/data/
[user@localHost] ~ % scp -r username@remote.server.com:~/results/ ./local_results/
```

Synchronize directories incrementally with compression and progress tracking:

```Shell
[user@localHost] ~ % rsync -avzP ./src/ username@remote.server.com:~/project/
```

Download a file directly or inspect HTTP response headers:

```Shell
[user@localHost] ~ % curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
[user@localHost] ~ % curl -I https://api.github.com
```

Send 4 packets to test server latency and packet loss:

```Shell
[user@localHost] ~ % ping -c 4 8.8.8.8
```

### Directory symbols

You might be confused about what is "~", "..", "./", etc when you cd into different folders, and these are actually just symbols for folders. There is nothing more than that.

| **Symbol**  | **Name**              | **Meaning**                                                                      | **Equivalent**                             | **Example Command** |
| ----------------- | --------------------------- | -------------------------------------------------------------------------------------- | ------------------------------------------------ | ------------------------- |
| `/`             | **Root Directory**    | The topmost level of the entire filesystem hierarchy (the root of the directory tree). | Similar to`C:\`in Windows; base of everything. | `cd /`                  |
| `~`             | **Home Directory**    | The personal workspace and primary folder for the currently logged-in user.            | Similar to`C:\Users\username\`in Windows.      | `cd ~`                  |
| `./`(or`.`)   | **Current Directory** | The directory you are currently standing in and working from.                          | "Right here" in the active folder.               | `./run_script.sh`       |
| `../`(or`..`) | **Parent Directory**  | The folder located directly one level up from your current location.                   | "Step back one level up".                        | `cd ..`                 |

### What Are Commands Under the Hood?

#### When you run a command like cd or ls, the shell treats the line as a function call:

* Command name: The function to call (e.g., cd, ls).
* Flags & targets: The input arguments passed to that function (e.g., -la, projects/).

However, at the operating system level, commands fall into two fundamentally different categories: External Programs and Shell Builtins.

#### External Programs (e.g., ls, grep, python)

Most tools are standalone binary executables stored on your disk (e.g., /bin/ls or /usr/bin/grep).

When you run an external program, the shell:

1. Spawns a separate child process using the fork() system call.
2. Replaces the child process memory with the executable code using exec().
3. Waits for the child process to complete and exit back to the shell prompt.
4. Because the child process runs in an isolated environment, it cannot modify the parent shell's internal state.

#### Shell Builtins (e.g., cd, pwd, exit)

cd cannot be an external program. If cd ran as a standalone binary in a child process:

* The child process would change its own working directory.
* The child process would exit immediately.
* You would land back in your parent shell right where you started.

To change your current session's state, cd must run directly inside the active shell process. It is implemented as a Shell Builtin—an internal function hardcoded into the shell source code.

Under the hood, cd <path></path> parses the path argument and triggers the OS kernel system call directly:

```C
// Conceptual representation of how Bash handles `cd`
int builtin_cd(char *path) {
    return chdir(path); // chdir() updates the current process working directory
}
```

#### How to Check Any Command Yourself?

You can inspect whether any command is an internal function or an external binary using type:

```Shell
type cd
# Output: cd is a shell builtin

type ls
# Output: ls is /bin/ls (or an alias to /bin/ls)
```
