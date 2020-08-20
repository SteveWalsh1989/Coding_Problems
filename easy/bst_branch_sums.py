

def get_branch_sum(root):
    """sums values of all branches within a BST"""
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

    sums = get_branch_sum(root)

    print(f" The list of all sums of each branches within BST is {sums}")


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


''' Run Program '''
main()


