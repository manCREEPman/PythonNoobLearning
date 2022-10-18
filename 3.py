from __future__ import annotations

class WrongDirectionError(Exception):
    pass

ontology = {
    'classes': {},
    'relations': {},
    'class_elements': {},
    'relations_elements': {}
}

class Node:
    def __init__(self, left=None, right=None, type = 'class', name = 'a'):
        self.left = left
        self.right = right
        self.type = type
        self.name = name
        self.__secret = 'secret'
    
    def make_child(self, child, direction: str ='left'):
        if direction == 'left':
            self.left = child
        elif direction == 'right':
            self.right = child
        else:
            raise WrongDirectionError
    
    def get_child(self, direction: str='left') -> Node:
        if direction == 'left':
            return self.left
        elif direction == 'right':
            return self.right
        else:
            raise WrongDirectionError

    def __str__(self) -> str:
        return f'{self.left} / {self.right}'

class a:
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right
    
    def __str__(self) -> str:
        return f'{self.left} / {self.right}'
    
# x = a(1, a(1, 2))
# print(x.left, x.right)
    
def make_Node(tree: Node):
    x = 1
    y = 2
    z = 'Zа наших'
    tree.right = x 
    tree.left = Node
    tree.left.right = y 
    tree.left.left = Node
    tree.left.left.right = z
    
t = Node()
make_Node(t)
x = Node()
print(x)

# print(t.right, t.left.right, t.left.left.right)
#print(t.right) 
# print(t is t.left)
# print(t.left is t.left.left)