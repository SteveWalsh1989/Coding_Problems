"""

Lilah has a string, , of lowercase English letters that she repeated infinitely many times.

Given an integer, , find and print the number of letter a's in the first
letters of Lilah's infinite string.

For example, if the string  and , the substring we consider is ,
the first  characters of her infinite string.
There are  occurrences of a in the substring.

Function Description

Complete the repeatedString function in the editor below.
It should return an integer representing the number of
occurrences of a in the prefix of length  in the infinitely
 repeating string.

repeatedString has the following parameter(s):
- s: a string to repeat
- n: the number of characters to consider


Input Format
- The first line contains a single string, .
- The second line contains an integer, .

Constraints

For  of the test cases, .
Output Format

Print a single integer denoting the number of letter a's in the first
letters of the infinite string created by repeating  infinitely many times.

"""


def count_repeats(num_letters, letters):
    # declare return value
    count = 0

    # single value string optimiser
    if len(letters) == 1 and letters == 'a':
        return num_letters

    # max number if all letters in string were target 'a'
    for index, i in enumerate(num_letters * letters):
        # break clause
        if index >= num_letters:
            return count
        # counter
        elif i == 'a':
            count += 1


def main():
    """ Main function """

    letters = "x"
    num_repeats = 970770

    results = count_repeats(num_repeats, letters)

    print(f"Letters: {letters}, repeated indefinitely ")
    print(f"Results: {results} in the first  {num_repeats} letters")


''' Run Program '''
main()