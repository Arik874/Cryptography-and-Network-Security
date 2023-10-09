def rail_fence_encrypt(text, key):
    cycle = 2 * (key - 1)
    encrypted_text = ''

    for i in range(key):
        for j in range(i, len(text), cycle):
            encrypted_text += text[j]
            if 0 < i < key - 1 and j + cycle - 2 * i < len(text):
                encrypted_text += text[j + cycle - 2 * i]
                
    return encrypted_text


def rail_fence_decrypt(encrypted_text, key):
    cycle = 2 * (key - 1)
    decrypted_text = [' '] * len(encrypted_text)
    index = 0

    for i in range(key):
        for j in range(i, len(encrypted_text), cycle):
            decrypted_text[j] = encrypted_text[index]
            index += 1
            if 0 < i < key - 1 and j + cycle - 2 * i < len(encrypted_text):
                decrypted_text[j + cycle - 2 * i] = encrypted_text[index]
                index += 1

    return ' '.join(decrypted_text)



input_text = input("Plain text: ")
key = int(input("Key: "))
encrypted_text = rail_fence_encrypt(input_text, key)
print("Output:", encrypted_text)
decrypted_text = rail_fence_decrypt(encrypted_text, key)
print("Decrypted text:", decrypted_text)