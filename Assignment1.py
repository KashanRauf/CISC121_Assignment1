import re

# Get user input for plaintext and key.
plaintext = input("Input plaintext to encrypt: ")
key = input("Input key for encrypting: ")

# Convert the plaintext and key to uppercase.
plaintext = plaintext.upper()
key = key.upper()

# Use a regex to remove non-letters.
regex = re.compile('[^A-Z]')
processed_text = regex.sub("", plaintext)

# Algorithm for encrypting processed_text to key.

# Converting processed_text to a list of characters because strings are immutable.
text_char_list = list(processed_text)

# Iterating through each character in the list.
for i in range(len(text_char_list)) :
    # ASCII values and ord() function are used to calculate the expected value of each character.
    cur = text_char_list[i]
    curKey = key[i % len(key)]
    # It is more efficient to calculate the character to encode than create a Vigenere table iteratively.
    swap = (ord(cur)+ord(curKey))-65
    if swap > 90 :
        swap -= 26
    text_char_list[i] = chr(swap)
# Converting the list back into a string after encoding.
processed_text = ''.join(text_char_list)

# Outputs the encrypted result.
print ("Encrypted message:", processed_text)


'''
    Explanation of values used in algorithm:
    - ASCII values are used with the ord() function to calculate encoded character.
    - The first value for capital letters is 65 (A), and the last is 90 (Z)
    - The value 65 is subtracted in line 38 to ensure the value remains as a capital letter.
    - If the value of 'swap' is still greater than 90, 26 is subtracted to ensure the value is correct.
    - This number is used because there are 26 letters in the alphabet
'''