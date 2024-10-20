class Position:
    def __init__(self, index, line_no, cols, file_name):
        self.index = index
        self.line_no = line_no
        self.cols = cols
        self.file_name = file_name

class Error:
    def __init__(self, pos_start, pos_end, error_name, details):
        self.pos_start = pos_start  # Position instance
        self.pos_end = pos_end      # Position instance
        self.error_name = error_name
        self.details = details
        
    def __str__(self) -> str:
        result = f'Error: {self.error_name}: {self.details}\n'
        result += f'File: {self.pos_start.file_name}\n'  # Access file_name
        result += f'Line: {self.pos_start.line_no}\n'    # Access line number
        result += f'Column: {self.pos_start.cols}'       # Access column
        return result

# Creating Position instances
pos_start = Position(index=0, line_no=1, cols=0, file_name="script.py")
pos_end = Position(index=5, line_no=1, cols=5, file_name="script.py")

# Creating an Error instance
error = Error(pos_start, pos_end, "SyntaxError", "Invalid syntax.")
print(error)  # This will use the __str__ method
