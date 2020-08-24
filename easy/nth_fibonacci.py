

def nth_fibonacci(n):
    """ Returns nth value in fibonacci sequence f(n) = f(n-1)  + f(n-2)"""

    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return nth_fibonacci(n - 1) + nth_fibonacci(n - 2)


def main():
    """ Main function"""

    n = 6
    res = nth_fibonacci(n)

    print(f"The {n}th number in the fibonacci sequence is {res}")


''' Run Program '''
main()

