word_without_vowels = ""

user_word = input("Inserisci una parola: ") 
user_word = user_word.upper()

vowels = "AEIOU"

for letter in user_word:
    if letter in vowels:
        continue
    else:
        word_without_vowels += letter

print("Parola senza vocali:", word_without_vowels)
