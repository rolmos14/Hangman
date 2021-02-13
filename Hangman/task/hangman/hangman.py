import random


prog_languages = ["python", "java", "kotlin", "javascript"]

print("H A N G M A N")

while True:

    play_quit = input('Type "play" to play the game, "exit" to quit: ')
    if play_quit == "exit":
        break  # finish game
    if play_quit != "play":
        continue  # ask again

    attempts = 8
    word_to_guess = random.choice(prog_languages)
    word_to_show = "-" * len(word_to_guess)
    letters_guessed = set()

    while attempts:

        print("\n" + word_to_show)
        user_letter = input("Input a letter: ")

        if len(user_letter) != 1:
            print("You should input a single letter")
            continue  # while

        if not user_letter.islower():
            print("Please enter a lowercase English letter")
            continue  # while

        if user_letter in letters_guessed:
            print("You've already guessed this letter")
            continue  # while
        letters_guessed.add(user_letter)

        if user_letter in word_to_guess:
            for i in range(len(word_to_guess)):
                if word_to_guess[i] == user_letter:
                    word_to_show = word_to_show[:i] + user_letter + word_to_show[i + 1:]
            if word_to_guess == word_to_show:
                break  # exit while
        else:
            print("That letter doesn't appear in the word")
            attempts -= 1

    if attempts:
        print("\n",
              word_to_guess,
              "You guessed the word!",
              "You survived!",
              sep="\n")
    else:
        print("You lost!")
