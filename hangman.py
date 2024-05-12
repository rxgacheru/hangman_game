import random

def main():
    words = ["abruptly", "absurd", "bagpipes", "beekeeper", "cobweb.", "cycle", "python", "flapjack", "flyby", "sweatshirt", "sweatpants", "mattress", "friends", "clocks", "biology", "algebra", "suitcase", "knives", "ninjas", "zombie"]
    chosen_word = random.choice(words).lower()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman! Try to guess the chosen word correctly letter by letter before you run out of attempts.")

    while attempts > 0:
        print("Attempts remaining:", attempts)
        print("Guessed letters:", guessed_letters)

        for letter in chosen_word:
            if letter in guessed_letters:
                print(letter, end=" ")
            else:
                print("_", end=" ")
        
        guess = input("\nEnter a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.append(guess)

        if guess not in chosen_word:
            attempts -= 1

        # Check if the player has won
        if all(letter in guessed_letters for letter in chosen_word):
            print("\nCongratulations! You guessed the word:", chosen_word)
            break

    # Check if the player has lost
    if attempts == 0:
        print("\nSorry, you ran out of attempts. The word was:", chosen_word)

if __name__ == "__main__":
    main()
