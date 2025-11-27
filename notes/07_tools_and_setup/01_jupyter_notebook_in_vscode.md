# Starting Jupyter Notebook in VS Code — From Virtual Environment Activation

This guide starts **directly from activating your virtual environment**, and now also includes the required step to **install/activate the VS Code Python & Jupyter extensions**.

---

## 1. Activate Your Virtual Environment

### Linux / macOS

```
source venv/bin/activate
```

### Windows (PowerShell)

```
venv\Scripts\Activate.ps1
```

If activation is successful, your terminal will show something like:

```
(venv) user@computer:~/project_folder$
```

---

## 2. Install Jupyter Inside the Virtual Environment

Once the `venv` is active:

```
pip install jupyter notebook ipykernel
```

(Optional but recommended):

```
pip install numpy pandas matplotlib
```

---

## 3. Open VS Code in Your Project Folder

If you're inside your project folder:

```
code .
```

Or open manually from VS Code → **File → Open Folder**.

---

## 4. Install & Enable Required VS Code Extensions

In VS Code:

1. Click the **Extensions** icon (left sidebar) or press `Ctrl+Shift+X`.
2. Install these two extensions (both by Microsoft):

   * **Python**
   * **Jupyter**
3. Make sure both show as **Enabled**.

These extensions allow VS Code to:

* Recognize `.ipynb` files
* Run Jupyter kernels
* Connect Python environments

Without them, notebooks will not work properly.

---

## 5. Select the Virtual Environment in VS Code

1. Press **Ctrl+Shift+P**.
2. Type and select: **Python: Select Interpreter**.
3. Choose your venv interpreter:

   * Linux/macOS → `./venv/bin/python`
   * Windows → `.\venv\Scripts\python.exe`

VS Code will now use your virtualenv for notebook execution.

---

## 6. Create a New Jupyter Notebook

### Method 1 — Command Palette

1. Press **Ctrl+Shift+P**.
2. Select **Jupyter: Create New Jupyter Notebook**.
3. Save as `my_notebook.ipynb`.

### Method 2 — Manual

1. Click **New File**.
2. Name it `my_notebook.ipynb`.

VS Code will automatically open it in notebook mode.

---

## 7. Select the Notebook Kernel

At the top-right of the notebook:

1. Click **Select Kernel**.
2. Choose the Python environment from your `venv`.

This links the notebook to your activated virtual environment.

---

## 8. Test It — Run a Python Cell

Create a cell and type:

```
print("Jupyter Notebook is running inside VS Code!")
```

Run using:

* **Shift + Enter**
* **Ctrl + Enter**
* Or the **Run ▶ button**

You should see the output under the cell.

---

## 9. Example: Simple Plot

```
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.title("Sine Wave")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.show()
```

---

## 10. Managing the Kernel

If something breaks or freezes:

* Click **Restart Kernel** (⟳)
* Or use **Ctrl+Shift+P** → `Jupyter: Restart Kernel`

---

## 11. Quick Summary

1. Activate venv → `source venv/bin/activate` or `venv\Scripts\Activate.ps1`
2. `pip install jupyter ipykernel`
3. `code .` to open VS Code
4. Install/enable **Python** + **Jupyter** extensions
5. **Python: Select Interpreter** → choose `venv`
6. Create `.ipynb` notebook
7. Select Kernel → `venv`
8. Run cells

Now you’re fully set to use Jupyter Notebook inside VS Code with the correct extensions and environment.
