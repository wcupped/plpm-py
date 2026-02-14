# <img width="32" height="32" alt="plpm" src="https://github.com/user-attachments/assets/2d06bb3a-88e1-45f7-be22-ae740036a609" /> PLPM - Pacman-like Package Manager

<img width="1280" height="640" alt="banner" src="https://github.com/user-attachments/assets/20f0c03f-f0a5-4579-bc50-763a2886f4e7" />

# What is PLPM (Pacman-Like Package Manager)?
A Windows package manager that is aiming on creating Linux-like experience, inspired by [WinGet](https://github.com/microsoft/winget-cli) and especially [Arch Linux](https://archlinux.org/) Package Manager named [Pacman](https://wiki.archlinux.org/title/Pacman)

# Main Features
It has three parameters when calling utility through CLI:
- -S
- -Sr
- -F

-S - Install package by its name
-Sr - Sync repositories and hashes
-F - Find package by its name

It does check expected hash and the hash of installer that is being took from URL, that is provided with the name of package in [PLPM Repository](https://github.com/wcupped/plpm-repo) (pls help adding more packages to this repository) where we also store hashes of installers.
We're planning to improve the security and add more features in this package manager.

# Installation
Go to [Releases tab](https://github.com/wcupped/plpm-py/releases/latest) and choose the type of utility, portable or the setup one

> [!NOTE]
> You can also compile it yourself by executing `build.bat` file in the root directory of repository.

# Building manually
- Run command `pip install -r requirements.txt` in the root directory of repository.
- Run `build.bat` script and wait until it will end it's job.
The compiled binary will be at `output` directory, with `_internal` directory, this one is required, to be able to start `plpm.exe`
> [!NOTE]
> It is possible to make it compile only the one binary without directory required by changing `--onedir` argument in `build.bat` to `--onefile`, but when You will try running the binary file it will run very slow.

# Additional information
The package manager is pretty small and being in early access at this point. All PRs will be appreciated and looked through. We need Your help in developing this software, and we hope You will suggest us some changes.
You can also submit [Issues](https://github.com/wcupped/plpm-py/issues) if You have any.
We plan to rewrite this program on C++ later for more speed and efficiency, I hope You will like this utility. 
Good luck using PLPM! >_