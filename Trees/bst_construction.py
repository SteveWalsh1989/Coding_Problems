
"""

Write a Trees class that supports:
- inserting new nodes
- removing nodes
  - a node can be replaced by the left most node of it’s right sided child as it is smaller than any other node on it’s side and strictly greater than any node from the left hand child’s nodes from the original node
- searching for values
__________________________________________________________________

Trees is said to be valid if:
- it’s value is strictly greater than the value of every node to it’s left
- its value is equal to or less than any value to it’s right
- it’s child nodes are either valid Trees or null
  
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

For all insertion, searching and deletion:

Average: Time/space -: O(logN)
- where n is number of nodes
- since we are eliminating half the remaining nodes each time moving branch

Worst case: Time/space O(N)
- if the tree is set up in such a way that eliminating half each time didnt work
- IE: tree with no left nodes

__________________________________________________________________

"""


def main():
    """ Main function"""

    new_bst = BST(1)
    new_bst.insert(2).insert(4).insert(6).insert(12).insert(20).insert(26)
    check_val = 4
    contains = new_bst.contains(check_val)

    print(f"Trees created ")

    if contains:
        print(f"The Trees contains {check_val}" )
    else:
        print(f"The Trees does not contain {check_val}")

    new_bst.delete(check_val)
    contains = new_bst.contains(check_val)

    print(f"Removed {check_val} from Trees")

    if contains:
        print(f"The Trees contains {check_val}")
    else:
        print(f"The Trees does not contain {check_val}")


class BST:
    """Trees class """

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        """ Inserts a value as node in Trees """

        # track current node
        current_node = self

        while True:
            # when less traverse left
            if value < current_node.value:

                # If leaf node add value as Trees
                if current_node.left is None:
                    current_node.left = BST(value)
                    break
                else:
                    # move left
                    current_node = current_node.left
            # when more traverse right
            else:

                # If leaf node add value as Trees
                if current_node.right is None:
                    current_node.right = BST(value)
                    break
                else:
                    # move right
                    current_node = current_node.right

        # allow for chaining calls - test.insert(1).insert(2) etc
        return self

    def contains(self, value):
        """ Checks if Trees contains a value - returns true/false"""
        # keep track of current node
        current_node = self

        while current_node is not None:
            # when less traverse left
            if value < current_node.value:
                current_node = current_node.left
            # when more traverse right
            elif value > current_node.value:
                current_node = current_node.right
            # if found
            else:
                return True

    def delete(self, value):
        """ remove nodes from Trees """

        # keep track of current node
        current_node = self

        # Step 1: find node
        while current_node is not None:
            if value < current_node.value:
                # track parent node
                parent_node = current_node

                current_node = current_node.left

            # when more traverse right
            elif value > current_node.value:
                parent_node = current_node

                current_node = current_node.right
            # # Step 2: Node found
            else:

                # Node has both children
                if current_node.left is not None and current_node.right is not None:
                    current_node.value = current_node.right.get_lowest_value()
                    current_node.right.remove(current_node.value, current_node)
                # root node - no parent
                elif parent_node is None:
                    if current_node.left is not None:
                        # reassign all node values
                        current_node.value = current_node.left.value
                        current_node.right = current_node.left.right
                        current_node.left = current_node.left.left
                    elif current_node.right is not None:
                        current_node.value = current_node.right.value
                        current_node.left = current_node.right.left
                        current_node.right = current_node.right.right
                    else:
                        # root node with no children - IE: deleting the Trees
                        current_node.value = None

                # has one or no child nodes - assign either left or right
                elif parent_node.left == current_node:

                    parent_node.left = current_node.left if current_node.left is not None else current_node.right
                elif parent_node.right == current_node:
                    parent_node.right = current_node.left if current_node.left is not None else current_node.right
                break

                return self

    def get_lowest_value(self):
        """ Gets the lowest value in a right side of Trees"""
        # called on right sub tree
        current_node = self

        while current_node.left is not None:
            current_node = current_node.left

        return current_node.value


''' Run Program '''
main()


