"""
The product sum problem involves being able to create a function that is able to analyse a special array of values and provide the sum of each elements

A special array is one that contains sub arrays and here the sums of the values within sub arrays are to be multipled by their depth within the special array

IE:
arr = [ 5, 2, [7, -1], 3, [6  [-13, 8], 4]]

Calculation is: 1(5 + 7) + 2( 7 -1) + 1(3) + 2(6 + 3(-13 + 8) + 4)

Res = 12


This is a classic recursion problem.
- declare sum as 0
- Iterate through the special array
- check if the element is a list
—-- if list: call function recursively and increment the multiplier and return val as sum
—--if not list: add value to sum
- return the sum * multiplier
________________________________________________________________________________

Space and Time Complexity

Space: O(D)
- where d is the maximum depth of sub arrays

Time: O(N)
- where N is total number of elements in the array, counting all elements from sub arrays



"""

def product_sum(array, multiplier=1):
    """ Calculates the product su mof special arrays"""
    arr_sum = 0
    for val in array:
        if type(val) is list:

            # call and add to sum recursively
            arr_sum += product_sum(val, multiplier + 1)
        else:
            # add single elements value
            arr_sum += val

    return arr_sum * multiplier


def main():
    """ Main function"""
    arr = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]

    res = product_sum(arr)

    print(f"The product sum of {arr} is {res}")


''' Run Program '''
main()





