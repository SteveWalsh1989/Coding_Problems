

def palindrome_check(str):
    """Checks if a word/sentence is a palindrome"""

    # remove any white space for sentences
    cln_str = str.replace(" ", "")

    reversed_string = ""

    for i in reversed(range(len(cln_str))):
        reversed_string += cln_str[i]

    is_palindrome = reversed_string == cln_str

    if is_palindrome:
        print(f"'{cln_str}' is a palindrome.")
    else:
        print(f"'{cln_str}' is not a palindrome.")


def main():
    """ Main function"""
    str_1 = "racecar"
    str_2 = "gigantic"
    str_3 = "borrow or rob"

    palindrome_check(str_1)
    palindrome_check(str_2)
    palindrome_check(str_3)


''' Run Program '''
main()
