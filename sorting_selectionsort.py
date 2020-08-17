
def selection_sort(array):
    """ Selection Sort Algorithm"""
    print(f'Unsorted: {array}')

    # keep track of index of first number in unsorted sub list
    current_index = 0

    while current_index < len(array) - 1:
        # find index of smallest number
        smallest_index = current_index

        # loop over unsorted list
        for i in range(current_index + 1, len(array)):

            # check if current smallest is bigger than checked index
            if array[smallest_index] > array[i]:

                # If true set new smallest index
                smallest_index = i

        # swap the smallest number with current index
        swap(current_index, smallest_index, array)
        current_index += 1

    print(f'Sorted:   {array} \n')


def swap(a, b, array):
    """ swaps the elements of two positions within an array"""
    array[a], array[b] = array[b], array[a]


def main():
    """ Main function"""
    test_list = [8, 5, 2, 9, 5, 6, 3]
    test_list_2 = [-4, 5, 10, 8, -10, -6, -4, -2, -5, 3, 5, -4, -5, -1, 1, 6, -7, -6, -7, 8]

    # test
    print(f'Running Selection Sort')
    selection_sort(test_list)
    selection_sort(test_list_2)


''' Run Program '''
main()
