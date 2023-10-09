from Crypto.Cipher import DES3
import binascii

def xor_encrypt(input_data, key):
    return bytes([a ^ b for a, b in zip(input_data, key)])

def main():
    # Original message
    message = b"Hello, XOR Encryption using 3DES!"

    # 3DES key (24 bytes)
    key = b"ThisIsMySecretKeyFor3DES"

    # XOR-like encryption
    xor_encrypted = xor_encrypt(message, key)

    # 3DES encryption
    cipher = DES3.new(key, DES3.MODE_ECB)
    des3_encrypted = cipher.encrypt(xor_encrypted)

    # Print the encrypted message
    encrypted_hex = binascii.hexlify(des3_encrypted).decode()
    print("Encrypted Message:", encrypted_hex)

if __name__ == "__main__":
    main()
