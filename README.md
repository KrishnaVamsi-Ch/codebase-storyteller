# 🌍 Codebase Storyteller – Multilingual Python Project Explainer

Turn any Python project into a structured story – in the language of your choice!  
This tool analyzes code files, extracts classes & functions, and summarizes them in natural language with optional translation.

---

## 🧠 Features

- Scans `.py` files and extracts function/class structure  
- Generates easy-to-understand summaries  
- Translates explanation into 100+ languages (Hindi, Tamil, French, Spanish, etc.)  
- Useful for documentation, learning, onboarding, or exploring codebases  

---

## 📦 Example Output

**Input file:**

```python
class FileReader:
    def __init__(self, filename):
        self.filename = filename

    def load_file(self):
        with open(self.filename, 'r') as file:
            return file.read()

def greet_user(name):
    return f"Hello, {name}!"
