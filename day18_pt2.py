import ast

class EquationTransformer(ast.NodeTransformer):
    def visit_BinOp(self, node):
        if isinstance(node.op, ast.Pow):
            new_node = ast.BinOp(self.visit(node.left), ast.Add(), self.visit(node.right))
        elif isinstance(node.op, ast.Sub):
            new_node = ast.BinOp(self.visit(node.left), ast.Mult(), self.visit(node.right))
        else:
            new_node = node
        return new_node

exprs = []
with open("day18.in") as f:
    for line in f:
        exprs.append(line.strip())

sum = 0
for expr in exprs:
    # ready for some ultimate hax
    new_expr = expr.replace("*", "-").replace("+", "**")
    tree = ast.parse(new_expr)
    new_tree = EquationTransformer().visit(tree)
    sum += eval(ast.unparse(new_tree))

print(sum)
