






def main():
    """ Main function"""

    res = smallest_difference(arr_1, arr_2)

    print(f"The values with the smallest absolute difference within {arr_1} and {arr_2} are {res}")


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # track current node
        current_node = self

        while True:
            # when less traverse left
            if value < current_node:

                # If leaf node add value as BST
                if current_node.left is None:
                    current_node.left = BST(value)
                    break
            else:
                # move left
                current_node = current_node.left

            # when more traverse right
            if value <= current_node:

                # If leaf node add value as BST
                if current_node.right is None:
                    current_node.right = BST(value)
                    break
            else:
                # move right
                current_node = current_node.right


    def contains(self, value):
        pass

    def delete(self, value):
        pass


''' Run Program '''
main()


