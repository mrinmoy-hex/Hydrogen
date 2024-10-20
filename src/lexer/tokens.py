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
    def __init__(self, type_: str, value: any = None):
        """
        Initializes a token.

        Args:
            type_ (str): The type of the token.
            value (any, optional): The value of the token. Defaults to None.
        """
        self.type = type_
        self.value = value

    def __repr__(self) -> str:
        """Returns a string representation of the token."""
        if self.value:
            return f"{self.type}: {self.value}"
        return f"{self.type}"

