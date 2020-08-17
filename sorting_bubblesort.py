

def bubble_sort(array):
    """ BubbleSort Algorithm"""
    print(f'Unsorted: {array}')

    # Assume array is not sorted
    is_sorted = False

    counter = 0  # small optimisation to count iterations by ignoring final position of elements sorted

    while not is_sorted:
        is_sorted = True

        for i in range(len(array) - 1 - counter):
            if array[i] > array[i+1]:
                swap(i, i+1, array)
                is_sorted = False

        counter += 1

    print(f'Sorted:   {array} \n')


def swap(a, b, array):
    """ swaps the elements of two positions within an array"""
    array[a], array[b] = array[b], array[a]


def main():
    """ Main function"""
    test_list = [8, 5, 2, 9, 5, 6, 3]
    test_list_2 = [-4, 5, 10, 8, -10, -6, -4, -2, -5, 3, 5, -4, -5, -1, 1, 6, -7, -6, -7, 8]

    # test
    print(f'Running Bubble Sort')
    bubble_sort(test_list)
    bubble_sort(test_list_2)

''' Run Program '''
main()
