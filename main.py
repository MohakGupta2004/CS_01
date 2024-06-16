import argparse

def caesar_cipher(text, shift):
    def shift_char(char):
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            return chr((ord(char) - offset + shift) % 26 + offset)
        return char

    return ''.join(shift_char(char) for char in text)

def main():
    parser = argparse.ArgumentParser(description="Encrypt or decrypt a text using Caesar Cipher.")
    parser.add_argument('-e', '--encrypt', type=str, help="Text to encrypt")
    parser.add_argument('-d', '--decrypt', type=str, help="Text to decrypt")
    parser.add_argument('-s', '--shift', type=int, required=True, help="Shift value (1 to 26)")

    args = parser.parse_args()

    if args.encrypt:
        encrypted_text = caesar_cipher(args.encrypt, args.shift)
        print(f"The Encrypted Text is: {encrypted_text}")
    elif args.decrypt:
        decrypted_text = caesar_cipher(args.decrypt, -args.shift)
        print(f"The Decrypted Text is: {decrypted_text}")
    else:
        print("You must specify either -e/--encrypt or -d/--decrypt with the text to process.")

if __name__ == "__main__":
    main()
