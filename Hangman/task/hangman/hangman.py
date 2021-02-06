import random


prog_languages = ["python", "java", "kotlin", "javascript"]
attempts = 8
word_to_guess = random.choice(prog_languages)
word_to_show = "-" * len(word_to_guess)

print("H A N G M A N")

for _ in range(attempts):
    print("\n" + word_to_show)
    user_letter = input("Input a letter: ")
    if user_letter in word_to_guess:
        if user_letter not in word_to_show:
            for i in range(len(word_to_guess)):
                if word_to_guess[i] == user_letter:
                    word_to_show = word_to_show[:i] + user_letter + word_to_show[i + 1:]
    else:
        print("That letter doesn't appear in the word")

print("",
      "Thanks for playing",
      "We'll see how well you did in the next stage",
      sep="\n")
