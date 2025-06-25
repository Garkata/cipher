def create_polybius_square():
    square = [
        ['a', 'b', 'c', 'd', 'e'],
        ['f', 'g', 'h', 'i', 'k'],
        ['l', 'm', 'n', 'o', 'p'],
        ['q', 'r', 's', 't', 'u'],
        ['v', 'w', 'x', 'y', 'z']
    ]
    letter_to_coords = {}
    coords_to_letter = {}

    for row in range(5):
        for col in range(5):
            letter = square[row][col]
            letter_to_coords[letter] = (row + 1, col + 1)
            coords_to_letter[(row + 1, col + 1)] = letter

    return letter_to_coords, coords_to_letter


def bifid_decrypt(ciphertext):
    letter_to_coords, coords_to_letter = create_polybius_square()
    ciphertext = ciphertext.lower().replace('j', 'i')

    coords = []
    for char in ciphertext:
        if char in letter_to_coords:
            coords.extend(letter_to_coords[char])
        else:
            raise ValueError(f"Invalid character: {char}")

    half = len(coords) // 2
    rows = coords[:half]
    cols = coords[half:]
    pairs = list(zip(rows, cols))

    decrypted = ''.join(coords_to_letter[(r, c)] for r, c in pairs)
    return decrypted


# ==== Run the decryption ====
if __name__ == "__main__":
    encrypted_input = input("Enter the encrypted text: ")
    try:
        result = bifid_decrypt(encrypted_input)
        print("Decrypted text:", result)
    except ValueError as e:
        print("Error:", e)
