import os

def create_initfile():
    files: list = ['lexer', 'parser', 'errors']
    os.chdir('src')
    path: str = os.getcwd()
    # print(os.getcwd())
    for i, file in enumerate(files):
        init_file: str = os.path.join(path, file, '__init__.py')
        if not os.path.exists(init_file):
            with open(init_file, "w") as f:
                f.write('')     # create an empty __init__ file
            print(f"Process[{i}] exited with success")
        else:
            print("File already exists")
            
def move_files():
    pass