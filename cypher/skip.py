def skip(text, key):
    encrypted = ""
    index = 0
    key+=1
    duljina = len(text)
    while(len(encrypted)!=duljina):
                   print(index)
                   encrypted += text[index]
                   index+=key
                   if index>=duljina:
                         index-=duljina
                         if(len(encrypted)==duljina):
                                return encrypted
                   if index== 0:
                         return "Greshka"
                   
    

def main():

    text = input("Tekst za kriptirane: ")

    key = int(input("Vuvedi s kolko da se izmestvat bukvite (0-25): "))

    encrypted_text = skip(text, key)
    print(encrypted_text)


if __name__ == "__main__":
    main()
