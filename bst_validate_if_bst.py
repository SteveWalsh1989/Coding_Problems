"""


Function that takes in a BST and returns if a valid BST.
__________________________________________________________________

BST is said to be valid if:
- it’s value is strictly greater than the value of every node to it’s left
- its value is equal to or less than any value to it’s right
- it’s child nodes are either valid BST or null

__________________________________________________________________
Valid:
0             5
             /      \
1         3          7
          /   \       /   \
2      2    4     6   9
        /              \
3    1                8


Invalid
0             5
             /      \
1         8          2
          /   \       /   \
2      2    4     6   9
        /              \
3    1                8
__________________________________________________________________


"""


def validate_bst(bst):
    """Validates if bst is true bst """
    return validate_bst_helper(bst, float("-inf"), float("inf"))


def validate_bst_helper(tree, max_val, min_val):

    # if leaf node
    if tree is None:
        return True
    # if outside of allowed range
    elif tree.value < min_val or tree.value >= max_val:
        return False

    # checking each child is valid branch
    left_is_valid = validate_bst_helper(tree.left, min_val, tree.value)
    right_is_valid = validate_bst_helper(tree.right, tree.value, max_val)

    return left_is_valid and right_is_valid


def main():
    """ Main function """

    # create BST
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.left.left = BinaryTree(4)
    root.left.left.left = BinaryTree(8)
    root.left.left.right = BinaryTree(9)
    root.left.right = BinaryTree(5)
    root.left.right.right = BinaryTree(10)
    root.right = BinaryTree(3)
    root.right.left = BinaryTree(6)
    root.right.right = BinaryTree(7)

    res = validate_bst(root)

    if res:
        print(f"The tree is a valid BST ")
    else:
        print(f"The tree is not a valid BST ")


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


''' Run Program '''
main()
