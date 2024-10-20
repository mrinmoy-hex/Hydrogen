from .lexer.lexer import Lexer

def run(text, fn: str):
    lexer = Lexer(text, fn)
    tokens, error = lexer.make_tokens() # make_tokens() is expected to return two values
    
    return tokens, error