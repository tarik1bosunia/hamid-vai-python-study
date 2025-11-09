# Python Virtual Environment Guide

This guide describes how to create, activate, deactivate virtual environments in Windows, Linux, and macOS, and how to install packages.

## Table of Contents
- [What is a Virtual Environment?](#what-is-a-virtual-environment)
- [Creating a Virtual Environment](#creating-a-virtual-environment)
- [Activating a Virtual Environment](#activating-a-virtual-environment)
- [Deactivating a Virtual Environment](#deactivating-a-virtual-environment)
- [Installing Packages](#installing-packages)
- [Managing Dependencies](#managing-dependencies)
- [Best Practices](#best-practices)

## What is a Virtual Environment?

A virtual environment is an isolated Python environment that allows you to install packages and dependencies for a specific project without affecting other projects or the system-wide Python installation.

## Creating a Virtual Environment

### Using venv (Python 3.3+)

The `venv` module is included in Python 3.3 and later versions.

**in Windows powershell or Linux/macOS terminal:**

```bash
python -m venv venv
```

You can replace `venv` with any name you prefer for your virtual environment directory.

### Using virtualenv (Alternative)

If you prefer using the `virtualenv` package:

**Install virtualenv first:**
```bash
pip install virtualenv
```

**Create virtual environment:**
```bash
virtualenv venv
```

## Activating a Virtual Environment

### Windows

**PowerShell:**
```bash
venv/scripts/activate
```

**Git Bash:**
```bash
source venv/Scripts/activate
```

### Linux/macOS

```bash
source venv/bin/activate
```

**Note:** After activation, you'll see `(venv)` or your environment name at the beginning of your command prompt.

## Deactivating a Virtual Environment

To deactivate the virtual environment and return to the global Python environment:

**All platforms:**
```bash
deactivate
```

## Installing Packages

Once your virtual environment is activated, you can install packages using pip:

### Install a single package
```bash
pip install package_name
```

### Install a specific version
```bash
pip install package_name==1.2.3
```

### Install multiple packages
```bash
pip install package1 package2 package3
```

### Install from requirements.txt
```bash
pip install -r requirements.txt
```

### Upgrade a package
```bash
pip install --upgrade package_name
```

### Uninstall a package
```bash
pip uninstall package_name
```

## Managing Dependencies

### Create requirements.txt

To save all installed packages and their versions:

```bash
pip freeze > requirements.txt
```

### View installed packages

```bash
pip list
```

### Show package information

```bash
pip show package_name
```

## Best Practices

1. **Always use a virtual environment** for each project to avoid dependency conflicts
2. **Add venv/ to .gitignore** - don't commit virtual environment folders to version control
3. **Use requirements.txt** to track project dependencies
4. **Name your environment** descriptively or use a standard name like `venv` or `.venv`
5. **Activate before working** - always activate your virtual environment before installing packages or running your project
6. **Keep requirements.txt updated** - regenerate it when you add or remove packages

## Common Issues

### PowerShell Execution Policy (Windows)

If you get an error when trying to activate on Windows PowerShell:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Python command not found

- On **Windows**: Use `python` or `py`
- On **Linux/macOS**: Use `python3`

### Multiple Python versions

To specify a Python version when creating a virtual environment:

```bash
python3.11 -m venv venv
```

## Additional Resources

- [Official Python venv documentation](https://docs.python.org/3/library/venv.html)
- [pip documentation](https://pip.pypa.io/en/stable/)
- [virtualenv documentation](https://virtualenv.pypa.io/en/latest/)