import random


prog_languages = ["python", "java", "kotlin", "javascript"]
word_to_guess = random.choice(prog_languages)
word_to_show = word_to_guess[0:3] + (len(word_to_guess) - 3) * "-"

user_word = input(f'''H A N G M A N \nGuess the word {word_to_show}: ''')

if user_word == word_to_guess:
    print("You survived!")
else:
    print("You lost!")
