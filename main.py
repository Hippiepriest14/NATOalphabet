import pandas

file = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet = {row.letter:row.code for (index,row) in file.iterrows()}

def generate_word():

    word = input("Enter a word: ").upper()
    try:
        new_word = [alphabet[letter] for letter in word]
        print(new_word)
    except KeyError:
        print("Sorry,use only letters.")
        generate_word()

generate_word()




