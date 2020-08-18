# lower case 1-z: 97 - 122 in unicode. Uppercase is 65 - 90


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
