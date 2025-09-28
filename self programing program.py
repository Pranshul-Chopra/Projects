import ast
import random

def self_modifying_function(a, b):
    """
    A toy function that mutates its own stored source code
    instead of relying on inspect.getsource().
    """

    if not hasattr(self_modifying_function, "source"):
        self_modifying_function.source = """
def self_modifying_function(a, b):
    return a + b
"""

    tree = ast.parse(self_modifying_function.source)


    class Mutator(ast.NodeTransformer):
        def visit_BinOp(self, node):
            self.generic_visit(node)
            if isinstance(node.op, ast.Add) and random.random() < 0.5:
                node.op = ast.Mult()
            elif isinstance(node.op, ast.Mult) and random.random() < 0.5:
                node.op = ast.Add()
            return node

    mutated = Mutator().visit(tree)
    ast.fix_missing_locations(mutated)

   
    new_src = ast.unparse(mutated)

 
    self_modifying_function.source = new_src

 
    exec(new_src, globals())


    return a + b



if __name__ == "__main__":
    for i in range(1, 6):
        print(f"Call {i}: result =", self_modifying_function(2, 3))
