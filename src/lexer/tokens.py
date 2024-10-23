# Tokens type

# goona store this tokens in dictionary in future
DIGITS = '0123456789'

TT_INT = 'INT'
TT_FLOAT = 'FLOAT'
TT_PLUS = 'PLUS'
TT_MINUS = 'MINUS'
TT_MUL = 'MUL'
TT_DIV = 'DIV'
TT_LPAREN = 'LPAREN'
TT_RPAREN = 'RPAREN'
TT_EOF = 'EOF'

class Tokens:
    """Represents a token with a type and optional value."""
    def __init__(self, type_: str, value: any = None, pos_start=None, pos_end=None):
        """
        Initializes a token.

        Args:
            type_ (str): The type of the token.
            value (any, optional): The value of the token. Defaults to None.
            pos_start, pos_end: For tracking the error in the token
        """
        self.type = type_
        self.value = value
        
        if pos_start:
            self.pos_start = pos_start.copy()
            self.pos_end = pos_start.copy()
            self.pos_end.advance()  # move the next position for end
            
        if pos_end:
            self.pos_end = pos_end.copy()

    def __repr__(self) -> str:
        """Returns a string representation of the token."""
        if self.value:
            return f"{self.type}: {self.value}"
        return f"{self.type}"

