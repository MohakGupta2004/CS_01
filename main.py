# ENCRYPTION AND DECRYPTION OF A TEXT USING CAESER CIPHER - Prasunet Company
def encrypt_text(plaintext, shift):
    encrypt_text = ""
    for char in plaintext:
        if char.isalpha():
            isUpper = char.isupper()
            char = char.lower()
            index = ord(char) - ord('a')
            new_index = (index+shift) % 26
            new_char = chr(ord('a')+new_index)
            encrypt_text+=new_char.upper() if(isUpper) else new_char
        else:
            encrypt_text+=char
    
    return encrypt_text
         
def decrypt_text(ciphertext, shift):
    return encrypt_text(ciphertext,-shift)
    
def main():
    print("*************ENCRYPT/DECRYPTION OF A TEXT USING CAESER CIPHER*************")
    encrypt_or_decrypt = input("What you want to do? (e for Encrypt a sentence/d for Decrypt a sentence): ")
    if(encrypt_or_decrypt == "e"):
        user_input = input("Enter the text you want to encrypt:")
        shift = int(input("Enter the shift (1 to 26): "))
        encrypted_text = encrypt_text(user_input, shift)
        print(f"The Encrypted Text is: {encrypted_text}")
    elif(encrypt_or_decrypt == 'd'):
        user_input = input("Enter the text you want to decrypt:")
        shift = int(input("Enter the shift (1 to 26): "))
        encrypted_text = decrypt_text(user_input, shift)
        print(f"The Decrypted Text is: {encrypted_text}")
    else:
        print("Type a valid Arguement!!!!")

if __name__ == "__main__":
    main()