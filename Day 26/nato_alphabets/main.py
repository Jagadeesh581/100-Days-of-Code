import pandas


nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Create a dictionary.
nato_alphabet_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}
print(nato_alphabet_dict)

# Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ").upper()
user_output_list = [nato_alphabet_dict[letter] for letter in user_input]
print(user_output_list)
