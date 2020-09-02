

def find_largest_numbers(array, num_elements):
    """Returns ordered list of largest elements"""
    largest_numbers = []

    for _ in range(num_elements):
        largest = max(array)
        largest_numbers.insert(0, largest)
        array.remove(largest)

    return largest_numbers


def main():
    """ Main function"""
    arr = [2, 56, 23, 41, 18, 12, 6, 32, 45, 98, 41 ]

    num_vals = 3
    res = find_largest_numbers(arr, num_vals)

    print(f"The {num_vals} largest values within {arr} are {res}")


''' Run Program '''
main()

