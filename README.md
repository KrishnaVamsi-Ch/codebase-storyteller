# 🌍 Codebase Storyteller – Multilingual Python Project Explainer

Turn any Python project into a structured story – in the language of your choice!  
This tool analyzes code files, extracts classes & functions, and summarizes them in natural language with optional translation.

---

## 🧠 Features

- 🔍 Scans `.py` files and extracts function/class structure  
- 📖 Generates easy-to-understand summaries  
- 🌐 Translates explanation into 100+ languages (Hindi, Tamil, French, Spanish, etc.)  
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
📄 sample.py  
  🔹 Classes: ['FileReader']  
  🔹 Functions: ['__init__', 'load_file', 'greet_user']

Este archivo contiene una clase (`FileReader`) y tres funciones (`__init__`, `load_file`, `greet_user`).
Estas funciones se utilizan para leer un archivo y saludar al usuario.

Ce fichier contient une classe (`FileReader`) et trois fonctions (`__init__`, `load_file`, `greet_user`).
Ces fonctions sont utilisées pour lire un fichier et saluer l'utilisateur.

git clone https://github.com/KrishnaVamsi-Ch/codebase-storyteller.git
cd codebase-storyteller
pip install -r requirements.txt
python parser.py
python translate.py

🧭 Use Cases
📚 Beginners learning how codebases are structured

🧪 Documentation writers summarizing large projects

🌍 Multilingual devs who want explanations in their language

👥 Teams onboarding new developers

📫 Let's Connect



🧠 “Code is not just what a computer understands — it's what humans understand too.”

yaml
Copy code

---

✅ Paste this whole thing inside your GitHub [README.md editor](https://github.com/KrishnaVamsi-Ch/codebase-storyteller/edit/main/README.md), then click **Commit changes**.

When you’re done, say **“done ✅”** and I’ll check it live again!




You said:

what are these codes and they are in different boxes that is why im getting confued

ChatGPT said:
Great question, Krishna — and thanks for sharing the screenshot. Let me clarify everything simply:
