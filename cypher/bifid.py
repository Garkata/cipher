def bifid(text):

    square = [
        ['a', 'b', 'c', 'd', 'e'],
        ['f', 'g', 'h', 'i', 'k'],
        ['l', 'm', 'n', 'o', 'p'],
        ['q', 'r', 's', 't', 'u'],
        ['v', 'w', 'x', 'y', 'z']
    ]


    letter_to_coords = {}
    for row in range(5):
        for col in range(5):
            letter = square[row][col]
            letter_to_coords[letter] = (row + 1, col + 1)

    # Preprocess input
    text = text.lower().replace('j', 'i')


    rows, cols = [], []
    for char in text:
        if char in letter_to_coords:
            r, c = letter_to_coords[char]
            rows.append(str(r))
            cols.append(str(c))
        else:
            raise ValueError(f"Invalid character: {char}")


    combined = rows + cols

    pairs = [(int(combined[i]), int(combined[i+1])) for i in range(0, len(combined), 2)]


    encrypted = ''
    for r, c in pairs:
        encrypted += square[r - 1][c - 1]

    return encrypted

def main():
    text = input("Duma:")
    print(bifid(text))


if __name__ == "__main__":
    main()