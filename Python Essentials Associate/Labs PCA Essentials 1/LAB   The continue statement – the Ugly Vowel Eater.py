# Prompt the user to enter a word
user_word = input("Invia una parola: ")

# Convert the word entered by the user to upper case
user_word = user_word.upper()

# Define a string containing all vowels to be "eaten"
vowels = "AEIOU"

for letter in user_word:
    if letter in vowels:
        continue
    elif letter not in vowels:
        print(letter)
    else:
        print("Inaspettata lettera")