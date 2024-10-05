import random

def get_random_word():
    words = ['python', 'hangman', 'challenge', 'programming', 'random', 'computer', 'game', 'developer']
    return random.choice(words)

def display_word(word, guessed_letters):
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    word = get_random_word()
    guessed_letters = []
    wrong_guesses = 0
    max_wrong_guesses = 7

    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters.")

    while wrong_guesses < max_wrong_guesses:
        print("\nWord: ", display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"Good job! {guess} is in the word.")
        else:
            wrong_guesses += 1
            print(f"Sorry, {guess} is not in the word. You have {max_wrong_guesses - wrong_guesses} wrong guesses left.")

        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations! You guessed the word: {word}")
            break
    else:
        print(f"\nYou lost! The word was: {word}")

if __name__ == "__main__":
    hangman()


#new comment
