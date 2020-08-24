

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



