
"""
A function that takes in an array of distinct intergers and an interger that represents a target value.
- The goal is to return an array that contains doubles of integers from the array whos sum equals the target value
- Is no doubles found, return empty array
- array contains at most one double
__________________________________________________________________

IE:
arr - [3, 5, -4, 8, 11, 1, -1, 6]
target - 10

Res: [-1, 11]
__________________________________________________________________
"""


def two_number_sum(arr, target):
    """ returns array of double whos sum equals target """
    res = []

    for num_1 in arr:
        for num_2 in arr:
            if num_1 + num_2 == target and num_1 != num_2:
                # add to res and return since there is only one double
                res.append(num_1)
                res.append(num_2)
                return res
    return res


def main():
    """ Main function"""
    arr = [14, 3, 6, -1, 12, 13, 11, 18, 1]
    target = 10

    res = two_number_sum(arr, target)

    print(f"The values within  {arr} whose product is  {target} are {res}")


''' Run Program '''
main()



