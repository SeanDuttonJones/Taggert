import ast

class TagExtractor:

    def __init__(self):
        self.TAG_ATTRIBUTE_NAME = "__tags__"

    def parse(self, python_code):
        tree = ast.parse(python_code)
        
        for node in tree.body:
            if(isinstance(node, ast.Assign) and len(node.targets) == 1):
                target = node.targets[0]

                if(isinstance(target, ast.Name) and target.id == self.TAG_ATTRIBUTE_NAME):
                    return ast.literal_eval(node.value)