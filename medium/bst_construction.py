






def main():
    """ Main function"""

    new_bst = BST(1)
    new_bst.insert(2).insert(4).insert(6).insert(12).insert(20).insert(26)
    check_val = 4
    contains = new_bst.contains(check_val)

    print(f"BST created ")

    if contains:
        print(f"The BST contains {check_val}" )
    else:
        print(f"The BST does not contain {check_val}")

    new_bst.delete(check_val)
    contains = new_bst.contains(check_val)

    print(f"Removed {check_val} from BST")

    if contains:
        print(f"The BST contains {check_val}")
    else:
        print(f"The BST does not contain {check_val}")


class BST:
    """BST class """

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        """ Inserts a value as node in BST """

        # track current node
        current_node = self

        while True:
            # when less traverse left
            if value < current_node.value:

                # If leaf node add value as BST
                if current_node.left is None:
                    current_node.left = BST(value)
                    break
                else:
                    # move left
                    current_node = current_node.left
            # when more traverse right
            else:

                # If leaf node add value as BST
                if current_node.right is None:
                    current_node.right = BST(value)
                    break
                else:
                    # move right
                    current_node = current_node.right

        # allow for chaining calls - test.insert(1).insert(2) etc
        return self

    def contains(self, value):
        """ Checks if BST contains a value - returns true/false"""
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
        """ remove nodes from BST """

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
                        current_node.right = current_node.right.right
                        current_node.left = current_node.right.left
                    else:
                        # root node with no children - IE: deleting the BST
                        current_node.value = None

                # has one or no child nodes - assign either left or right
                elif parent_node.left == current_node:

                    parent_node.left = current_node.left if current_node.left is not None else current_node.right
                elif parent_node.right == current_node:
                    parent_node.right = current_node.left if current_node.left is not None else current_node.right
                break

                return self

    def get_lowest_value(self):
        """ Gets the lowest value in a right side of BST"""
        # called on right sub tree
        current_node = self

        while current_node is not None:
            current_node = current_node.left

        return current_node.value


''' Run Program '''
main()


