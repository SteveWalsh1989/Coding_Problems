"""
Sorting Algorithm to sort list in ascending order
————————————————————————————————
Ex:
Inital:  [8, 5, 2, 9, 5, 6, 3]
Goal : [2, 3, 5, 5, 6, 8, 9]
————————————————————————————————
- Quick to run
- Often used in production
————————————————————————————————
Works using a pivot value
- can be selected at random
- could be first/ last value in array

Every number that is smaller than the pivot move to the left of the pivot
Every number that is bigger than the pivot move to the right of the pivot
At the end of the iteration then the pivot is in it’s final position within the array
Repeat until uits all sorted
 ————————————————————————————————

Ex:
Inital:  [8, 5, 2, 9, 5, 6, 3]

Pivot - first value in the array - 8
 [8, 5, 2, 9, 5, 6, 3]
  P

We then have Left and Right pointers which will be at the 5 and 3
 [8, 5, 2, 9, 5, 6, 3]
  P  L                   R

While the right pointer is greater than or euqal to the left pointer then we haven’t finished iterating

For each pass
Is the left number greater than the pivot number and is the right number smaller than the pivot number

if yes
- we swap those two numbers

1 ___________________
[8, 5, 2, 9, 5, 6, 3]
 P  L                   R
- L is not greater than the pivot, R is greater than the pivot - so it stays

2 ___________________
Increment L
 [8, 5, 2, 9, 5, 6, 3]
  P      L              R
- Both are smaller than the pivot - stay the same

3 ___________________
Increment L
 [8, 5, 2, 9, 5, 6, 3]
  P           L          R
Now: L(9) is greater than P(8) and R(3) is smaller than P
- So they are swapped
 [8, 5, 2, 3, 5, 6, 9]
  P           L          R

4 ___________________
Increment L
 [8, 5, 2, 3, 5, 6, 9]
  P               L      R
- L is smaller than P(8), stays,  Now R(9) is greater than P so that moves one index to the left
 [8, 5, 2, 3, 5, 6, 9]
  P               L  R

5 ___________________
Increment L
 [8, 5, 2, 3, 5, 6, 9]
  P                   R
                       L
R(6) is smaller than P, L(6) is smaller than P
- left moves to the right
 [8, 5, 2, 3, 5, 6, 9]
  P                   R  L
Now we stop as R is no longer greater than or equal to L
So we then swap the P and the R
 [6, 5, 2, 3, 5, 8, 9]
   P                  R  L
We know now that R(8) is in it’s final sorted position.

6 ___________________
We work on the two sub arrays that have been defined to the left and right of the pivoted value 8
 [6, 5, 2, 3, 5, 8, 9]
L sub array-  [6, 5, 2, 3, 5]
R sub array- [9]

We will do the quick sort then starting on the smaller of the two arrays - helps with space complexity
For an array of 1 then we know that it is already sorted so in this example both 8 and 9 are in their final positons
[6, 5, 2, 3, 5, 8, 9]

7 - 10___________________
Do the quick sort method on the longer sub array L sub array-  [6, 5, 2, 3, ]
L sub array-  [6, 5, 2, 3, 5 ]
                       P  L       R
L < P > R
- move L to the right
  [6, 5, 2, 3, 5, 8, 9 ]
    P      L      R
L < P > R
- move L to the right
  [6, 5, 2, 3, 5, 8, 9  ]
    P          L  R
L < P > R
- move L to the right
  [6, 5, 2, 3, 5, 8, 9  ]
    P          L  R
L < P > R
- move L to the right
  [6, 5, 2, 3, 5, 8, 9  ]
    P              R
                     L
- move L to the right
  [6, 5, 2, 3, 5, 8, 9  ]
    P              R
                         L
Swap R and P  as L > R - this is the final position for 6
  [5, 5, 2, 3, 6, 8, 9  ]

11___________________
Quicksort on sub array [5, 5, 2, 3]
  [5, 5, 2, 3, 6, 8, 9  ]
   P  L      R
L < 5 > R
- move L to the right
  [5, 5, 2, 3, 6, 8, 9  ]
   P       L  R
L < 5 > R
- move L to the right
  [5, 5, 2, 3, 6, 8, 9  ]
   P           R
                 L
L < 5 > R
- move L to the right
  [5, 5, 2, 3, 6, 8, 9  ]
   P           R
                     L
L > R
- swap P and R
- final position for new P -   [3, 5, 2, 5, 6, 8, 9  ]


12___________________
Keep repeating process
Result - [2, 3, 5, 5, 6, 8, 9  ]

_________________________________________________________
_________________________________________________________
Time and Space Complexity
Time:
- In worst case when you position pivot into one tiny array and one huge array and it keeps happening when trying to do it on each sub array then it pretty much O(n^2)
- In the best case O(N log(n))
- Average case also comes to  O(N log(n))

Space:
- O( log(n)) as in order to to implement quicksort, recursion is needed and is done in place typically
- this is due to making sure to use quicksort on the smaller array of the two first to try and minimise the amount of space used on the call stack in memory
- using it then on the remaining single array through tail recurison that most compilers provide it helps with space saving on the call stack

_________________________________________________________
_________________________________________________________

"""


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
