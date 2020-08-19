

def node_depth(root, depth=0):
    """ Main function"""

    # handle base case
    if root is None:
        return 0

    # Call function recursively on child nodes
    return depth + node_depth(root.left, depth + 1) + node_depth(root.right, depth + 1)


def main():
    """ Main function"""

    # create BST - res should be 16
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.left.left = BinaryTree(4)
    root.left.left.left = BinaryTree(8)
    root.left.left.right = BinaryTree(9)
    root.left.right = BinaryTree(5)
    root.right = BinaryTree(3)
    root.right.left = BinaryTree(6)
    root.right.right = BinaryTree(7)

    res = node_depth(root)

    print(f" The sum of node depths for BST is {res}")


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


''' Run Program '''
main()





