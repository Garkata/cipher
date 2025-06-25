import math
def create_column_order(keyword):

    order = sorted(list(enumerate(keyword)), key=lambda x: (x[1], x[0]))
    return [index for index, _ in order]

def columnar_encrypt(text, keyword):
    text = text.replace(" ", "")
    cols = len(keyword)
    order = create_column_order(keyword)


    rows = (len(text) + cols - 1) // cols
    padded_text = text.ljust(rows * cols, 'X')


    grid = [padded_text[i:i+cols] for i in range(0, len(padded_text), cols)]


    ciphertext = ''
    for col_index in order:
        for row in grid:
            ciphertext += row[col_index]
    return ciphertext

def columnar_decrypt(ciphertext, keyword):
    cols = len(keyword)
    rows = math.ceil(len(ciphertext) / cols)
    total_chars = len(ciphertext)


    order = create_column_order(keyword)


    full_cols = total_chars % cols
    short_cols = cols - full_cols if full_cols != 0 else 0


    grid = ['' for _ in range(cols)]
    index = 0
    for pos in range(cols):
        col_index = order[pos]
        col_len = rows - 1 if col_index >= cols - short_cols else rows
        grid[col_index] = ciphertext[index:index+col_len]
        index += col_len


    plaintext = ''
    for r in range(rows):
        for c in range(cols):
            if r < len(grid[c]):
                plaintext += grid[c][r]


    return plaintext

def main():
    text = input("Text: ")
    keyword = input("Keyword: ")
    encrypted = columnar_encrypt(text, keyword)
    print("Result:", encrypted)

if __name__ == "__main__":
    main()
