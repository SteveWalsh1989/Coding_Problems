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
0                5
             /      \
1         8          2
        /  \       /   \
2      2    4     6     9
      /                  \
3    1                    8
__________________________________________________________________


"""


def validate_bst(bst):
    """Validates if bst is true bst """
    # call helper function passing in the tree and the min/ max values for ints that could be initially used for root
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

    # create invalid BST
    invalid_bst = BinaryTree(1)
    invalid_bst.left = BinaryTree(2)
    invalid_bst.left.left = BinaryTree(4)
    invalid_bst.left.left.left = BinaryTree(8)
    invalid_bst.left.left.right = BinaryTree(9)
    invalid_bst.left.right = BinaryTree(5)
    invalid_bst.left.right.right = BinaryTree(10)
    invalid_bst.right = BinaryTree(3)
    invalid_bst.right.left = BinaryTree(6)
    invalid_bst.right.right = BinaryTree(7)

    # create valid BST
    valid_bst = BinaryTree(11)
    valid_bst.left = BinaryTree(5)
    valid_bst.left.left = BinaryTree(3)
    valid_bst.left.right = BinaryTree(5)
    valid_bst.left.left.left = BinaryTree(1)
    valid_bst.right = BinaryTree(15)
    valid_bst.right.left = BinaryTree(13)
    valid_bst.right.right = BinaryTree(30)

    # check if bsts are valid/ invalid
    res_1 = validate_bst(invalid_bst)
    res_2 = validate_bst(valid_bst)


    # print results
    print_results(res_1)
    print_results(res_2)


def print_results(res):
    """ prints results"""
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
