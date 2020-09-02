"""

__________________________________________________________________

Goal: Solving the maximum sub array problem

A function that takes in a non-empty array of integers and returns
- the max sum that can be obtained by summing all integers in a non-empty sub array
- sub array can only contain adjacent numebers

IE: [ 2, 6, -9, 3, 1, -2, 7, 2, 4, -9, 3, 1, 6, -5, 4]

Res: 19 from [ 3, 1, -2, 3, 7, 2, 4, -9, 3, 1, 6 ]
__________________________________________________________________
Time and Space Complexity
Time: O(N)
Spac: O(1)
_________________________________________________________________

"""


def kadanes_algorithm(array):
    """ returns sum of highest value sub array """

    # declare max for current index
    highest_sum_at_index = array[0]

    # declare max sum
    highest_sum = array[0]

    # iterate through rest of values
    for val in array[1:]:

        # check if number is viable to add or to start new sub array
        highest_sum_at_index = max(val, highest_sum_at_index + val)

        # check if updating highest sum or keeping existing
        highest_sum = max(highest_sum, highest_sum_at_index)

    return highest_sum


def main():
    """ Main function"""

    # res should be 16 [ 3, 1, -2, 7, 2, 4, -9, 3, 1, 6]
    arr = [2, 7, -9, 3, 1, -2, 7, 2, 4, -9, 3, 1, 6, -5, 4]

    res = kadanes_algorithm(arr)

    print(f"The sum of the maximum sub array within {arr} is  {res}")


''' Run Program '''
main()


