""":arg

Basic Sorting Algorithm to sort list in ascending order

Ex:
Inital:  [8, 5, 2, 9, 5, 6, 3]
Goal : [2, 3, 5, 5, 6, 8, 9]


Not a very performant sorting algorthm but relatively simple to implement

Revoles around taking the first item in the array and creating a new ’sorted’ list with this element and then inserting the elements into this list from the original resulting in a new sorted array

Start with the number 8
[8]
We then start at the rest of numbers and add them to the new list of [8]
So we get [5, 8]

Next is 2
compare with 8
 - since 2 < 8 swap
compare with 5
- since 2 < 5 swap
So we have [2, 5, 8]

Next is 9
compare with 8
- since 9 > 8 - insert at end
So we have [2, 5, 8, 9 ]

And keep going until [2, 3, 5, 5, 6, 8, 9]


Space and Time Complexity:
Space: O(1)
- it all occurs within the original array

Time: O(n^2)
- where n is lenght of input array


"""

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
