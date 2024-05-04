from ast import Num, BinOp

class Interpreter:
    def __init__(self, parser):
        self.parser = parser

    def visit(self, node):
        # Visit each node type using the visitor pattern
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception('No visit_{} method'.format(type(node).__name__))

    def visit_Num(self, node):
        return node.value

    def visit_BinOp(self, node):
        if node.op.type == 'PLUS':
            return self.visit(node.left) + self.visit(node.right)
        elif node.op.type == 'MINUS':
            return self.visit(node.left) - self.visit(node.right)
        elif node.op.type == 'MUL':
            return self.visit(node.left) * self.visit(node.right)
        elif node.op.type == 'DIV':
            return self.visit(node.left) // self.visit(node.right)  # Integer division
        else:
            self.generic_visit(node)

    def interpret(self):
        tree = self.parser.parse()
        return self.visit(tree)
