"""

Write a function that takes in an array of integers and returns a boolean representing whether the array is monotonic.

The array can contain duplicate values
__________________________________________________________________
Monotonic - entire array is either increasing or decreasing

IE:
arr = [5]
arr1 = [-1, -6, -99, - 120, -230, -999]
arr2 = [1, 3, 5, 5, 23, 45, 67, 98, 122]
__________________________________________________________________

If single element/ empty array
- return true
Since the array can contain duplicate values
- cannot just take the first two elements to determine the direction
- Need to check for flats and can use a helper function
  - Checks the direction and then can compare current and previous values to see if breaks direction
__________________________________________________________________
Space and Time Complexity:

Space: O(1)
Time:  O(N)
__________________________________________________________________
Code:

"""


def check_monotonic_array(array):
    """Check ifs an array is monotonic"""

    # if empty/ single element array then its monotonic
    if len(array) <= 2:
        return True
    # check which direction array about be going if monotonic
    direction = array[1] - array[0]

    for i in range(1, len(array)):

        # check_flats
        if direction == 0:
            direction = array[i] - array[i - 1]

        if check_flats(direction, array[i - 1], array[i]):
            return False

    return True


def check_flats(direction, last_val, current_val):
    """ checks when a subsequent number in array is not the same"""

    difference = current_val - last_val

    if direction > 0:
        return difference < 0
    return difference > 0


def main():
    """ Main function"""
    # monotonic arrays
    arr = [5]
    arr1 = [-1, -6, -99, - 120, -230, -999]
    arr2 = [1, 3, 5, 23, 45, 67, 98, 122]

    # Non-monotonic  arrays
    arr3 = [-1, -6, -99, - 120, -98, -999]
    arr4 = [1, 3, 5, 23, 45, 67, 98, 12]

    lists = []
    lists.append(arr)
    lists.append(arr1)
    lists.append(arr2)
    lists.append(arr3)
    lists.append(arr4)

    for list in lists:
        res = check_monotonic_array(list)
        if res:
            print(f"The  array {list} is monotonic")
        else:
            print(f"The  array {list} is not monotonic")


''' Run Program '''
main()

