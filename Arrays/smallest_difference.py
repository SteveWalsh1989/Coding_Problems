"""
Given two, non empty arrays of integers, return an array containing two elements, one from each of the original arrays whos absolute difference is the smallest possible. The position of the first element in the returned array must be from the first of the two original arrays
__________________________________________________________________

IE:

Arr_1 = [-6, 23, 4, 15, 26, 54, -11]
Arr_2 = [-19, 1, 11, 28, 32, 96, 38]

Res: = [26, 28]
__________________________________________________________________

- Sorting the arrays makes it easier since it’s more likely smaller numbers would have closer absolute zero than largely distanced numbers
- Need to have index for where we are in each array
- Need to store current smallest vans
- Need the result to have both
- If num_1 > num_2 need to increment num_2 pointer as it gives it best chance of getting closer to num_1
- If num_1 = num_2 then absolute difference is 0 so can return
__________________________________________________________________
Space and Time Complexity


Space: O(1)

Time: O(NlogN + MlogM)
-  Where N and M are lengths of arr1 and arr2 respectively
-  The sorting which adds to the time and gives it the NlogN
__________________________________________________________________
"""


def smallest_difference(arr_1, arr_2):
    """ returns pair with smallest absolute difference """
    # initialise needed vars
    res = []
    smallest = float("inf")
    current = float("inf")

    # sort arrays
    arr_1.sort()
    arr_2.sort()

    # create index for searching each array
    arr_1_idx = 0
    arr_2_idx = 0

    # iterate over arrays within each range
    while arr_1_idx < len(arr_1) and arr_2_idx < len(arr_2):
        # store current numbers
        num_1 = arr_1[arr_1_idx]
        num_2 = arr_2[arr_2_idx]

        # compare
        if num_1 < num_2:
            current = num_2 - num_1
            arr_1_idx += 1
        elif num_1 > num_2:
            current = num_1 - num_2
            arr_2_idx += 1
        else:
            return [num_1, num_2]

        # check if smallest
        if smallest > current:
            smallest = current
            res = [num_1, num_2]
    return res


def main():
    """ Main function"""
    arr_1 = [-6, 23, 4, 15, 26, 54, -11]
    arr_2 = [-19, 1, 11, 27, 32, 96, 38]

    res = smallest_difference(arr_1, arr_2)

    print(f"The values with the smallest absolute difference within {arr_1} and {arr_2} are {res}")


''' Run Program '''
main()



