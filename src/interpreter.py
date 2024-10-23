from .lexer.lexer import Lexer
from .parser.parser import Parser

def run(text, fn: str):
    lexer = Lexer(text, fn)
    tokens, error = lexer.make_tokens() # make_tokens() is expected to return two values
    if error:
        return None, error
    
    # Generate AST
    parser = Parser(tokens)
    ast = parser.parse()
    
    return ast.node, ast.error