"""
Basic Sorting Algorithm to sort list in ascending order

Ex:
Inital:  [8, 5, 2, 9, 5, 6, 3]
Goal : [2, 3, 5, 5, 6, 8, 9]

How:
- Iterate through list
- compare element with the next element
- if the same - move one
- If element is smaller than next element - move on
- if element is larger than next element - swap, note the swap then move on
When at the end of the array - check if swaps are done
- if swaps where done - run through again
- if no swaps were done - array is sorted

Start of iteration 1
8, 5 - swap - 5, 8
8, 2 - swap - 5, 2, 8
8, 9 - keep - 5, 2, 8, 9
9, 5 - swap - 5, 2, 8, 5, 9
9, 6 - swap - 5, 2, 8, 5, 6, 9
9, 3 - swap-  5, 2, 8, 5, 6, 3, 9
We now have the final position of 9
End of iteration 1: [5, 2, 8, 5, 6, 3, 9]

Start of iteration 2
5, 2 - swap - 2, 5
5, 8 - keep - 2, 5, 8
8, 5 - swap - 2, 5, 5, 8
8, 6 - swap - 2, 5, 5, 6, 8
8, 3 - swap - 2, 5, 5, 6, 3, 8
We now have the final position of 8
End of iteration 2: [2, 5, 5, 6, 3, 8, 9 ]

Start of iteration 3
2, 5 - keep - 2, 5
5, 5 - keep - 2, 5, 5
5, 6 - keep - 2, 5, 5, 6
6, 3 - swap - 2, 5, 5, 3, 6
We now have the final position of 6
End of iteration 3: [2, 5, 5, 3, 6, 8, 9 ]

The next two iterations are just to get the 3 to be in the right place
total number of iterations = 5
End result:  [2, 3, 5, 5, 6, 8, 9]


Space and Time Complexity:
Space: O(1)
- as the algorithm runs in space, everything is done within the input array
- no additional memory is used

Time: o(n^2)
- where n ios the lenght of the array
- We are looping through the array multiple times until sorted
- In the worst case it would need to go through every possible combination which would be n2
"""

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
