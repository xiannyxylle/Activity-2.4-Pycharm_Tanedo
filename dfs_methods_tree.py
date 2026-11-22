
# ALGORITHM: DFS Methods in Binary Tree
# Student: Tanedo, Carlo R. (BSIT-2A)

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


class BinaryTree:
    def __init__(self):
        # Constructing the tree based on Assessment 3.5
        self.root = Node('C')

        self.root.left = Node('A')
        self.root.right = Node('R')

        self.root.left.left = Node('L')
        self.root.left.right = Node('O')

        self.root.right.left = Node('T')
        self.root.right.right = Node('A')

        self.root.left.left.left = Node('N')
        self.root.left.left.right = Node('E')

        self.root.left.right.left = Node('D')
        self.root.left.right.right = Node('O')

    # Preorder: Root -> Left -> Right
    def preorder(self, node):
        if node is None:
            return []

        return (
            [node.val]
            + self.preorder(node.left)
            + self.preorder(node.right)
        )

    # Inorder: Left -> Root -> Right
    def inorder(self, node):
        if node is None:
            return []

        return (
            self.inorder(node.left)
            + [node.val]
            + self.inorder(node.right)
        )

    # Postorder: Left -> Right -> Root
    def postorder(self, node):
        if node is None:
            return []

        return (
            self.postorder(node.left)
            + self.postorder(node.right)
            + [node.val]
        )


def run_dfs_program():
    tree = BinaryTree()

    print("=== DFS METHODS IN BINARY TREE ===")
    print("Student: Tanedo, Carlo R. (BSIT-2A)")
    print()

    print("Preorder (Root - Left - Right):")
    print(" - ".join(tree.preorder(tree.root)))

    print()

    print("Inorder (Left - Root - Right):")
    print(" - ".join(tree.inorder(tree.root)))

    print()

    print("Postorder (Left - Right - Root):")
    print(" - ".join(tree.postorder(tree.root)))


if __name__ == "__main__":
    run_dfs_program()
