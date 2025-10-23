def encrypt(text, shift):
    """Encrypt the text using Caesar Cipher."""
    result = ""
    for char in text:
        if char.isalpha():  # Encrypt only letters
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char  # Keep non-alphabetic characters unchanged
    return result


def decrypt(text, shift):
    """Decrypt the text using Caesar Cipher."""
    return encrypt(text, -shift)  # Just shift in the opposite direction


def main():
    print("=== Caesar Cipher Encryption & Decryption ===")
    message = input("Enter your message: ")
    shift = int(input("Enter shift value (1-25): "))

    encrypted = encrypt(message, shift)
    decrypted = decrypt(encrypted, shift)

    print("\n--- Results ---")
    print(f"Original Message: {message}")
    print(f"Encrypted Message: {encrypted}")
    print(f"Decrypted Message: {decrypted}")


if __name__ == "__main__":
    main()