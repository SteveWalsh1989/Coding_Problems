"""
Check if a sequence contains a subsequence

seq_1 = [3, 5, 2, -1, 7, 8, 9, -5]
sub_seq_1 = [-1, 3, 5, 7] - true
sub_seq_2 = [-1, 3, 6, 7] - false

————————————————————————————————————
Quick option would be to iterate through sub sequence and cehck if each value is within the main sequence

- Account for - where val in sub sequence appears more than once


"""


def validate_subsequence(seq, sub_seq):
    """ Validates if sequence contains subsequence"""
    is_valid = True

    if seq == sub_seq:
        return False

    for i in sub_seq:
        if i not in seq:
            is_valid = False
        else:
            seq.remove(i)

    if is_valid:
        print(f"{sub_seq} is a sub sequence of {seq}")
    else:
        print(f"{sub_seq} is not a sub sequence of {seq}")


def main():
    """ Main function"""
    seq_1 = [3, 5, 2, -1, 7, 8, 9, -5]
    sub_seq_1 = [-1, 3, 5, 7]
    sub_seq_2 = [-1, 3, 6, 7]
    sub_seq_3 = [-1, 3, 5, 5]

    validate_subsequence(seq_1, sub_seq_1)
    validate_subsequence(seq_1, sub_seq_2)
    validate_subsequence(seq_1, sub_seq_3)


''' Run Program '''
main()





