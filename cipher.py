import string

def decoder(word, shift):
    word = word.replace(',',"")
    alphabet = string.ascii_lowercase
    letters = list(word.lower())
    for i in range(len(letters)):
        index = alphabet.find(letters[i])
        index += int(shift)
        if index >= 26:
            index = index % 26
            letters[i] = alphabet[index]
        else:
            letters[i] = alphabet[index]
    word = "".join(letters)
    return word

def main():
    word, shift = input().split()
    print(decoder(word, shift))

main()