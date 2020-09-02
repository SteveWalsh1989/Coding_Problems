"""
Basic Sorting Algorithm to sort list in ascending order

Ex:
Inital:  [8, 5, 2, 9, 5, 6, 3]
Goal : [2, 3, 5, 5, 6, 8, 9]

Diving the list into two sub lists within the array
 - not actually creating new arrays

List 1 - unsorted items
List 2 - sorted items

Intially all items are in List 1
Each time we iterate through list 1 we will search for the smallest number
- when found we append it to the start list 2


 [ 8, 5, 2, 9, 5, 6, 3]
   |
start with 8: 8 > 5 = move

 [ 8, 5, 2, 9, 5, 6, 3]
        |
5: 5 > 2 = move

 [ 8, 5, 2, 9, 5, 6, 3]
            |
2: 2 < 9  = keep 2 as smallest
2: 2 < 5  = keep 2 as smallest
2: 2 < 6  = keep 2 as smallest
2: 2 < 3  = keep 2 as smallest

End iteration 1: 2 is the smallest number in this list
- swap the 2 with first element in the unsorted list which is it’s final position
[2, 5, 8, 9, 5, 6, 3]

Keep going with iteration.

End result : [2, 3, 5, 5, 6, 8, 9]

Space and Time complexity:
Space: O(1)
- using the same array

Time: O(n^2)
- where n = lenght of the array
- we have to keep reinterating through the unsorted sub list


"""
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
