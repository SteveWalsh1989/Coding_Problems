"""

Finding the closest value in a BST - numbers are unique
__________________________________________________________________

0               40
             /      \
1         33          61
          /   \        /   \
2        20    36      51   70
        /              \
3      9                55

IE:
Input - 12
Res - 13
__________________________________________________________________

- Need to keep track of the closest values beet candidate
- We need to check then the absolute value of what we have with the target value and node
- if smaller difference then thats our new candidate
- if target is smaller than current node then we traverse left
- if target is larger than current node then we traverse right
-edge case: if absolute difference between current node and target is 0 - we can stop

__________________________________________________________________
Code:
"""
def find_closest_value(tree, target):
    """ locates closet value within bst"""
    return find_closest_value_helper(tree, target, tree.value)


def find_closest_value_helper(tree, target, best_candidate):
    """ helper function for recursion in locating best candidate"""

    # for leaf nodes
    if tree is None:
        return best_candidate

    # compare absolute difference between nodes and target
    if abs(target - best_candidate) > abs(target - tree.value):
        best_candidate = tree.value

    # compare best candidate with target to determine best traversal route
    if target > tree.value:
        return find_closest_value_helper(tree.right, target, best_candidate)
    elif target < tree.value:
        return find_closest_value_helper(tree.left, target, best_candidate)
    else:
        return best_candidate 


def main():
    """ Main function"""

    # create BST
    root = BinaryTree(40)
    root.left = BinaryTree(33)
    root.left.left = BinaryTree(20)
    root.left.left.left = BinaryTree(9)
    root.left.right = BinaryTree(36)
    root.right = BinaryTree(61)
    root.right.left = BinaryTree(51)
    root.right.left.right = BinaryTree(55)
    root.right.right = BinaryTree(70)

    value = 3
    res = find_closest_value(root, value)

    print(f" The closest value in the BST to {value} is {res}")


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


''' Run Program '''
main()


