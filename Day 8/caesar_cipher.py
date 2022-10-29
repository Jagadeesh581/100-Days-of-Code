def caesar(caesar_message, caesar_shift, direction):
    """encrypt or decrypt yhe input message and prints the message"""
    cipher = ""
    if direction == "decode":
        caesar_shift *= -1
    for letter in caesar_message:
        if letter.isnumeric() or letter.isspace():
            cipher += letter
        elif letter.isupper():
            cipher += chr((ord(letter) + caesar_shift - 65) % 26 + 65)
        else:
            cipher += chr((ord(letter) + caesar_shift - 97) % 26 + 97)

    print(f"The {direction} text is {cipher}")


end = False

# continue if user types 'yes'.
while not end:
    encryption_or_decryption = input("Type 'encode' to encrypt or 'decode' to decrypt: \n").lower()
    message = input("Type your message: \n")
    shift = int(input("Type the shift number: \n"))

    caesar(caesar_message=message, caesar_shift=shift, direction=encryption_or_decryption)

    decision = input("Type 'yes' to continue or 'no' to stop: ").lower()
    if decision == "yes":
        end = False
    else:
        end = True
