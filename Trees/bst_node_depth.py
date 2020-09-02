"""
Given a Trees return the sum of the depth of each node

____________________________________________________________
0             1
            /   \
1         2       3
          / \    /  \
2       4    5  6   7
        /     \
3     8        9


Here being 0(1) + 1(2) + 2(4) + 3(2) = 16
____________________________________________________________

Recursive approach:
——————————
When we call the function we will return the sum of the depth of the node that we are at, plus the return values of calls to the recursive function on the left and right children of the node.

Pass in the node and the depth of the node

function as formula would be.
f(n, d) = d + f( l, d+1) + f( r, d+1)
n - node
d - depth node
l - left child of node
r - right child of node

Base case will be when there is a leaf node without children.


____________________________________________________________
Space and Time Complexity:

Space: O(h)
  - h - height

Time: O(N)
- n - number nodes
"""

def node_depth(root, depth=0):
    """ Main function"""

    # handle base case
    if root is None:
        return 0

    # Call function recursively on child nodes
    return depth + node_depth(root.left, depth + 1) + node_depth(root.right, depth + 1)


def main():
    """ Main function"""

    # create Trees - res should be 16
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

    print(f" The sum of node depths for Trees is {res}")


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


''' Run Program '''
main()





