import random


prog_languages = ["python", "java", "kotlin", "javascript"]
word_to_guess = random.choice(prog_languages)

user_word = input('''H A N G M A N \nGuess the word: ''')

if user_word == word_to_guess:
    print("You survived!")
else:
    print("You lost!")
