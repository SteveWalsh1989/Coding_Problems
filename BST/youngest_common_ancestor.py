"""
Given three inputs which are instances of a tree class where
each node has an ancestor property pointing to their youngest
ancestor where the:
First input is top ancestor in the tree and
the other two inputs are descendants in the tree.

Write a function that returns the youngest common ancestor of the two descendant inputs
________________________________________________________________

IE:

0              A
             /   \
1         B       C
        /   \    /   \
2     D      E  F     G
     /  \
3   H    I


Input: A, E, I
Res:  B
____________________________________________________________________

Space and Time Complexity

Space: O(1)

Time: O(D)
- where d is depth of tree

_____________________________________________________________________
"""


def get_youngest_ancestor(top_ancestor, descendant_1, descendant_2):
    """ returns youngest common ancestor between two descendants in an ancestor tree"""



def create_tree():
    """ creates and returns new tree"""
    ancestor_trees = {}
    for letter in list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        ancestor_trees[letter] = ancestor_trees(letter)
        return ancestor_trees


def main():
    """ main function """

    # create ancestor tree BST
    ancestor_tree = create_tree()
    ancestor_tree["A"].addDescendants(ancestor_tree["B"], ancestor_tree["C"])
    ancestor_tree["B"].addDescendants(ancestor_tree["D"], ancestor_tree["E"])
    ancestor_tree["D"].addDescendants(ancestor_tree["H"], ancestor_tree["I"])
    ancestor_tree["C"].addDescendants(ancestor_tree["F"], ancestor_tree["G"])

    # Set inputs
    input_1 = ancestor_tree["A"]
    input_2 = ancestor_tree["E"]
    input_3 = ancestor_tree["I"]

    # call function
    res = get_youngest_ancestor(input_1, input_2,  input_3 )

    # print results
    print(f"The youngest common ancestor between {input_1} and {input_2} is {res}")


# This is the class of the input ancestor tree.
class Trees:
    def __init__(self, value):
        self.value = value
        self.ancestor = None

    def add_descendant(self, *descendants):
        for descendant in descendants:
            descendant.ancestor = self


''' Run Program '''
main()