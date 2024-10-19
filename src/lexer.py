from .tokens import *
from .errors import IllegalCharError

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = -1
        self.current_char = None
        self.advance()  # starts the pos at 0

    def advance(self):
        self.pos += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None

    def make_tokens(self):
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
                char = self.current_char
                return [], IllegalCharError("'" + char + "'"+ " is not a valid character.")    # return empty list of token for illegal character
        
        tokens.append(Tokens(TT_EOF))        
        return tokens
    
    
    def make_numbers(self):
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



