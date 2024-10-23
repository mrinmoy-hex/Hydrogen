from ..errors.string_with_arrows import string_with_arrows

class Error:
    """Base class for all errors in the lexer and parser."""
    def __init__(self, pos_start, pos_end, error_name, details) -> None:
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.error_name = error_name
        self.details = details
        
    def __str__(self) -> str:
        result = f'{error_highlight(self.error_name)}: {self.details}\n'
        result += f'{error_highlight("File ==> ")}: {self.pos_start.file_name}, line: {self.pos_start.line_no + 1}\n'   # Positon instance
        result += '\n\n' + string_with_arrows(self.pos_start.filetxt, self.pos_start, self.pos_end)
        return result
    
class IllegalCharError(Error):
    def __init__(self,pos_start, pos_end, details) -> None:
        super().__init__(pos_start, pos_end, "Illegal Character", details)


class InvalidSyntaxError(Error):
    def __init__(self,pos_start, pos_end, details) -> None:
        super().__init__(pos_start, pos_end, "Invalid Syntax", details)
    
    
            
def error_highlight(text: str) -> str:
    """Highlighting the error text with red color"""
    return f"\033[91m{text}\033[0m"  # ANSI escape code for red text



