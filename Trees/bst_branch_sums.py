"""
Given a Trees, create function that returns a list of it’s branch sums
ordered from leftmost branch sums to the rightmost branch sums
__________________________________________________________________

0              1
             /  \
1          2       3
         /   \    /  \
2       4     5   6  7
       / \    /
3    8    9  10


Here there are 5 branches ending in 8,9,10,6,7

SO sums would be:
1+2+4+8 =15
1+2+4+9 = 16
1+2+5+10 = 18
1+3+6 = 10
1+3+7 = 11

result being : [15, 16, 18, 10, 11]
__________________________________________________________________
- Need to keep runing total passed into recursive function,
    - when no more children it can be added to an array of branch values
- Sum up values within the array
__________________________________________________________________
Space and Time Complexity


Space: O(N)
- impacted by list of branch sums
- impacted by recurisve nature of function


Time: O(N)
- need to traverse all nodes


"""


def get_branch_sum(root):
    """sums values of all branches within a Trees"""
    sums = []

    branch_sum_helper(root, 0, sums)
    return sums


def branch_sum_helper(node, total_sum, sums):

    # return if none
    if node is None:
        return

    # update branch total
    updated_sum = total_sum + node.value

    # check if need to continue
    if node.left is None and node.right is None:
        sums.append(updated_sum)
        return
    
    branch_sum_helper(node.left, updated_sum, sums)
    branch_sum_helper(node.right, updated_sum, sums)


def main():
    """ Main function"""

    # create Trees
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

    sums = get_branch_sum(root)

    print(f" The list of all sums of each branches within Trees is {sums}")


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


''' Run Program '''
main()


