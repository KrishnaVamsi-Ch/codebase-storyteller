# 🌍 Codebase Storyteller – Multilingual Python Project Explainer

Turn any Python project into a structured story – in the language of your choice!  
This tool analyzes code files, extracts classes & functions, and summarizes them in natural language with optional translation.

---

## 🧠 Features

- 🔍 Scans `.py` files and extracts function/class structure  
- 📖 Generates easy-to-understand summaries  
- 🌐 Translates explanation into 100+ languages (Hindi, Tamil, French, Arabic, etc.)  
- 🗃️ Useful for documentation, learning, onboarding, or just exploring codebases  

---

## 📦 Example Output

**Input file:** `sample.py`

```python
class FileReader:
    def __init__(self, filename):
        self.filename = filename

    def load_file(self):
        with open(self.filename, 'r') as file:
            return file.read()

def greet_user(name):
    return f"Hello, {name}!"
```

**🧠 Output:**

📄 sample.py
  🔹 Classes: ['FileReader']
  🔹 Functions: ['__init__', 'load_file', 'greet_user']
  
🌐 Translations

🇪🇸 Spanish:
Este archivo contiene una clase (`FileReader`) y tres funciones (`__init__`, `load_file`, `greet_user`).
Estas funciones se utilizan para leer un archivo y saludar al usuario.

🇫🇷 French:
Ce fichier contient une classe (`FileReader`) et trois fonctions (`__init__`, `load_file`, `greet_user`).
Ces fonctions sont utilisées pour lire un fichier et saluer l'utilisateur.

🚀 How to Use

git clone https://github.com/KrishnaVamsi-Ch/codebase-storyteller.git
cd codebase-storyteller
pip install -r requirements.txt
python parser.py
python translate.py  # optional

🧭 Use Cases

📚 Beginners learning how codebases are structured

🧪 Documentation writers summarizing large projects

🌍 Multilingual devs who want explanations in their language

👥 Teams onboarding new develope







