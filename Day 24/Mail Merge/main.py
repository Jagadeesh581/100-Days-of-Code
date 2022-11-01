#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

# Save all the names as list from invited_names.txt.
with open("./Input/Names/invited_names.txt", "r") as names:
    all_names = names.readlines()

# Save all the contents of starting_letter.txt in variable.
with open("./Input/Letters/starting_letter.txt", "r") as letter:
    letter_content = letter.read()

for name in all_names:
    name = name.strip()
    # 'w' - write mode if the specified file not available then it will create a new file.
    # Write the finished letter replacing name with all_names list.
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w") as letter:
        letter.write(letter_content.replace("[name]", name))
