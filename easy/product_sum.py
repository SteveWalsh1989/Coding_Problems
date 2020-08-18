

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





