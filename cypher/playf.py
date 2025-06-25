import string

def prepare_text(text):
    text = text.upper().replace("J", "I")
    text = ''.join(filter(str.isalpha, text))
    result = ""
    i = 0

    while i < len(text):
        a = text[i]
        if i + 1 < len(text):
            b = text[i + 1]
            if a == b:
                result += a + 'X'
                i += 1
            else:
                result += a + b
                i += 2
        else:
            result += a + 'X'
            i += 1
    return result

def create_key_square(key):
    key = key.upper().replace("J", "I")
    seen = set()
    square = []

    for char in key + string.ascii_uppercase:
        if char not in seen and char in string.ascii_uppercase and char != 'J':
            seen.add(char)
            square.append(char)
        if len(square) == 25:
            break

    return [square[i*5:(i+1)*5] for i in range(5)]

def find_position(square, letter):
    for row in range(5):
        for col in range(5):
            if square[row][col] == letter:
                return row, col
    return None, None

def encrypt_pair(square, a, b):
    row1, col1 = find_position(square, a)
    row2, col2 = find_position(square, b)

    if row1 == row2:
        # Same row → move right
        return square[row1][(col1 + 1) % 5] + square[row2][(col2 + 1) % 5]
    elif col1 == col2:
        # Same column → move down
        return square[(row1 + 1) % 5][col1] + square[(row2 + 1) % 5][col2]
    else:
        # Rectangle → swap columns
        return square[row1][col2] + square[row2][col1]

def playfair_encrypt(message, key):
    square = create_key_square(key)
    text = prepare_text(message)
    encrypted = ""

    for i in range(0, len(text), 2):
        encrypted += encrypt_pair(square, text[i], text[i+1])
    return encrypted

def playfair_decrypt(message, key):
    square = create_key_square(key)
    text = prepare_text(message)
    encrypted = ""

    for i in range(0, len(text), 2):
        encrypted += decrypt_pair(square, text[i], text[i+1])
    return encrypted

def decrypt_pair(square, a, b):
    row1, col1 = find_position(square, a)
    row2, col2 = find_position(square, b)

    if row1 == row2:
        # Same row → move right
        return square[row1][(col1 - 1) % 5] + square[row2][(col2 - 1) % 5]
    elif col1 == col2:
        # Same column → move down
        return square[(row1 - 1) % 5][col1] + square[(row2 - 1) % 5][col2]
    else:
        # Rectangle → swap columns
        return square[row1][col2] + square[row2][col1]

# 🔁 User Input
if __name__ == "__main__":
    message = input("Enter your message: ")
    key = input("Enter the keyword: ")
    encrypted = playfair_encrypt(message, key)
    print("Encrypted message:", encrypted)