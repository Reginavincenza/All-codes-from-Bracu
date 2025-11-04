#Node class for creating tree

class Node:
    def __init__(self, value=None, children=None):
        self.value = value
        self._children = children or []

    def is_terminal(self):
        return len(self._children) == 0

    def heuristic_value(self):
        return self.value

    def children(self):
        return self._children
    
def minimax(node, depth, maximizingPlayer):
    # Base case: terminal node or depth limit reached
    if depth == 0 or node.is_terminal():
        return node.heuristic_value()

    if maximizingPlayer == True: # Maximizing Player
       #Write your code here
        node_value = float("-inf")
        for i in node._children:
            node_value = max(node_value, minimax(i, depth-1, False))
        return node_value

    else:  # Minimizing player
       #Write your code here
        node_value = float("inf")
        for i in node._children:
            node_value = min(node_value, minimax(i, depth-1, True))
        return node_value

# Example tree
leaf1 = Node(3)
leaf2 = Node(5)
leaf3 = Node(2)
leaf4 = Node(9)
child1 = Node(children = [leaf1, leaf2])
child2 = Node(children = [leaf3, leaf4])
root = Node(children = [child1, child2])

print("Optimal value:", minimax(root, 3, True))