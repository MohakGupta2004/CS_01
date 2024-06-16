import argparse

def encrypt_text(plaintext, shift):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            isUpper = char.isupper()
            char = char.lower()
            index = ord(char) - ord('a')
            new_index = (index + shift) % 26
            new_char = chr(ord('a') + new_index)
            encrypted_text += new_char.upper() if isUpper else new_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt_text(ciphertext, shift):
    return encrypt_text(ciphertext, -shift)

def main():
    parser = argparse.ArgumentParser(description="Encrypt or decrypt a text using Caesar Cipher.")
    parser.add_argument('-e', '--encrypt', type=str, help="Text to encrypt")
    parser.add_argument('-d', '--decrypt', type=str, help="Text to decrypt")
    parser.add_argument('-s', '--shift', type=int, required=True, help="Shift value (1 to 26)")

    args = parser.parse_args()

    if args.encrypt:
        encrypted_text = encrypt_text(args.encrypt, args.shift)
        print(f"The Encrypted Text is: {encrypted_text}")
    elif args.decrypt:
        decrypted_text = decrypt_text(args.decrypt, args.shift)
        print(f"The Decrypted Text is: {decrypted_text}")
    else:
        print("You must specify either -e/--encrypt or -d/--decrypt with the text to process.")

if __name__ == "__main__":
    main()
