# ML Environment Setup Checklist

This guide sets up a clean Python virtual environment for ML projects using **venv**, **pip-tools**, and Jupyter.

---

## 1. Create & activate a virtual environment
```bash
# Create venv
python3 -m venv ml-env

# Activate venv (Mac/Linux)
source ml-env/bin/activate

# (On Windows PowerShell)
ml-env\Scripts\Activate
```

---

## 2. Upgrade essentials
```bash
pip install --upgrade pip setuptools wheel
```

---

## 3. Install pip-tools
```bash
pip install pip-tools
```

---

## 4. Create requirements.in
Example file (`requirements.in`):
```
numpy
pandas
matplotlib
seaborn
scikit-learn
tensorflow
xgboost
jupyter
```

---

## 5. Compile locked requirements.txt
```bash
pip-compile requirements.in
```

This generates a **fully pinned** `requirements.txt`.

---

## 6. Install dependencies
```bash
pip install -r requirements.txt
```

---

## 7. Add venv to Jupyter
```bash
pip install ipykernel
python -m ipykernel install --user --name=ml-env --display-name "Python (ml-env)"
```

Now in Jupyter Notebook/Lab, select **Kernel → Change Kernel → Python (ml-env)**.

---

## 8. Save environment (optional)
Export installed packages for backup:
```bash
pip freeze > requirements-lock.txt
```

---

## 9. Recreate environment later
```bash
python3 -m venv ml-env
source ml-env/bin/activate
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

---

