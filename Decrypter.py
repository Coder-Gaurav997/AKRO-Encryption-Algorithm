# ---------------------------------------------------
# DECRYPTER FOR YOUR CUSTOM ENCRYPTION
# ---------------------------------------------------

encoded_text = input("Enter the encrypted text: ")
key = "KEY"


# ---------------------------------------------------
# Step 1: Reverse back to original order
# ---------------------------------------------------
def reverse_back(text):
    parts = text.split(',')
    return parts[::-1]


# ---------------------------------------------------
# Step 2: Remove junk letters (added after every 3rd)
# Pattern: 3 numbers + 1 letter repeating
# ---------------------------------------------------
def remove_random_junk(reversed_list):
    cleaned = []

    for i, item in enumerate(reversed_list):
        # every 4th item is junk (index 3,7,11,...)
        if (i + 1) % 4 != 0:
            cleaned.append(item)

    return cleaned


# ---------------------------------------------------
# Step 3: Subtract KEY ASCII values
# ---------------------------------------------------
def subtract_key(ascii_list, key):
    decrypted_ascii = []
    key_length = len(key)

    for i in range(len(ascii_list)):
        value = int(ascii_list[i])
        key_ascii = ord(key[i % key_length])

        original_value = value - key_ascii
        decrypted_ascii.append(original_value)

    return decrypted_ascii


# ---------------------------------------------------
# Step 4: Convert ASCII back to string
# ---------------------------------------------------
def ascii_to_text(ascii_values):
    characters = []

    for num in ascii_values:
        characters.append(chr(num))

    return "".join(characters)


# ---------------------------------------------------
# DECRYPTION PIPELINE
# ---------------------------------------------------
reversed_list = reverse_back(encoded_text)
clean_ascii = remove_random_junk(reversed_list)
original_ascii = subtract_key(clean_ascii, key)
decoded_text = ascii_to_text(original_ascii)

print("Decrypted text:", decoded_text)