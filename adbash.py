def ADbash(text):
 encrypted = ""
 for char in text:
     if char.isalpha():
         if char.isupper():
             encrypted = encrypted + chr(65+(25-(ord(char)-65)))
         else:
             encrypted = encrypted + chr(97+(25-(ord(char)-97)))
     else:
         encrypted = encrypted + char
 return encrypted

def main():
    text = input("Tekst za kriptirane(adbash): ")
    encrypt = ADbash(text)
    print(encrypt)

if __name__ == "__main__":
    main()