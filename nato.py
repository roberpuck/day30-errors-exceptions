# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def convert_word(wr):
    try:
        output_list = [phonetic_dict[letter] for letter in wr]
        print(output_list)
    except KeyError:
        print("Sorry, only letter in the alphabet please.")
        return

app_on = True

while app_on:
    word = input("Enter a word: ").upper()
    if word != 'EXIT':
        convert_word(word)
    else:
        app_on = False