def cezur(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():

            offset = 65 if char.isupper() else 97
            encrypted += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            encrypted += char
    return str(encrypted)

def caesar_decrypt(text, shift):
    decrypted = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')

            decrypted += chr((ord(char) - base - shift) % 26 + base)
        else:
            decrypted += char

    return decrypted

def main():

    text = input("Tekst za kriptirane: ")

    while True:
        try:
            shift = int(input("Vuvedi s kolko da se izmestvat bukvite (0-25): "))
            if 0 <= shift <= 25:
                break
            else:
                print("Vuvedi chislo mejdu 0 i 25")
        except ValueError:
            print("Trqbva da e chislo")

    encrypted_text = cezur(text, shift)
    print(encrypted_text)


if __name__ == "__main__":
    main()
