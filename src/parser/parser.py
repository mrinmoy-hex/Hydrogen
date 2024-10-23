from ..lexer import tokens
from ..errors.errors import *

# Nodes
class NumberNode:
    """Represents a number in the AST."""
    def __init__(self, tok) -> None:
        self.tok = tok
        
    def __repr__(self) -> str:
        return f"{self.tok}"
    
class BinOpNode:
    """Represents a binary operation in the AST."""
    def __init__(self, left_node, op_tok, right_node) -> None:
        self.left_node = left_node
        self.op_tok = op_tok
        self.right_node = right_node
        
    def __repr__(self) -> str:
        return f'({self.left_node}, {self.op_tok}, {self.right_node})'

##########################   

# Parse Result

class ParseResult:
    def __init__(self) -> None:
        self.error = None
        self.node = None
        
    def register(self, result):
        if isinstance(result, ParseResult):
            if result.error: self.error = result.error
            return result.node
        
        return result
    
    def success(self, node):
        self.node = node
        return self
    
    
    def failure(self, error):
        self.error = error
        return self
        

##########################    
# Parser

class Parser:
    """Parses tokens into an abstract syntax tree (AST)."""
    def __init__(self, tokens) -> None:
        self.tokens = tokens
        self.tok_index = -1
        self.advance()  # initializes the current_tok
        
    
    def advance(self):
        self.tok_index += 1
        if self.tok_index < len(self.tokens):
            self.current_tok = self.tokens[self.tok_index]
            
        return self.current_tok
    
    
    def parse(self):
        result = self.expr() 
        if not result.error and self.current_tok.type != tokens.TT_EOF:
            return result.failure(InvalidSyntaxError(
                self.current_tok.pos_start, self.current_tok.pos_end,
                "Expected '+', '-', '*' or '/'"
            ))   
        return result

    
    def factor(self):
        response = ParseResult()
        tok = self.current_tok
        if tok.type in (tokens.TT_INT, tokens.TT_FLOAT):
            response.register(self.advance())
            return response.success(NumberNode(tok))
        
        return response.failure(InvalidSyntaxError(
            tok.pos_start, tok.pos_end, 
            "Expected int or float"
        ))
    
    
    
    def term(self):
        return self.bin_opr(self.factor, (tokens.TT_MUL, tokens.TT_DIV))
    
    
    def expr(self):
        return self.bin_opr(self.term, (tokens.TT_PLUS, tokens.TT_MINUS))
    
    
    def bin_opr(self, func, opr):
        result = ParseResult()
        left = result.register(func())
        if result.error: return result
        
        while self.current_tok.type in opr:
            op_tok = self.current_tok
            right = result.register(func())
            if result.error: return result
            left = BinOpNode(left, op_tok, right)
            
            result.register(self.advance())
            
        return result.success(left)