class FileReader:
    def __init__(self, filename):
        self.filename = filename

    def load_file(self):
        with open(self.filename, 'r') as file:
            return file.read()

def greet_user(name):
    return f"Hello, {name}!"
