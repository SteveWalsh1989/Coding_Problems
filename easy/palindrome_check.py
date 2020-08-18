

def palindrome_check(word):
    """Checks if a word is a palindrome"""

    reversed_string = ""

    for i in reversed(range(len(word))):
        reversed_string += word[i]

    is_palindrome = reversed_string == word

    if is_palindrome:
        print(f"'{word}' is a palindrome.")
    else:
        print(f"'{word}' is not a palindrome.")


def main():
    """ Main function"""
    word_1 = "racecar"
    word_2 = "gigantic"

    palindrome_check(word_1)
    palindrome_check(word_2)


''' Run Program '''
main()
