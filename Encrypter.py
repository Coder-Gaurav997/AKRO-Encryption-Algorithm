from random import choice
from string import ascii_letters

# ---------------------------------------------------
# INPUT
# ---------------------------------------------------
text = input("Enter the text to encrypt: ")
key = "KEY"


# ---------------------------------------------------
# Convert text into comma-separated ASCII values
# Example: "Hi" -> "72,105"
# ---------------------------------------------------
def convert_to_ascii(text):
    ascii_values = []

    for char in text:
        ascii_values.append(str(ord(char)))

    return ",".join(ascii_values)


# ---------------------------------------------------
# Add repeating KEY ASCII values to text ASCII values
# KEY repeats automatically (KEYKEYKEY...)
# ---------------------------------------------------
def add_key_to_ascii(ascii_text, key):
    ascii_list = ascii_text.split(',')
    encrypted = []

    key_length = len(key)

    for i in range(len(ascii_list)):
        text_ascii = int(ascii_list[i])
        key_ascii = ord(key[i % key_length])  # repeat key

        encrypted_value = text_ascii + key_ascii
        encrypted.append(str(encrypted_value))

    return ",".join(encrypted)


# ---------------------------------------------------
# Insert random junk letters after every 3rd element
# Adds obfuscation layer
# ---------------------------------------------------
def add_random_junk(encrypted_text):
    ascii_list = encrypted_text.split(',')
    result = []

    for i in range(len(ascii_list)):
        result.append(ascii_list[i])

        # After every 3rd value insert random letter
        if (i + 1) % 3 == 0:
            random_letter = choice(ascii_letters)
            result.append(random_letter)

    return ",".join(result)


# ---------------------------------------------------
# Reverse the entire encrypted sequence
# Final scrambling step
# ---------------------------------------------------
def reverse_encrypted_str(junk_added_text):
    encrypted_list = junk_added_text.split(',')
    reversed_list = encrypted_list[::-1]
    return ",".join(reversed_list)


# ---------------------------------------------------
# ENCRYPTION PIPELINE
# ---------------------------------------------------
ascii_text = convert_to_ascii(text)
encrypted_text = add_key_to_ascii(ascii_text, key)
junk_added_text = add_random_junk(encrypted_text)
reversed_text = reverse_encrypted_str(junk_added_text)

print("The encrypted text is:", reversed_text)