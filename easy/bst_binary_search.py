def binary_search(array, target):
    """Locates index of target within array if exists"""

    # return recursive function given start + end of array
    return binary_search_helper(array, target, 0, len(array)-1)


def binary_search_helper(array, target, left, right):
    """ recursion helper for locating index of value within bst """

    while left <= right:
        midpoint = (left + right) // 2
        midpoint_val = array[midpoint]

        if target == midpoint_val:
            return midpoint   # return targets index
        elif target < midpoint_val:
            right = midpoint - 1   # shift right index
        else:
            left = midpoint + 1 # shift left index

    # if target doesnt exist in array
    return -1


def main():
    """ Main function """

    array = [0, 1, 21, 33, 45, 61, 71, 72, 73]
    target = 21

    index = binary_search(array, target)

    print(f" The index of {target} within {array} is  {index}")


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


''' Run Program '''
main()


