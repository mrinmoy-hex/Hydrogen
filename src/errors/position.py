class Position:
    """Represents the current position in the input text."""
    def __init__(self, index, line_no, cols, file_name, filetxt) -> None:
        """
        Keeps track of position.

        Args:
            index (int): The character index in the text.
            line_no (int): The current line number.
            cols (int): The current column number.
            file_name (str): The name of the file being processed.
            filetxt (str): Keeps tracks of the text and returns in case of error
        """
        self.index = index
        self.line_no = line_no
        self.cols = cols
        self.file_name = file_name
        self.filetxt = filetxt      
        
    def advance(self, current_char=None):
        """Advances the position based on the current character.

        Args:
            current_char (str): The current character being processed.
        """
        self.index += 1
        self.cols += 1
        
        if current_char == '\n':
            self.cols = 0
            self.line_no += 1
            
        # return self
            
    def copy(self):
        """Creates a copy of the current position."""
        return Position(self.index, self.line_no, self.cols, self.file_name, self.filetxt)