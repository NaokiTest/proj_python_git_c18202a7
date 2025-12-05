import os

# ディレクトリの作成
os.makedirs('proj_python_git_c18202a7', exist_ok=True)

# ファイルの作成
with open('proj_python_git_c18202a7/basic_calculations.py', 'w') as f:
    f.write('''
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
''' )