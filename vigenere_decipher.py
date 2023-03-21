# Get input for message and key
message = input("Input message to decrypt: ")
key = input("Input key for decrypting: ")

# Convert to uppercase
message = message.upper()
key = key.upper()

# Decryption algorithm

# Convert message to list
message_char_list = list(message)

# Iterate through each character in the message
for i in range(len(message_char_list)):
    cur = message_char_list[i]
    curKey = key[i % len(key)]
    
    swap = (ord(cur)-ord(curKey))+65
    print(swap)
    if swap < 65:
        swap += 26
        print(swap)
    message_char_list[i] = chr(swap)

result = ''.join(message_char_list)

print ("Decrypted message:", result)