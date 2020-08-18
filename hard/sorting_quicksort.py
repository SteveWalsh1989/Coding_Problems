

def quicksort(array):
    """ Quick Sort Algorithm"""
    print(f'Unsorted: {array}')

    quicksort_helper(array, 0, len(array) - 1)

    print(f'Sorted: {array}')

    return array


def quicksort_helper(array, start_index, end_index):
    """helper function for quick sort"""
    # base case
    if start_index >= end_index:
        return

    # Set up pivot
    pivot_index = start_index

    # Set up left and right indexes
    left_index = start_index + 1
    right_index = end_index

    # apply quick sort main logic
    while right_index >= left_index:
        if array[left_index] > array[right_index] and array[right_index] < array[pivot_index]:
            swap(left_index, right_index, array)
        if array[left_index] <= array[pivot_index]:
            left_index += 1
        if array[right_index] >= array[pivot_index]:
            right_index -= 1

    # swap pivot and right index
    swap(pivot_index, right_index, array)

    # For Space complexity work on smaller array first
    left_subarray_is_smaller = right_index - 1 - start_index < end_index - (right_index + 1)
    if left_subarray_is_smaller:
        quicksort_helper(array, start_index, right_index - 1)
        quicksort_helper(array, right_index + 1, end_index)
    else:
        quicksort_helper(array, right_index + 1, end_index)
        quicksort_helper(array, start_index, right_index - 1)


def swap(a, b, array):
    """ swaps the elements of two positions within an array"""
    array[a], array[b] = array[b], array[a]


def main():
    """ Main function"""
    test_list = [8, 5, 2, 9, 5, 6, 3]
    test_list_2 = [-4, 5, 10, 8, -10, -6, -4, -2, -5, 3, 5, -4, -5, -1, 1, 6, -7, -6, -7, 8]

    # test
    print(f'Running Selection Sort')
    quicksort(test_list)
    quicksort(test_list_2)


''' Run Program '''
main()
