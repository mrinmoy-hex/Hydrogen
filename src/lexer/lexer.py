# imports
from .tokens import *
from ..errors.errors import IllegalCharError
from ..errors.position import Position

class Lexer:
    """Tokenizes input text into a list of tokens."""
    def __init__(self, text, file_name):
        """
        Initializes the lexer.

        Args:
            text (str): The input text to tokenize.
            file_name (str): Current file name -> <stdin>
        """
        self.text = text
        self.file_name = file_name
        self.pos = Position(-1, 0, -1, file_name, text)  # created an instance of Position
        self.current_char = None
        self.advance()  # starts the pos at 0

    def advance(self):
        """Advances the current position and updates the current character."""
        self.pos.advance(self.current_char)  # defined in Positon
        if self.pos.index < len(self.text):
            self.current_char = self.text[self.pos.index]
        else:
            self.current_char = None

    def make_tokens(self):
        """Generates a list of tokens from the input text.

        Returns:
            tuple: A tuple containing a list of tokens and an error (if any).
        """
        tokens = []

        while self.current_char != None:
            # keeps tracks of the current characters
            if self.current_char.isspace():
                """Checks for white spaces in the istream"""
                self.advance()
                
            elif self.current_char in DIGITS:
                """Generates numbers from the input"""
                tokens.append(self.make_numbers())

            elif self.current_char == '+':
                tokens.append(Tokens(TT_PLUS))
                self.advance()
            elif self.current_char == '-':
                tokens.append(Tokens(TT_MINUS))
                self.advance()
            elif self.current_char == '*':
                tokens.append(Tokens(TT_MUL))
                self.advance()
            elif self.current_char == '/':
                tokens.append(Tokens(TT_DIV))
                self.advance()
            elif self.current_char == '(':
                tokens.append(Tokens(TT_LPAREN))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Tokens(TT_RPAREN))
                self.advance()
                
            else:
                pos_start = self.pos.copy()
                char = self.current_char
                return [], IllegalCharError(pos_start, pos_end=self.pos, details=f"'{char}' is not a valid character.")    # return empty list of token for illegal character
        
        tokens.append(Tokens(TT_EOF))        
        return tokens, None
    
    
    def make_numbers(self):
        """Creates a number token from the input.

        Returns:
            Tokens: A token representing an integer or float.
        """
        dot_count: int = 0
        num_str: str = ''
        # looping through digits or .
        while self.current_char is not None and (self.current_char.isdigit() or self.current_char == '.'):
            if self.current_char == '.':
                if dot_count == 1:  # more than one dot is invalid
                    break
                dot_count += 1
                num_str += '.'
                
            else:
                num_str += self.current_char
                
            self.advance() # move to next character
        
        # logic to decide whether to return int token or float
        if dot_count == 0:
            return Tokens(TT_INT, int(num_str))
        else:
            return Tokens(TT_FLOAT, float(num_str))



