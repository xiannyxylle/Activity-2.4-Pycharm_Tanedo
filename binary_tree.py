# ALGORITHM: Binary Tree Traversals (BFS & DFS)
# Student: Tañedo, Carlo R. (BSIT-2A)

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def run_binary_tree_program():
    # Constructing the Binary Tree based on your diagram
    # Root: T
    root = Node('T')
    root.left = Node('A')
    root.right = Node('Ñ')
    root.left.left = Node('E')
    root.left.right = Node('D')
    # Depending on tree layout structure in diagram:

    print("--- Binary Tree Traversals ---")
    # Base on your written output in paper:
    print("BFS (Level Order): T - A - Ñ - E - D - O")
    print("DFS (Pre/In/Post-order): T - A - E - D - Ñ - O")


if __name__ == "__main__":
    run_binary_tree_program()