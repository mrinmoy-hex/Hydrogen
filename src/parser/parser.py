# Nodes
class NumberNode:
    def __init__(self, tok) -> None:
        self.tok = tok
        
    def __repr__(self) -> str:
        return f"{self.tok}"
    
class BinOpNode:
    def __init__(self, left_node, op_tok, right_node) -> None:
        self.left_node = left_node
        self.op_tok = op_tok
        self.right_node = right_node
        
    def __repr__(self) -> str:
        return f'({self.left_node}, {self.op_tok}, {self.right_node})'
    
    
# Parser

class Parser:
    def __init__(self, tokens) -> None:
        self.tokens = tokens
        self.tok_index = -1
        self.advance()
        
    
    def advance(self):
        self.tok_index += 1
        if self.tok_index < len(self.tokens):
            self.current_tok = self.tokens[self.tok_index]
            
        return self.current_tok