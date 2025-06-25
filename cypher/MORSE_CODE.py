# Morse code dictionary
MORSE_CODE_DICT = {
    'A': '.-',    'B': '-...',  'C': '-.-.', 'D': '-..',
    'E': '.',     'F': '..-.',  'G': '--.',  'H': '....',
    'I': '..',    'J': '.---',  'K': '-.-',  'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',  'P': '.--.',
    'Q': '--.-',  'R': '.-.',   'S': '...',  'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',  'X': '-..-',
    'Y': '-.--',  'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---','3': '...--',
    '4': '....-', '5': '.....', '6': '-....','7': '--...',
    '8': '---..', '9': '----.',
    '.': '.-.-.-',',': '--..--','?': '..--..','!': '-.-.--',
    '/': '-..-.', '(': '-.--.', ')': '-.--.-','&': '.-...',
    ':': '---...', ';': '-.-.-.','=': '-...-','+': '.-.-.',
    '-': '-....-', '_': '..--.-','"': '.-..-.','$': '...-..-',
    '@': '.--.-.', ' ': '/'
}
REVERSE_MORSE_CODE_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}
def decrypt_from_morse(morse_code):
    words = morse_code.strip().split(' / ')
    decoded_message = []
    for word in words:
        letters = word.split()
        decoded_word = ''.join(REVERSE_MORSE_CODE_DICT.get(letter, '?') for letter in letters)
        decoded_message.append(decoded_word)
    return ' '.join(decoded_message)

# Encryption function only
def encrypt_to_morse(text):
    text = text.upper()
    return ' '.join(MORSE_CODE_DICT.get(char, '') for char in text)

# Example usage
if __name__ == "__main__":
    plain = input("Enter your message: ")
    print("Morse Code:", encrypt_to_morse(plain))
