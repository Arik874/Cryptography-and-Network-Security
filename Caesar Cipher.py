def caesar_cipher(text, shift):
    encrypted_text = ""
    
    for char in text:
        if char.isupper():
            encrypted_char = chr(((ord(char) - 65 + shift) % 26) + 65)
        elif char.islower():
            encrypted_char = chr(((ord(char) - 97 + shift) % 26) + 97)
        else:
            encrypted_char = char
        encrypted_text += encrypted_char
    
    return encrypted_text

def caesar_decipher(text, shift):
    return caesar_cipher(text, -shift)

# Get user input for plaintext and shift
plaintext = input("Enter the plaintext: ")
shift = int(input("Enter the shift value (an integer): "))

encrypted_text = caesar_cipher(plaintext, shift)
decrypted_text = caesar_decipher(encrypted_text, shift)

print("Plaintext:", plaintext)
print("Encrypted:", encrypted_text)
print("Decrypted:", decrypted_text)
