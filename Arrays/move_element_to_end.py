"""
Given array of integers and integer. Create function that mopves all intances of that integer to the end of the array.

IE:
arr = [-6, 23, 4, 15, 26, 54, -11, 4, 66, -12, 14, 25, 4, 112, 20]
val = 4
res: [-6, 23, 15, 26, 54, -11, 66, -12, 14, 25, 112, 20, 4, 4, 4]
__________________________________________________________________
"""


def move_element(array, val):
    """ Moves all elements from provided val to the end of the provided array"""

    for num in array:
        if num == val:
            array.insert(len(array) , val)
            array.remove(num)


def main():
    """ Main function"""
    arr = [-6, 23, 4, 15, 26, 54, -11, 4, 66, -12, 14, 25, 4, 112, 20]
    val = 4
    
    move_element(arr, val)

    print(f"Arrays {arr} has been changed by moving the value {val} to the end")


''' Run Program '''
main()


