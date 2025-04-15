import os
import ast

def analyze_python_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        node = ast.parse(file.read())
    
    functions = [n.name for n in ast.walk(node) if isinstance(n, ast.FunctionDef)]
    classes = [n.name for n in ast.walk(node) if isinstance(n, ast.ClassDef)]
    
    return {
        'file': os.path.basename(filepath),
        'functions': functions,
        'classes': classes
    }

def analyze_directory(directory):
    results = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                path = os.path.join(root, file)
                results.append(analyze_python_file(path))
    return results

if __name__ == "__main__":
    directory = "example_project"
    analysis = analyze_directory(directory)
    for file_info in analysis:
        print(f"\n📄 {file_info['file']}")
        print(f"  🔹 Classes: {file_info['classes']}")
        print(f"  🔹 Functions: {file_info['functions']}")
