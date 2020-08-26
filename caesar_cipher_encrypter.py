
"""
basic shift cipher
_______________________________________________________________
Uses a key to shift the value of letters within the aphabet by the value of the key.

IE:
Str : abc
Key: 2
Res: cde


lower case 1-z: 97 - 122 in unicode. Uppercase is 65 - 90


IN programming need to take into account the wrapping of values when reaching the end of the alphabet

Example below mainly deals with lowercase words which in unicode would be from 97 - 122. Uppercase is 65 - 90.

_______________________________________________________________
Space and Time Complexity

Space: O(N)
Time: O(N)
Where N is the number if letters


"""

def caesar_cipher_encrypter(str, key):
    """ Encrypts string by shifting chars by keys value"""
    encrypted_str = ""
    new_key = key % 26  # ensures no wrap around
    for letter in str:
        val = ord(letter)
        new_val = val + new_key
        if new_val > 122:
            new_val = chr(96 + new_val % 122)
        else:
            new_val = chr(new_val)

        encrypted_str += new_val

    print(f"Encrypting {str}: {encrypted_str}")


def main():
    """ Main function"""
    str = "abcxyz"
    key = 2
    caesar_cipher_encrypter(str, key)


''' Run Program '''
main()
