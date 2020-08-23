# HANGMAN 8/8

import random
words = ['python', 'java', 'kotlin', 'javascript']
dictionary = "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
tries = 8
choice = random.choice(words)
new_choice = []
symbol = []
for char in choice:
    new_choice.append("-")
print("H A N G M A N\n")
player = input("Type 'play' to play the game, 'exit' to quit: ")
while tries != 0:

    if player == 'play':
        print("".join(new_choice))
        if list(choice) == new_choice:
            print(f"You guessed the word {choice}!\n""You survived!")
            break

        guess = input("Input a letter: ")

        if guess != guess[0] or guess == ' ':
            print("You should input a single letter\n")

        if guess not in dictionary:
            print("It is not an ASCII lowercase letter\n")

        elif guess in new_choice:
            print("You already typed this letter\n")

        elif guess in choice:
            for i in range(len(choice)):
                char = choice[i]
                if char == guess:
                    new_choice[i] = choice[i]
            print("\n")

        else:
            if guess in symbol:
                print("You already typed this letter\n")
            else:
                tries -= 1
                if tries == 0:
                    print("No such letter in the word\n""You are hanged!")

                else:
                    print("No such letter in the word\n")
        symbol.append(guess)
    elif player == "exit":
        break
    else:
        print("error")

