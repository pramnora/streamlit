import streamlit as st

# How to display Python code.

# -------------------------------------

# Example 1: Using backticks...

st.markdown("""
```python
def greeting(name):
    print(f"Hello, {name}")
```
""")

# -------------------------------------

# Example 2: Using code as string.../3 apostropes...


code=('''
def greeting2(name):
    print(f"Hello, {name}"
''')

st.code(code,language="python",line_numbers=True)

# -------------------------------------
