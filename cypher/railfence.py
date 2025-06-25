def rail_fence_encrypt(text, num_rails):
    if num_rails <= 1:
        return text
    rails = ['' for _ in range(num_rails)]

    rail = 0
    direction = 1

    for char in text:
        rails[rail] += char

        rail += direction

        if rail == 0 or rail == num_rails - 1:
            direction *= -1


    return ''.join(rails)

def rail_fence_decrypt(ciphertext, num_rails):
    if num_rails <= 1 or num_rails >= len(ciphertext):
        return ciphertext

    zigzag = [['\n' for _ in range(len(ciphertext))] for _ in range(num_rails)]

    rail = 0
    direction = 1

    for i in range(len(ciphertext)):
        zigzag[rail][i] = '*'
        rail += direction

        if rail == 0 or rail == num_rails - 1:
            direction *= -1

    index = 0
    for r in range(num_rails):
        for c in range(len(ciphertext)):
            if zigzag[r][c] == '*' and index < len(ciphertext):
                zigzag[r][c] = ciphertext[index]
                index += 1


    rail = 0
    direction = 1
    result = ''
    for i in range(len(ciphertext)):
        result += zigzag[rail][i]
        rail += direction

        if rail == 0 or rail == num_rails - 1:
            direction *= -1

    return result

def main():

    plaintext = input("Text: ")
    num_rails = int(input("Rails: "))

    encrypted = rail_fence_encrypt(plaintext, num_rails)
    print("Encrypted:", encrypted)

if __name__ == "__main__":
    main()
