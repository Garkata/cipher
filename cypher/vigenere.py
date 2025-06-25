def vigenere(plaintext, keyword):
    encrypted = ""
    keyword_index = 0
    keyword = keyword.upper()

    for char in plaintext:
        if char.isalpha():
            k = ord(keyword[keyword_index % len(keyword)]) - ord('A')

            if char.isupper():
                base = ord('A')
                p = ord(char) - base
                c = (p + k) % 26
                encrypted += chr(base + c)
            else:
                base = ord('a')
                p = ord(char) - base
                c = (p + k) % 26
                encrypted += chr(base + c)

            keyword_index += 1
        else:
            encrypted += char

    return encrypted

def vigenere_decrypt(ciphertext, keyword):
    decrypted = ""
    keyword_index = 0
    keyword = keyword.upper()

    for char in ciphertext:
        if char.isalpha():
            k = ord(keyword[keyword_index % len(keyword)]) - ord('A')

            if char.isupper():
                base = ord('A')
                c = ord(char) - base
                p = (c - k) % 26
                decrypted += chr(base + p)
            else:
                base = ord('a')
                c = ord(char) - base
                p = (c - k) % 26
                decrypted += chr(base + p)

            keyword_index += 1
        else:
            decrypted += char
    return decrypted

def main():
    plaintext = input("text: ")
    keyword = input("keyword: ")

    ciphertext = vigenere(plaintext, keyword)
    print("Encrypted:", ciphertext)

if __name__ == "__main__":
    main()
