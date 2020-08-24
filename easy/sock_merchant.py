

def check_socks(arr, length):
    """ checks for number of pairs of values within an array"""
    pairs = 0

    # sort list
    arr.sort()
    i = 0

    # iterate
    while i < (length - 1):
        # set values
        current = arr[i]
        next = arr[i + 1]

        # check if the same sock or different
        if next == current:
            pairs += 1
            i += 2
        else:
            i += 1

    return pairs


def main():
    """ Main function"""
    arr = [2, 3, 3, 1, 2, 1, 4, 2, 2, 2, 1]

    res = check_socks(arr, len(arr) )

    print(f"The  array {arr} has {res} pairs")


''' Run Program '''
main()
