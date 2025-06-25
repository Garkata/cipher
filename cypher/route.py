import math

def create_grid(message):
    message = message.replace(" ", "").upper()
    length = len(message)
    rows = math.floor(math.sqrt(length))
    cols = math.ceil(length / rows)

    while rows * cols < length:
        rows += 1

    grid = [['X' for _ in range(cols)] for _ in range(rows)]
    i = 0
    for r in range(rows):
        for c in range(cols):
            if i < len(message):
                grid[r][c] = message[i]
                i += 1
    return grid

def custom_zigzag_read(grid):
    rows = len(grid)
    cols = len(grid[0])
    result = []

    for c in range(cols):
        if c % 2 == 0:
            # Upward direction from bottom to top
            for r in reversed(range(rows)):
                result.append(grid[r][c])
        else:
            # Downward direction from top to bottom
            for r in range(rows):
                result.append(grid[r][c])
    return ''.join(result)

def create_grid_dimensions(message_length):
    rows = math.floor(math.sqrt(message_length))
    cols = math.ceil(message_length / rows)

    while rows * cols < message_length:
        rows += 1

    return rows, cols
def decrypt_custom_route_cipher(ciphertext):
    ciphertext = ciphertext.upper().replace(" ", "")
    length = len(ciphertext)
    rows, cols = create_grid_dimensions(length)


    grid = [['' for _ in range(cols)] for _ in range(rows)]

    i = 0
    for c in range(cols):
        if c % 2 == 0:

            for r in reversed(range(rows)):
                if i < length:
                    grid[r][c] = ciphertext[i]
                    i += 1
        else:

            for r in range(rows):
                if i < length:
                    grid[r][c] = ciphertext[i]
                    i += 1


    result = []
    for r in range(rows):
        for c in range(cols):
            result.append(grid[r][c])

    return ''.join(result).rstrip('X')

def encrypt_custom_route_cipher(message):
    grid = create_grid(message)
    return custom_zigzag_read(grid)

# 🔁 User Input
if __name__ == "__main__":
    plaintext = input("Enter your message: ")
    ciphertext = encrypt_custom_route_cipher(plaintext)
    print("Encrypted message:", ciphertext)

