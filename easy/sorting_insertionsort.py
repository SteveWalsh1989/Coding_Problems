

def insertion_sort(array):
    """ Insertion Sort Algorithm"""
    print(f'Unsorted: {array}')

    for i in range(1, len(array)):
        # k will be the current number trying to insert
        k = i

        while k > 0 and array[k] < array[k - 1]:
            swap(k, k - 1, array)
            k -= 1

    print(f'Sorted:   {array} \n')


def swap(a, b, array):
    """ swaps the elements of two positions within an array"""
    array[a], array[b] = array[b], array[a]


def main():
    """ Main function"""
    test_list = [8, 5, 2, 9, 5, 6, 3]
    test_list_2 = [-4, 5, 10, 8, -10, -6, -4, -2, -5, 3, 5, -4, -5, -1, 1, 6, -7, -6, -7, 8]

    # test
    print(f'Running Insertion Sort')
    insertion_sort(test_list)
    insertion_sort(test_list_2)


''' Run Program '''
main()
