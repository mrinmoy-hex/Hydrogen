
class Error:
    def __init__(self, error_name, details) -> None:
        self.error_name = error_name
        self.details = details
        
    def __str__(self) -> str:
        result = f'{error_highlight(self.error_name)}: {self.details}'
        
        return result
    
class IllegalCharError(Error):
    def __init__(self, details) -> None:
        super().__init__("Illegal Character", details)
        

def error_highlight(text: str) -> str:
    """Highlighting the error text with red color"""
    return f"\033[91m{text}\033[0m"  # ANSI escape code for red text
